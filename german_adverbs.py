
#top25germanadverbs

import random
while True: #initiate loop

        d = { 'eben ':'just now',
                'erst ':'first',
                'natürlich ': 'naturally',
                'vielleicht ':'perhaps',
                'dort ':	'there',
                'auch ':'also',
                'so ':'so',
                'dann ':'then',
                'da ':'there',
                'noch ':	'still, yet',
                'also ':'so',
                'nur '	:'only',
                'schon ':'already',
                'mehr ':'more',
                'jetzt '	:'now',
                'immer '	:'always',
                'sehr ':'very',
                'hier '	:'here',
                'doch '	:'but, still',
                'wieder ':'again',
                'eigentlich ': 'actually',
                'oben ': 'above',
                'nun,nu ':	'now',
                'heute '	: 'today',
                'weit '	: 'widely, far'}
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
