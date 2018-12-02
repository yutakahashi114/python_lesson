import random

def hangman(word):
    wrong = 0
    stages = [
        "",
        "_______     ",
        "|     |     ",
        "|     |     ",
        "|     O     ",
        "|    /|\    ",
        "|    / \    ",
        "|           "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        message = "1文字を予想してね："
        char = input(message)
        if char in rletters:
            index = rletters.index(char)
            board[index] = char
            rletters[index] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "_" not in board:
            print("You Win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("You Lose")
        print("正解は{0}".format(word))

if __name__ == "__main__":
    # word = input("Enter one word : ")
    answer_list = [
        "cat",
        "dog",
        "hang",
        "man",
        "python"
    ]
    rand = random.randint(0, len(answer_list))
    word = answer_list[rand]
    hangman(word)
