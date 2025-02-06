string1='''
 +---+
 |   |
 O   |
/|\  |
/ \  |
'''
string2='''
 +---+
 |   |
 O   |
/|\  |
/    |
'''
string3='''
 +---+
 |   |
 O   |
/|\  |
     |
'''
string4='''
 +---+
 |   |
 O   |
/|   |
     |
'''
string5='''
 +---+
 |   |
 O   |
 |   |
     |
'''
string6='''
 +---+
 |   |
 O   |
     |
     |
'''
string7='''
 +---+
 |   |
     |
     |
     |
'''
again="yes"
while "yes" in again:
        secret="bat"
        print("Welcome to Hangman! you have 7 lives")
        lives=7
        x_tmp = secret
        listt=''
        go=input("Enter a letter/guess: ")
        go=go.lower()
        while go in listt:
            print("Letter already used")
            go=input("Enter a letter/guess: ")
            go=go.lower()
        listt=listt+go
        attempt= "_"*len(secret)
        index = secret.find(go)
        start = 0
        '''print("Welcome back to Hangman! you have 7 lives")'''
        while "_" in attempt:
            if go in secret:
                listt=listt+go
                oldIndex = 0
                start = 0
                numletter=secret.count(go)
                if numletter==1:
                    indexPos = secret.find(go)
                    attempt = attempt[0:indexPos]+go+attempt[indexPos+1:]
                    print(attempt)
    #        else:
    #            attempt = attempt[start:index+oldIndex]+go+attempt[index+1+oldIndex:]
    #            oldIndex = oldIndex +index+1
    #            x_tmp = x_tmp[index+1:]
    #            index = x_tmp.find(go)
            else:
                print("Wrong guess!")
                lives=lives-1
                if lives==6:
                   print(string7)
                elif lives==5:
                   print(string6)
                elif lives==4:
                   print(string5)
                elif lives==3:
                   print(string4)
                elif lives==2:
                   print(string3)
                elif lives==1:
                   print(string2)
                else lives==0:
                   print(string1)
                   print("Game over")
            if attempt==secret:
                print("Win!")
                break
            go=input("Enter a letter/guess: ")
            go=go.lower()
        again=input("Would you like to play again?")