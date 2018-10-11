
#amcg2014

import random
while True: #initiate loop


        d = {'absolument':'absolutely','actuellement':'currently','ailleurs':'elsewhere','alors':'so','ainsi':'thus; so','apres':'after','assez':'quite, fairly','aujourd hui':'today','aussi':'s well','aussitot':'immediately','autant':'much','autrefois':'in the old day',
             'autrement':'differently','autour':'around','avant':'before','avant-hier':'on the day before yesterday','avec':'with','beaucoup':'a lot','bas':'low','bien':'well','bientot':'soon','brusquement':'abruptly','cependant':'nonetheless','certes':'admittedly',
             'certainement':'certainly','ci':'here','combien':'how much/many','comme':'as','comment':'how','completement':'completely','dabord':'first','davantage':'more','debout':'standing','dehors':'outside','deja':'already','dela':'beyond',
             'demain':'tomorrow','depuis':'since','dernierement':'lately','desormais':'from now on, henceforth','dessus':'on top of','devant':'in front of','doucement':'softly','egalement':'as well/equally','encore':'again/still','enfin':'finally; eventually','ensemble':'together','ensuite':'nextthen','enormement': 'enormously','environ':'about','facilement':'easily','franchement':'frankly','gentiment':'kindly','guere':'hardly','haut':'high','heureusement':'fortunately','hier':'yesterday','ici':'here','immediatement':'immediately','jamais':'never','la':'there','la-bas':'over there','la-dedans':'in here, in there','la-dessus':'on here; on there','largement':'greatly; well','legerement':'lightly; slightly','lentement':'slowly','loin':'far','longtemps':'for a long time','lors':'when','lors de':'during','maintenant':'now','mal':'poorly; badly','meme':'even','moins':'less','mieux':'better','naturellement':'naturally','ne':'not','non':'no; not','oui':'yes','parfois':'sometimes','partout':'everywhere','pas':'not','parfaitement':'perfectly','peu':'few, little','peut-etre':'perhaps','plutt':'rather','plus':'more, ___-er','point':'hardly any; almost no','pourquoi':'why','pourtant':'yet','precedemment':'previously','precisement':'precisely','premierement':'firstly','pres':'near','presque':'nearly','profondement':'profoundly','puis':'then','quelque':'some','quelque part':'somewhere','rapidement':'rapidly','rarement':'rarely','seulement':'only','serieusement':'seriously','simplement':'simply','si':'as/so','soudain':'suddenly','souvent':'often','surtout':'especially','tant':'so much','tantot':'sometimes','tard':'late','tellement':'so (much)','tot':'early','toujours':'always','tout':'all','tres':'very','trop':'too much','vite':'quickly','vraiment':'really'}
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
