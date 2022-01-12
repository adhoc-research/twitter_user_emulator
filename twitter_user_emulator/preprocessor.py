def delimiter_cleaner(split_string):
    '''
    Removes delimiters from tweets.

    Args:
        split_string (str): Tweet to split

    Returns:
        If downloaded tweet has no delimiters:
            split_string (str): Original tweet
        If downloaded tweet has delimiters:
            split_string_clean (str): Tweet with delimiters cleaned
    '''
    if isinstance(split_string, list):  # if there was a delimiter in the text
        split_string_clean = []
        for seg in split_string:  # iterates parts segmented by the delimiter
            if (seg.isnumeric()):  # if segment contains only numbers
                pass
            elif seg == "Replying to ":  # if segment is replying template text
                pass
            elif seg.startswith("@"):  # if segment contains only a username
                pass
            else:
                split_string_clean.append(seg)

        split_string_clean = ''.join(split_string_clean)  # concatenates list items into single string
            
        return split_string_clean
    else:
        return split_string


def preprocessor(tweets_df):
    '''
    Cleans tweets dataframe.

    Args:
        tweets_df (Pandas Dataframe): Downloaded tweets

    Returns:
        tweets_df_clean (Pandas Dataframe): Cleaned downloaded tweets
    '''
    
    # removes entries with nan in tweets column
    tweets_df_clean = tweets_df[tweets_df['Embedded_text'].notna()]

    # splits tweets into segments separated by the \n delimiter
    tweets_df_clean["Embedded_text_clean"] = tweets_df_clean['Embedded_text'].str.split('\n')

    # applies delimiter cleaning function and pushes output to new column
    tweets_df_clean["Embedded_text_clean"] = tweets_df_clean["Embedded_text_clean"].apply(delimiter_cleaner)

    # removes tweets with a length less than 5 characters
    tweets_df_clean = tweets_df_clean[tweets_df_clean['Embedded_text_clean'].str.len()>=5]

    return tweets_df_clean


def formatter(tweets_df):
    '''
    Writes formatted tweets to a text file.

    Args:
        tweets_df (Pandas Dataframe): Downloaded tweets

    Returns:
        None
    '''

    with open("tweets_file.txt", 'w') as tweets_file:
        for t in tweets_df:
            tweets_file.write('<|startoftext|>'+t+'<|endoftext|>')



