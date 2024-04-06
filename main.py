
def Board():
    zero = 'X' if xstate[0] else 'O' if ostate[0] else 0
    one = 'X' if xstate[1] else 'O' if ostate[1] else 0
    two = 'X' if xstate[2] else 'O' if ostate[2] else 0
    three = 'X' if xstate[3] else 'O' if ostate[3] else 0
    four = 'X' if xstate[4] else 'O' if ostate[4] else 0
    five = 'X' if xstate[5] else 'O' if ostate[5] else 0
    six = 'X' if xstate[6] else 'O' if ostate[6] else 0
    seven = 'X' if xstate[7] else 'O' if ostate[7] else 0
    eight = 'X' if xstate[8] else 'O' if ostate[8] else 0
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for 'x' and 0 for 'o'
    print("Welcome to TIC TAC TOE !")
    while True:
        Board()
        if turn == 1:
            print("X's Chance")
            value = int(input("Please Enter a value to place 'X' "))
            xstate[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please Enter a value to place 'O' "))
            ostate[value] = 1
