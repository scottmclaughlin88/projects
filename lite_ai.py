#good practice to do a print to make sure script has no underlying issues.
#print('hello')
#https://karlamclaren.com/emotional-vocabulary-page/
import json
#put functions above print statements(good practice)
def get_messages():
    file = open('messages.txt','r')
    lines = file.readlines()
    messages = []
    for line in lines:
        messages.append(line.strip().split(' '))
    return messages

def get_wordscores():
    file = open('word_scores.txt','r')
    lines = file.readlines()
    messages = {}
    for line in lines:
        word = line.strip().split(' ')[0]
#if Python barks at you with something like 'int' and 'str', you need to convert such line using int, or str, etc ()
        score = int(line.strip().split(' ')[1])
        messages[word] = score
    return messages

def get_jsonwords():
    with open('wordlist.json',mode='r') as info:
        json_words = json.loads(info.read())
    print(json_words)

def get_message_scores(messages,scores):
    message_scores = []
    for message in messages:
        message_scores.append([message,get_score(message,scores)])
    return message_scores

#title and intitial description from CW (for later)
#adding categories to the dict
#build a baseline for a bassenian model.  later we can add a company modifier that adds exceptions (some people just are always threatening)
def get_score(message,scores):
    total_score = 0
    for word in message:
        if word in scores:
            total_score += scores[word]
    return total_score

def main():

    get_jsonwords()
    exit()

    messages = get_messages()
    # print(messages)
    scores = get_wordscores()
    # print(scores)
    message_scores = get_message_scores(messages,scores)
    for score in message_scores:
        print(score)

#you can put this on the bottom of your code
#helps to reduce confusion
if __name__=="__main__":
    main()
