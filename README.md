# twitter_user_emulator

A simple Python package that wraps [scweet](https://github.com/Altimis/Scweet) and [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) to allow easy tweet generation based on any existing Twitter account.

The idea of this project is to let anyone unfamiliar with GPT-2 to create their own Twitter bot emulating an existing account (e.g., [Deep Leffen](https://twitter.com/DeepLeffen), [Deep Slacks Bot](https://twitter.com/DeepSlacks), [Deep Bumpaah Bot](https://twitter.com/boomer_bump_bot)) in a single API call. The library handles all boilerplate code and basic hyperparameter tuning involved, allowing the user to spend that time curating tweets they want instead.

# Install
twitter_user_emulator can be installed [via PyPi](https://pypi.org/project/twitter-user-emulator/0.0.1/):

`pip3 install twitter_user_emulator`

To enable GPU usage for faster training (recommended), a version of Tensorflow 2.X (min 2.5.1) must be installed on your system.

# Usage

An example API call:

```
from twitter_user_emulator import emulator

emulator.emulate_user(user="bumpaah", start_date="2020-01-01", end_date="2021-01-01", out_tweets=2000)
```

This piece of code will download and train a gpt-2 model to generate 2000 tweets based on all the tweets user @bumpaah made between 2020-01-01 and 2021-01-01.

>The model will fail to train if there are not enough tweets as input. Please try to pick a time range with at least 500 tweets.

# Colab Notebook
A notebook tutorial that goes over the underlying logic of this implementation can be found [here](https://colab.research.google.com/drive/1buFScRhtOLZQdTbb6rYH2QlYvH4sDlgt).

# License
MIT

# Disclaimer
This repo has no affiliation with OpenAI or Twitter.
