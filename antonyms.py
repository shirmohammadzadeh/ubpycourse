antonyms = dict()
while 1:
    a=input('Enter the word\n')
    if  a in antonyms.keys():
        print (antonyms[a])
    else:
        
        print ('I dont know the antonum',a)
        b=input('\nDo you know? y/n')
        if b == 'y' :
            c=input('\nWhat is it?')
            antonyms[a]=c
            antonyms [c]=a  
        else:
            print('ok!')
