secret="apple"
print("Welcome to Hangman! you have 7 lives")
lives=7
attempt= "_____"
while "_" in attempt:
    go=input("Enter a letter/guess (must be lowercase): ")
    if go=="apple":
        print("Win!")
        break
    elif go in secret:
        numletter=secret.count(go)
        if numletter==1:
            indexPos = secret.find(go)
            attempt = attempt[0:indexPos]+go+attempt[indexPos+1:]
            print(attempt)
        else:
            indexPos = secret.find(go)
            attempt = attempt[0:indexPos]+go+go+attempt[indexPos+1:]
            print(attempt)
    else:
        print("Wrong guess!")
        lives=lives-1
        if lives<=0:
            print("Out of lives! Game over")
            break