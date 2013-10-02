LiveTwitterStreamSentimentAnalysis
==================================
This is one of my minor project from the DataScience course.I have collected live tweets from Twitter Social Networking site and
used the tweets for various findings.The project description is given below:



Twitter represents a fundamentally new instrument to make social measurements. Millions of people voluntarily express opinions across any topic imaginable --- this data source is incredibly valuable for both research and business.
 
For example, researchers have shown that the "mood" of communication on twitter reflects biological rhythms and can even used to predict the stock market. A student here at UW used geocoded tweets to plot a map of locations where "thunder" was mentioned in the context of a storm system in Summer 2012.
Researchers from Northeastern University and Harvard University studying the characteristics and dynamics of Twitter have an excellent resource for learning more about this area.
 
In this project, I have
 
●      access the twitter Application Programming Interface(API) using python.
●      estimate the public's perception (the sentiment) of a particular term or phrase.
●      analyze the relationship between location and mood based on a sample of twitter data.


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

**
This project is  poorly documented due to lack of time but I promise as soon as I get time I will properly document it
and include in it more findings.Sorry for the inconvenience.


