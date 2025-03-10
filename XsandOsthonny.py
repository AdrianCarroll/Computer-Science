a="_"
while True:
    grid1 = [a, '|', a, '|', a]
    grid2 = [a, '|', a, '|', a]
    grid3 = [a, '|', a, '|', a]
    print("Welcome to X's and O's")
    print("To win, create a line with X's or O's. The X player always goes first")
    print(grid1)
    print(grid2)
    print(grid3)
    player=1
    def check_winner():
        if grid1[0] == grid1[2] == grid1[4] != a or \
           grid2[0] == grid2[2] == grid2[4] != a or \
           grid3[0] == grid3[2] == grid3[4] != a:
            return True
        if grid1[0] == grid2[0] == grid3[0] != a or \
           grid1[2] == grid2[2] == grid3[2] != a or \
           grid1[4] == grid2[4] == grid3[4] != a:
            return True
        if grid1[0] == grid2[2] == grid3[4] != a or \
           grid1[4] == grid2[2] == grid3[0] != a:
            return True
        return False
    while a in grid1 or grid2 or grid3:
        if a in grid1 or grid2 or grid3:
            if player==1:
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
                if check_winner():
                    print("Player X wins!")
                    break
                player=2
            else:
                row=int(input("Enter a number from 1 to 3: "))
                collum=int(input("Enter a 0, 2 or 4: "))
                if row==1:
                    if collum==0:
                        grid1[0]='O'
                    elif collum==2:
                        grid1[2]='O'
                    else:
                        grid1[4]='O'
                elif row==2:
                    if collum==0:
                        grid2[0]='O'
                    elif collum==2:
                        grid2[2]='O'
                    else:
                        grid2[4]='O'
                else:
                    if collum==0:
                        grid3[0]='O'
                    elif collum==2:
                        grid3[2]='O'
                    else:
                        grid3[4]='O'
                print(grid1)
                print(grid2)
                print(grid3)
                if check_winner():
                    print("Player O wins!")
                    break
                player=1
    else:
        print("It's a draw!")

    again = input("Game over, would you like to play again? Y/N: ").upper()
    if again != "Y":
        print("Thanks for playing!")
        break
