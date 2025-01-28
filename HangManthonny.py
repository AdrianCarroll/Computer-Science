secret="banana"
print("Welcome to Hangman! you have 7 lives")
lives=7
attempt= "_____"
while "_" in attempt:
    go=input("Enter a letter/guess (must be lowercase): ")
    if go=="banana":
        print("Win!")
        break
    elif go in secret:
        numletter=secret.count(go)
        if numletter==1:
            indexPos = secret.find(go)
            attempt = attempt[0:indexPos]+go+attempt[indexPos+1:]
            print(attempt)
        else:
            oldindex=0
            start=0
            for i in range (numletter):
                indexPos = secret[start:].find(go)
                print (indexPos)
                attempt = attempt[0:indexPos+start]+go+attempt[indexPos+oldindex+2:]
                print (attempt)
                oldindex=indexPos
                start=indexPos+1
            print(attempt)
    else:
        print("Wrong guess!")
        lives=lives-1
        if lives<=0:
            print("Out of lives! Game over")
            break