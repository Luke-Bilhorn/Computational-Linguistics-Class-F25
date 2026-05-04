'''
Created on May 30, 2023

Structure and other ideas taken from https://github.com/wadetb/eliza

@author: tvandrun
'''

import re
import random


# Make a function that will perform a regex replacement.
# Given two regular expressions, make a function that will
# take a string and test whether it has a match for the first
# regex, and, if so, will replace it using the other regex.
def replacement(reSearch, reReplace) :
    return lambda str : re.sub(reSearch, reReplace, str) if re.search(reSearch, str) else None
#    return test_replace(lambda str: re.search(reSearch, str),
#                       lambda str: re.sub(reSearch, reReplace, str))

# Like pattern_response, but for the case where there are
# several substitutions to be made
def pattern_response(reSearch, response_orig) :
    def ff(str):
        match = re.search(reSearch, str)
        if match :
            replacements = match.groupdict()
            response = response_orig
            for x in replacements :
                response = re.sub(x, replacements[x], response)
            return response
        else :
            return None
    return ff

last_resort = ["I'm not sure I understand you.", 
               "Go on.", 
               "Perhaps we should change the subject.",
               "What does that suggest to you?", 
               "Are you sure?"]

basicSubList = [(r'\b(I|i) was\b', "you were"), (r"\b(I|i) wasn't\b", "you weren't"), (r'\byou are\b', 'I am'), 
                (r'\b(Y|y)ou are not\b', r'I am not'), (r"\b(Y|y)ou aren't\b", 'I am not'), (r'\bme\b', "you"), 
                (r'\bmy\b', "your"), (r'\bmine\b', "yours"), ("(i|I)\'m", "you are"), (r'\b(i|I)\b', "you"), (r'\bam\b', "are"), 
                (r'\byou\b', "me"), (r'\byours\b', "mine"), (r'\b(Y|y)our\b', "my"), (r'\bare\b', "to be"), 
                (r'\bcan\'t\b', "can not"), (r'\W$', "")]                       
                       
basicSubs = [replacement(basicSubList[i][0], "X%sX" % i) for i in range(len(basicSubList))] + [replacement("X%sX" % i, basicSubList[i][1]) for i in range(len(basicSubList))]


rule_regexes = [(r'you are sorry', 'You have nothing to apologize for.'),
                (r'you (dreamed|dreamt) that (?P<xxx>.*$)', 'Had you ever dreamt that xxx before?'),
                (r'[pP]ython', 'Do you mean the snake, the language, or the Monty?'),
                (r'dream', 'Tell me more about your dreams.'),
                (r'\b(egg(s?)|pancake(s?)|waffle(s?)|cereal|bacon|toast)\b', 'Do you usually have a good breakfast?'),
                ('(dream|sleep)', "It's important to get a good night of rest."),
                (r'your (?P<xxx>father|dad|mother|mom|brother|sister|friend|roommate|chapel buddy)', r'Do you get along with your xxx?'),
                (r'your (?P<xxx>father|dad|mother|mom|brother|sister)', r'Tell me about your family'),
                (r'your (father|dad|mother|mom|brother|sister|dog) (?P<xxx>[^.,!?]+)', r'Who else in your family xxx?'),
                (r'(every|always)', 'Can you think of a specific example?'),
                (r'(alike|like|similar|same)', 'What resemblance do you see?'),
                (r'me to be (a|an) (bot|agent|computer)', 'Does it bother you that you are talking to a chatbot?'),
                (r'you are (?P<xxx>depressed|sad|hungry|tired|angry|unhappy)', r'I am sorry to hear you are xxx'),
                (r'you are (?P<xxx>depressed|sad|hungry|tired|angry|unhappy)', r'Do you think that talking to me will help you not to be xxx?'),
                (r'you are (?P<xxx>tired|exhausted|worn out)', r'What is making you so xxx?'),
                (r'you need (?P<xxx>[^.,!?]+)', 'What would it mean to you if you got xxx?'),
                (r'I am not (?P<xxx>\w+)', 'Would you be more comfortable if I were xxx?'),
                (r'I am (?P<xxx>[^.,!?]+)', 'What makes you think I am xxx?'),
                (r'^(N|n)(O|o)(\.|!)*$', 'Why not?'), 
                (r'(W|w)hy\b.\?', "Because, I said so.")]
#(?P<xxx>[^.!]*)
rules = [pattern_response(p, q) for (p, q) in rule_regexes]



print("Please chat with me.")

while True :
    given = input()
    if not given:
        print("Please talk to me")
        continue
    # Make some modifications to the input
    given = given[0].lower() + given[1:]
    #words = re.split(r'[ ,\.;:()\-"!]', given)
    for sub in basicSubs :
        revised = sub(given)
        if revised :
            given = revised
    
    
    
    response = None
    
    random.shuffle(rules)
    for rule in rules :
        if not response :
            response = rule(given)
    
    if not response:
        response = random.choice(last_resort)
    
    print(response)