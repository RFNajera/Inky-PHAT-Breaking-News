#!/usr/bin/python3

#-----------------------------------------------------------------------
# Code to pull the latest breaking news tweet by the Associated Press from Twitter and display
# it in Pimoroni InkyPHAT display with code adapted from:
# Dan Aldred: https://github.com/TeCoEd/Yoda-Twitter-Streamer
# Sam Hector: https://github.com/samhector/InkyTwitterTrends
# Adam Bowie: https://www.adambowie.com/blog/2019/09/news-twitter-feeds-and-inky-what-e-ink-display/
# Earth Data Science: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
# Pimoroni Inky PHAT Getting Started:
# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
#-----------------------------------------------------------------------

import sys
sys.path.append(".")
import argparse # For parsing arguments: https://docs.python.org/3/howto/argparse.html
from PIL import Image, ImageFont, ImageDraw # Python Image Library
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium # For the fonts
from inky import InkyPHAT # For using the PHAT
import os # To interface with the operating system
import config # Where I stored the Twitter API keys
import tweepy as tw # Tweepy helps get data from Twitter: http://docs.tweepy.org/en/latest/

#-----------------------------------------------------------------------
# Twitter API object
#-----------------------------------------------------------------------
twitter = tw.OAuthHandler(config.consumer_key, config.consumer_secret) # Gets the consumer key and secret from the config file
twitter.set_access_token(config.access_key, config.access_secret) # Gets the access key and secret from the config gile
api = tw.API(twitter) # Creates api with all the information for accessing the API

#-----------------------------------------------------------------------
# Inky PHAT screen information
#-----------------------------------------------------------------------

colour="red" # There is also a yellow version: https://www.adafruit.com/product/3933 and a black/white version
inky_display = InkyPHAT(colour)
scale_size = 1
padding = 0

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(HankenGroteskMedium, 12) # Set the font type and size for tweets
font_bold = ImageFont.truetype(HankenGroteskBold, 14) # Set the font for header


#-----------------------------------------------------------------------
# Set the reflow to make sure the text fits into the screen
# Dan Aldred uses a better way that I couldn't just quite get going: https://github.com/TeCoEd/Yoda-Twitter-Streamer
#-----------------------------------------------------------------------

def reflow_tweet(quote, width, font):
    words = quote.split(" ")
    reflowed = ' '
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n " + word

    # reflowed = reflowed.rstrip() + '"'

    return reflowed

#----------------------------------------------------------------------
# Find the tweets and filter out retweets and replies
#----------------------------------------------------------------------

search_term = "from:ap" + " -filter:retweets" + " -filter:replies" # I'm using @AP from twitter and avoiding retweets and replies

# Collect tweets
tweets = tw.Cursor(api.search,
                   q = search_term,
                   lang="en",
                   result_type = "recent").items(1) # Return only one, the latest one

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text) # Don't really need iteration with one tweet at a time, but let in for when I get a bigger screen

#--------------------------------------------------------------------
# Make the tweet fit into the screen
#--------------------------------------------------------------------

reflowed_tweet = reflow_tweet(tweet.text, inky_display.WIDTH, font) # Formating the tweet text

#---------------------------------------------------------------------
# Display the tweets
#---------------------------------------------------------------------

draw.text((0,0), "Breaking News", inky_display.RED, font_bold) # Title of the screen at the top left (0,0)
draw.text((0,20), reflowed_tweet, inky_display.BLACK, font) # The text of the tweet will begin 20 spaces below the title (0,20)
inky_display.set_image(img)
inky_display.show()
