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
            