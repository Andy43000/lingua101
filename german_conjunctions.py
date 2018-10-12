
#top25germanadverbs

import random
while True: #initiate loop

        d = { 'und': 'and',
             'dass': 'that',
             'als': 'as, when',
             'oder': 'or',
             'aber': 'but',
             'wenn': 'if, when ',
             'weil': 'because',
             'denn': 'because',
             'sondern': 'but, rather',
             'ob': 'whether',
             'sowie': 'as well as',
             'beziehungsweise': 'or, respectively',
             'obwohl': 'although',
             'nachdem': 'after',
             'bevor': 'before',
              'sowohl...und...': 'both',
              'weder...und...': 'neither',
              'so dass': 'dass',
              'indem': 'while, by',
               'entweder...oder...': 'either or',
               'solange': 'as long as',
               'falls': 'in case, if',
               'sobald': 'as soon as',
               'zumal': 'particularly, especially'}
        question = random.choice(list(d.keys())) #get random key

        user = input(question) #pose question with key and get answer

        # print(question)

        #d.values

        answer = d.get(question) #use the key to get its corresponding value.

        print(answer)

        user_blank = user.strip() #remove blank spaces

        if user_blank == answer: #return verdict
                print('Correct!')

        #if user == 'exit':
        #        break
        else:
                print('incorrect!')

        if user_blank == 'exit':
                break
