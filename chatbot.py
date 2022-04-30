import re
import tkinter as tk

# how are you

def get_probability(message_in, recognised_words, single_response = False, required_words = []):

    probability = 0
    has_required_words = True

    for word in message_in:
        if word in recognised_words:
            probability += 1
    
    probability_percent = int((probability / len(recognised_words)) * 100)

    for word in required_words:
        if word not in message_in:
            has_required_words = False
            break
    
    if has_required_words == True or single_response == True:
        return int(probability_percent)
    
    else:
        return 0

def highest_probability(message_in:str):
    probability_list = {}

    def response(bot_response, recognised_words, single_response = False, required_words = []):
        nonlocal probability_list
        probability_list[bot_response] = get_probability(message_in,recognised_words, single_response, required_words)
    
    # {'HEllo' : 33, 'BYE' : 0}

    # Responses
    response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    response('I am doing fine! And you?', ['how','are','you','doing','fine'], required_words = ['how','you'])
    response('That is great to hear!', ['i','am','doing','fine'], required_words=['i','am','fine'])
    response('I am a chatbot written in Python!', ['tell', 'me', 'about', 'yourself'], required_words=['about', 'yourself'])
    response('I love eating electricity!', ['what','do', 'you', 'eat'], required_words=['what', 'you', 'eat'])

    best_match = max(probability_list, key = probability_list.get)
    
    unkown = 'I dont understand'

    if probability_list[best_match] < 1:
        return unkown
    return best_match
    
def get_response(message_in:str):
    split_message = re.split(r'\s+|[,;?;!.-]\s*', message_in.lower())
    return highest_probability(split_message)