LiveTwitterStreamSentimentAnalysis
==================================
This is one of my minor project from the DataScience course.I have collected live tweets from Twitter Social Networking site and
used the tweets for various findings.The project description is given below:


Script twitterstream.py- Used to fetch live stream data from twitter
> Create a twitter account if you do not already have one.
> Go to https://dev.twitter.com/apps and log in with your twitter credentials.
> Click "create an application".
> Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
> On the next page, scroll down and click "Create my access token".
> Copy your "Consumer key" and your "Consumer secret" into twitterstream.py.
> Click "Create my access token."
> Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret
> Run the following and make sure you see data flowing
$ python twitterstream.py
After this step we get raw twitter stream data.The data is dirty and is in json format.We need to parse the data to extract actual tweets from it.We can get the sample of the raw data in the file output.txt.

Findings:
> Sentiment score of each tweet based on sentiment scores of the terms in the AFINN-111.TXT file.(Turn tweet_sentiment.py).        
> Assignment of sentiment scores to new terms(Turn term_sentiment.py).
> Frequency Histogram of the live stream data(Turn frequency.py).
> Happiest State based on sentiment scores of geo tagged tweets(Turn happiest_state.py).
> Top ten hash tags(top_ten.py).


