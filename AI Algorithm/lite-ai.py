import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_top_tweets(scored_tweets,num = 10, reverse=False):
    sorted_tweets = dict(sorted(scored_tweets.items(),key = lambda x : x[1],reverse=reverse))
    tweets = list(sorted_tweets.keys())[0:num]
    return tweets
    
#Create file of words at the 0 index
def generated_word_scores(word_frequency):
    f = open('automatic_word_scores.txt','w')
    for word in word_frequency:
        f.write(word[0] + '\n')
    f.close()

#Create file of filtered words
def create_exclusion_list(filtered_words):
    f = open('filtered_words.txt','w')
    for word in filtered_words:
        f.write(word[0] + '\n')
    f.close()

#Dump filtered words to file
def filtered_word_frequency(word_frequency):
    f = open('filtered_words.txt','r')
    filtered_words = f.readlines()
    for word in filtered_words:
        word_frequency.pop(word.strip())
    return word_frequency

#Get frequency of word occurrance from data
def get_word_frequency(messages):
    word_frequency = {}
    for message in messages:
        for word in message:
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
    return word_frequency
  
# def get_messages():
#     file = open('messages.txt','r')
#     lines = file.readlines()
#     messages = []
#     for line in lines:
#         messages.append(line.strip().split(' '))
#     return messages

#Create a dict, get word scores
def get_wordscores():
    file = open('automatic_word_scores.txt','r')
    lines = file.readlines()
    messages = {}
    for line in lines:
        word = line.strip().split(' ')[0]
        score = int(line.strip().split(' ')[1])
        messages[word] = score
    return messages

def clean_messages(messages,bad_letters):
    clean_messages = []
    # print(bad_letters)
    for message in messages:
        clean_messages.append(clean_message(message,bad_letters))
    return clean_messages

def clean_message(message,bad_letters):
    clean_message = []
    for word in message:
        for letter in bad_letters:
            if letter in word:
                word = word.replace(letter,'')
        clean_message.append(word)
    return clean_message

#Create a dict of messages
def get_message_scores(messages,scores):
    message_scores = {}
    for message in messages:
        message_scores[str(message)] = get_score(message,scores)
    return message_scores

#Add up the message scores
def get_score(message,scores):
    total_score = 0
    for word in message:
        if word in scores:
            total_score += scores[word]
    return total_score


# messages = get_messages()
# messages = clean_messages(messages,'.,;:"')
# # print(messages)
# scores = get_wordscores()
# # print(scores)
# message_scores = get_message_scores(messages,scores)
# #items grabs everything out of the dictionary
# for message,score in message_scores.items():
#     print(message,score)
# scores_list = list(message_scores.values())
# print(scores_list)

# plt.plot(scores_list)
# plt.show()

#Pandas recommends ISO-8859-1 for encoding this type of data
def load_twitter_data(filename):
    df = pd.read_csv(filename, encoding = 'ISO-8859-1')
    return df

#Load data file
df = load_twitter_data('twitter.csv')
text = list(df['text'])
scores = get_wordscores()
text_as_words = []
#Run loop to remove all punctionation we don't want
for message in text:
    text_as_words.append(message.split(' '))
text_as_words = clean_messages(text_as_words,'.,;:"')
text_scores = get_message_scores(text_as_words,scores)
# for message,score in text_scores.items():
#     print(message,score)

#Create visualizer
# print(list(text_scores.values()))
print(len(list(text_scores.values())))
scores_to_view = list(text_scores.values())[0:3214]
times = list(range(0,3214))
times = np.array(times)
m,b = np.polyfit(times, scores_to_view, 1)
# print(times)
plt.plot(times, scores_to_view, 'o')
plt.plot(times, m*times + b, color = 'red')
plt.show()
# print(text[0:75])
word_frequency = get_word_frequency(text_as_words)
word_frequency_filtered = filtered_word_frequency(word_frequency)
sorted_list = sorted(word_frequency_filtered.items(),key = lambda x : x[1], reverse = True)
exclusion_list = sorted_list[0:50]

# generated_word_scores(sorted_list[0:100])
# for item in exclusion_list:
#     print(item)
# print(sorted_list[0:25])
# print(word_frequency_list[0:10])
# create_exclusion_list(exclusion_list)

#Print the worst and best tweets
print('Worst tweets:')
top_tweets = get_top_tweets(text_scores)
for tweet in top_tweets:
    print(tweet.replace(',','').replace("'", ''))
print('Best tweets:')

top_tweets = get_top_tweets(text_scores, reverse=True)
for tweet in top_tweets:
    print(tweet.replace(',','').replace("'", ''))