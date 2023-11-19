import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('First I was an idea,then a Bunch of googlers in California started  a lot of experiments,nd thats Where I came from', ['where are u from'], single_response=True)
    response('Iam your virtual friend', ['who is this'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('Iam your virtual friend', ['who is this'],  required_words=['who'])
    response('I\'m doing fine, and you?', ['how are u'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('coimbatore', ['which is the manchester of Tamilnadu'], single_response=True)
    response('mumbai', ['manchester of india'], required_words=['how'])
    response('Tennis is a popular racquet sport played between two individuals (singles) or two teams of two players each (doubles). The primary objective is to hit a ball over a net and into the opponent court in such a way that the opponent cannot return it. The game is played on a rectangular court with a net in the middle.', ['tell about tennis'], required_words=['tell'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_TENNIS, ['tell', 'about', 'tennis'], required_words=['about', 'tennis'])
    response(long.R_CRICKET, ['tell', 'about', 'cricket'], required_words=['about', 'cricket'])
    response(long.R_ORIGIN, ['where', 'are','u','from'], required_words=['where', 'are','u','from'])
    response(long.R_FRIEND, ['who', 'are','u'], required_words=['who', 'are','u'])
    response(long.R_WEATHER, ['weather','today'], required_words=['weather','today'])
    response(long.R_BOOKS, ['suggest','any','good','books','to','read'], required_words=['books','to','read'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
