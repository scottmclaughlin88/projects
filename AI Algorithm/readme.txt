#This is an update to the original lite-ai.py file, including a ranked list of words.
#Also added this section at the bottom, courtesy of Steve H.

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