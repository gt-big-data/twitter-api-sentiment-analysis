import re
import sys
import json

def get_tweet_sentiment(tweet_dict, weights):
    score = 0.0
    text = ""
    if u'text' in tweet_dict:
        utf8_text = tweet_dict[u'text']
        text = utf8_text
        toks = re.split('\s+', utf8_text.lower())
        for word in toks:
            word = re.sub('\W', '', word)
            if word in weights:
                score += weights[word]
        score = min(6, score)
        score = max(-6, score)
        for word in toks:
            word = re.sub('\W', '', word)
            if word not in weights and len(word) > 3:
                weights[word] = 0

    return score, text

def readWeights():
    weights = {}
    with open('sentiments.txt') as f:
        for line in f:
            toks = re.split('\s+', line.strip().lower()) 
            if len(toks) == 2:
                word = toks[0]
                word = re.sub('\W', '', word)
                weights[word] = float(toks[1])
    return weights

def main(tweet_file):
    weights = readWeights()
    sentiments = []
    with open(tweet_file) as tf:
        for line in tf:
            if line:
                tweet = json.loads(line)
                score, tweet_text = get_tweet_sentiment(tweet, weights)
                if abs(score) > 2:
                    print tweet_text, " had score ", score
                sentiments.append(score)
    total = 0.0
    for num in sentiments:
        total += num
    print total / len(sentiments)

if __name__ == '__main__':
    main(sys.argv[1])
