secret="bat"
print("Welcome to Hangman! you have 7 lives")
lives=7
x_tmp = secret
go=input("Enter a letter/guess (must be lowercase): ")
attempt= "_"*len(secret)
index = secret.find(go)
start = 0
listt=''
while "_" in attempt:
    if go in secret:
        listt=listt+go
        print(listt)
        oldIndex = 0
        start = 0
        numletter=secret.count(go)
        if numletter==1:
            indexPos = secret.find(go)
            attempt = attempt[0:indexPos]+go+attempt[indexPos+1:]
            print(attempt)
#         else:
#             attempt = attempt[start:index+oldIndex]+go+attempt[index+1+oldIndex:]
#             oldIndex = oldIndex +index+1
#             x_tmp = x_tmp[index+1:]
#             index = x_tmp.find(go)
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
        