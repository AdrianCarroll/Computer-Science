a=[]
grid1=[a,'|',a,'|',a]
grid2=[a,'|',a,'|',a]
grid3=[a,'|',a,'|',a]
print("Welcome to X's and O's")
print("To win, create a line with X's or O's. The X player always goes first")
print(grid1)
print(grid2)
print(grid3)
for a in grid1 and grid2 or grid3:
    row=int(input("Enter a number from 1 to 3: "))
    collum=int(input("Enter a 0, 2 or 4: "))
    if row==1:
        if collum==0:
            grid1[0]='X'
        elif collum==2:
            grid1[2]='X'
        else:
            grid1[4]='X'
    elif row==2:
        if collum==0:
            grid2[0]='X'
        elif collum==2:
            grid2[2]='X'
        else:
            grid2[4]='X'
    else:
        if collum==0:
            grid3[0]='X'
        elif collum==2:
            grid3[2]='X'
        else:
            grid3[4]='X'
    print(grid1)
    print(grid2)
    print(grid3)