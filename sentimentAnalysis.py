#!/usr/bin/env python3

#import TextBlob
from textblob import TextBlob

text = input("Enter your text to be analyzied: ")

obj = TextBlob(text)

#returns the sentiment of text
#by returning a value between -1.0 and 1.0 (-1.0 is very bad, 1.0 is very good)
sentiment = obj.sentiment.polarity

if sentiment > 0.25:
    print ("Good. Score: " + str(sentiment))
elif sentiment > -0.25 < 0.25: 
    print ("Indifferent. Score: " + str(sentiment))
elif sentiment < -0.25:
    print ("Bad. Score: " + str(sentiment))