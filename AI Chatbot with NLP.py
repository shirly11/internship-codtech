# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 22:32:29 2025

@author: ADMIN
"""
#1/6/25
#AI Chatbot with NLP

import nltk
import random
import string

from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you ?", ["I'm good, how about you?"]],
    ["what is your name ?", ["I'm your Python Chatbot."]],
    ["bye", ["Goodbye!", "See you later!"]],
    ["(.*)", ["Sorry, I don't understand that."]]
]

def chatbot():
    print("Start chatting with the bot (type 'bye' to stop)!")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
