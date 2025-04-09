def main():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    def display():
        for i in range(0, len(board)):
            if i % 3 == 2:
                print(board[i])
            else:
                print(board[i], end="")

    display()

    # エラーを出すとターンが進んでしまう　# 9ターン引き分けパターン 401753628 #9で決着パターン #012345768
    # CPUと対戦

    def input_turn(player):
        if player == "o":
            input_value: int = input("oのターンです。0-8の数字を入力してください")
            while board[int(input_value)] in ("o", "x"):
                print("この操作は無効です。他の数字を入力してください。")
                input_value: int = input("oのターンです。0-8の数字を入力してください")
                del board[int(input_value)]
                board.insert(int(input_value), "o")
            else:
                del board[int(input_value)]
                board.insert(int(input_value), "o")
        else:
            input_value: int = input("xのターンです。0-8の数字を入力してください")
            while board[int(input_value)] in ("o", "x"):
                print("この操作は無効です。他の数字を入力してください。")
                input_value: int = input("oのターンです。0-8の数字を入力してください")
                del board[int(input_value)]
                board.insert(int(input_value), "x")
            else:
                del board[int(input_value)]
                board.insert(int(input_value), "x")

    # def input_turn(player):
    #     if player == "o":
    #         input_value: int = input("oのターンです。0-8の数字を入力してください")
    #         del board[int(input_value)]
    #         board.insert(int(input_value), "o")
    #     else:
    #         input_value: int = input("xのターンです。0-8の数字を入力してください")
    #         del board[int(input_value)]
    #         board.insert(int(input_value), "x")

    def judgement(player) -> bool:
        if player == "o":
            if (
                board[0] == board[1] == board[2] == "o"
                or board[3] == board[4] == board[5] == "o"
                or board[6] == board[7] == board[8] == "o"
                or board[0] == board[3] == board[6] == "o"
                or board[1] == board[4] == board[7] == "o"
                or board[2] == board[5] == board[8] == "o"
                or board[2] == board[4] == board[6] == "o"
                or board[0] == board[4] == board[8] == "o"
            ):
                print("player o Win!!")
                return True
            else:
                return False
        else:
            if (
                board[0] == board[1] == board[2] == "x"
                or board[3] == board[4] == board[5] == "x"
                or board[6] == board[7] == board[8] == "x"
                or board[0] == board[3] == board[6] == "x"
                or board[1] == board[4] == board[7] == "x"
                or board[2] == board[5] == board[8] == "x"
                or board[2] == board[4] == board[6] == "x"
                or board[0] == board[4] == board[8] == "x"
            ):
                print("player x Win!!")
                return True
            else:
                return False

    for turn in range(0, 9):
        if turn % 2 == 0:
            input_turn("o")
            display()
            judgement("o")
        else:
            input_turn("x")
            display()
            judgement("x")
        if judgement("o") is True or judgement("x") is True:
            print("ゲーム終了です。")
            break
    if judgement("o") is False:
        print("引き分けです。")


if __name__ == "__main__":
    main()
