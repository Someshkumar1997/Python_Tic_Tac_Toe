
def Board():
    print(f" 0 | 1 | 2 ")
    print(f"---|---|---")
    print(f" 3 | 4 | 5 ")
    print(f"---|---|---")
    print(f" 6 | 7 | 8 ")


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for 'x' and 0 for 'o'
    print("Welcome to TIC TAC TOE !")
    while True:
        if turn == 1:
            print("X's Chance")
            value = input("Please Enter a value to place 'X'")
            xstate[value] = 1
        else:
            print("O's Chance")
            value = input("Please Enter a value to place 'O'")
            ostate[value] = 1
        Board()
        break
