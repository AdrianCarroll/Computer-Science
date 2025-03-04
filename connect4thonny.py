a="_"
row1=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
row2=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
row3=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
row4=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
row5=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
row6=["|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|", a, "|"]
print("Welcome to connect 4")
print("To win, make a vertical, horizontal or diagonal line using R or Y. R goes first: ")
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)
while a in row1:
    if a in row6:
        collum=input("Pick a number from 1 to 7: ")
        if collum==1:
            row6[1]="R"
        elif collum==2:
            row6[3]="R"
        elif collum==3:
            row6[5]="R"
        elif collum==4:
            row6[7]="R"
        elif collum==5:
            row6[9]="R"
        elif collum==6:
            row6[11]="R"
        else:
            row6[13]="R"
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)
    elif a in row5:
        collum=input("Pick a number from 1 to 7: ")
        if collum==1:
            row5[1]="R"
        elif collum==2:
            row5[3]="R"
        elif collum==3:
            row5[5]="R"
        elif collum==4:
            row5[7]="R"
        elif collum==5:
            row5[9]="R"
        elif collum==6:
            row5[11]="R"
        else:
            row5[13]=="R"
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)
