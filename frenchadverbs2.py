
#amcg2014

import random
while True: #initiate loop


        d = {'absolument':'absolutely','actuellement':'currently','ailleurs':'elsewhere','alors':'so','ainsi':'thus; so','apres':'after','assez':'quite, fairly','aujourd hui':'today','aussi':'s well','aussitot':'immediately','autant':'much',
              'autrefois':'in the old day','test':'test'}
         #set dictionary
        question = random.choice(d.keys()) #get random key

        user = raw_input(question, ) #pose question with key and get answer

        print question

        #d.values

        answer = d.get(question) #use the key to get its corresponding value.

        print answer

        if user == answer: #return verdict
                print 'Correct!'

        #if user == 'exit':
        #        break
        else:
                print 'incorrect!'

        if user == 'exit':
                break
