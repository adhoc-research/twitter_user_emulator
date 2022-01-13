import os
import shutil

from datetime import datetime
import gpt_2_simple as gpt2

from . import download_tweets
from . import preprocessor


def train_gpt_2(out_tweets):
    '''
    Trains GPT-2 model and generates tweets to a file in the working directory.

    Args:
        out_tweets (int): Number of tweets to generate. 1000 by default.

    Returns:
        None

    Raises:
        OSError: If an error occurs when trying to delete the directories
    '''

    # adapts some hyperparameters based on file size
    if (os.path.getsize("tweets_file.txt") >= 1000000):
        model_name = "355M"
        lr = 1e-4
    else:
        model_name = "124M"
        lr = 1e-5

    print("Downloading specified model...")
    gpt2.download_gpt2(model_name=model_name)  # downloads specified gpt model

    sess = gpt2.start_tf_sess()  # starts tensorflow session

    print("Finetuning model...")
    # finetunes gpt-2
    gpt2.finetune(sess,
                dataset="tweets_file.txt",
                model_name=model_name,
                steps=2000,
                learning_rate=lr,
                restore_from="fresh",
    )
                
    gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())  # timestamped text file

    # generates output file with tweets
    gpt2.generate_to_file(sess,
                      destination_path=gen_file,  # output file destination
                      length=200,
                      temperature=1.0,
                      top_p=0.9,
                      prefix='<|startoftext|>',  # start tag
                      truncate='<|endoftext|>',  # end tag
                      include_prefix=False,
                      nsamples=out_tweets,  # number of tweets to generate
                      batch_size=20,
    )

    try:
        os.remove("tweets_file.txt")  # deletes downloaded tweets
        shutil.rmtree("models")  #  deletes downloaded model
        shutil.rmtree("checkpoint")  # deletes trained model
        shutil.rmtree("samples")  # deletes samples folder
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def emulate_user(user, start_date, end_date, out_tweets=1000):
    '''
    Args:
        user (str): Username for account to scrape for tweets
        start_date (str): Date to start scraping tweets from (YYYY-MM-DD)
        end_date (str): Date to end scraping tweets at (YYYY-MM-DD)
        out_tweets (int): Number of tweets to generate
    
    Returns:
        None
    '''
    
    delimiter = "=========================="

    print(f"{delimiter}\nDownloading Tweets...\n{delimiter}")
    tweets_df = download_tweets.get_tweets_csv(user, start_date, end_date)
    
    print(f"{delimiter}\nCleaning Tweets...\n{delimiter}")
    tweets_df = preprocessor.preprocessor(tweets_df)
    preprocessor.formatter(tweets_df)

    print(f"{delimiter}\nEmulating User...\n{delimiter}")
    train_gpt_2(out_tweets)

    print("All done! You may now find the output CSV in your working directory.")
