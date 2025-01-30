again="yes"
while "yes" in again:
        secret="bat"
        print("Welcome to Hangman! you have 7 lives")
        lives=7
        x_tmp = secret
        listt=''
        go=input("Enter a letter/guess (must be lowercase): ")
        while go in listt:
            print("Letter already used")
            go=input("Enter a letter/guess (must be lowercase): ")
        listt=listt+go
        attempt= "_"*len(secret)
        index = secret.find(go)
        start = 0
        print("Welcome back to Hangman! you have 7 lives")
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
                if lives<=0:
                   print("Out of lives! Game over")
                   break
            if attempt==secret:
                print("Win!")
                break
            go=input("Enter a letter/guess (must be lowercase): ")
        again=input("Would you like to play again?")