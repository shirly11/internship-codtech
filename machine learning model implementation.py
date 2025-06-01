# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:58:39 2025

@author: ADMIN
#1/6/25
#machine learning model implementation
"""
import pandas as pd
import math
import string
from collections import defaultdict
from urllib.request import urlopen

# Load dataset from URL
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep="\t", names=["label", "message"])
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# Split data manually (80% train, 20% test)
split = int(0.8 * len(df))
train_data = df[:split]
test_data = df[split:]

# Basic preprocessing: lowercase, remove punctuation
def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

# Calculate prior probabilities and word counts
def train_naive_bayes(data):
    spam_words = defaultdict(int)
    ham_words = defaultdict(int)
    spam_total = 0
    ham_total = 0
    spam_count = 0
    ham_count = 0

    for _, row in data.iterrows():
        words = tokenize(row['message'])
        if row['label_num'] == 1:
            spam_count += 1
            for word in words:
                spam_words[word] += 1
                spam_total += 1
        else:
            ham_count += 1
            for word in words:
                ham_words[word] += 1
                ham_total += 1

    return {
        'spam_words': spam_words,
        'ham_words': ham_words,
        'spam_total': spam_total,
        'ham_total': ham_total,
        'spam_count': spam_count,
        'ham_count': ham_count,
        'vocab': set(list(spam_words.keys()) + list(ham_words.keys())),
        'total': spam_count + ham_count
    }

# Naive Bayes classifier
def predict(message, model):
    words = tokenize(message)
    spam_prob = math.log(model['spam_count'] / model['total'])
    ham_prob = math.log(model['ham_count'] / model['total'])

    for word in words:
        # Laplace smoothing
        spam_word_prob = (model['spam_words'][word] + 1) / (model['spam_total'] + len(model['vocab']))
        ham_word_prob = (model['ham_words'][word] + 1) / (model['ham_total'] + len(model['vocab']))
        spam_prob += math.log(spam_word_prob)
        ham_prob += math.log(ham_word_prob)

    return 1 if spam_prob > ham_prob else 0

# Train the model
model = train_naive_bayes(train_data)

# Predict and evaluate
correct = 0
for _, row in test_data.iterrows():
    prediction = predict(row['message'], model)
    if prediction == row['label_num']:
        correct += 1

accuracy = correct / len(test_data)
print("Accuracy (no sklearn):", round(accuracy * 100, 2), "%")
