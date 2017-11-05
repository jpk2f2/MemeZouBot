#!/usr/bin/python3
#this bot posts text to a subreddit

import praw
import pdb
import re
import os
import logging
import subprocess
import requests

#Reddit instance
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('memezou')


structure = "Hello World"
message = "Hello World"

message2 = subreddit.submit(message, structure, send_replies=False)
print("posting to r/memezou")