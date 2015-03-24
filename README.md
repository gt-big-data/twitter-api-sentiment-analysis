Introduction to Big Data club
==============================

(This repo is meant to be an example for Big Data club presentations)

## Objective
Big data involves storing and analyzing difficult-to-work with data sets, either in scale or in lack of structure.
Over the semester, we'll look at technologies and algorithms that will allow us to do both on some interesting data sets. 

We will start with doing sentiment analysis on data collected from the Twitter streaming API. Among many other things, 
the Twitter API lets you search for tweets matching certain keywords. Sentiment analysis lets us analyze what Twitter
users think about the topics of their tweets.

After this, we will be able to answer questions like "What do people think about 
{Nexus 5, the election, Miley Cyrus, Facebook, etc}?"


## Installation
Using pip,
```pip install -r requirements.txt```
You may need ```sudo``` permissions, unless you are using virtualenv.

## Usage
The project comes with sample data sets you can analyze. The file ```sentiments.py``` is used to analyze downloaded
tweets in json format. Run it with
```python sentiments.py data/atl.json```
to view "interesting" tweets and the average sentiment of a sample of tweets about the Falcons - 49ers game.


### Downloading More Data
You can also download more data with ```hashtag_downloader.py```, which streams data from the search criteria to
standard out.
Run like
```python hashtag_downloader.py <topic>```
where topic can be anything you're interested in or that people might write interesting things about.

*HOWEVER* The downloader requires you to have Twitter API keys to stream the data, and we can't make these public on the internet... so get your own! 

1. Register your Twitter account with http://dev.twitter.com
2. Log in to dev.twitter.com and go to "My applications" (hover over your avatar)
3. Create a new app (gt-big-data, for instance)
4. Create access tokens in the new app.

Then use the information from this app (gt-big-data) to fill out an `api_keys.py`

The python file `hashtag_downloader.py` is expecting is a `api_keys.py` file with these four lines:

```
KEY='<consumer key>'
SECRET='<consumer secret>'
TOKEN= '<access (oath) token>'
TOKEN_SECRET= '<access (oath) token secret>'
```
from your Twitter app page. To generate access tokens, you'll need to create them within the Twitter app (there's a big button for it.)


## Further topics
*  Machine learning is used heavily with sentiment analysis. Look into NLTK to see far more sophistocated algorithms
for sentiment analysis beyond the rudimentary one used here.
*  Use the Twitter API to see how sentiment about a topic varies by location.
