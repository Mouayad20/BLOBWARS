from State import State
import time
def userplayer(s):
    isource = int(input("enter i  ball"))
    jsource = int(input("enter j  ball"))
    idist = int(input("enter i  dist"))
    jdist = int(input("enter j  dist"))
    canMoveAble = s.can_move(isource, jsource, idist, jdist, "B")
    while canMoveAble == "no":
        isource = int(input("renter i  ball"))
        jsource = int(input("renter j  ball"))
        idist = int(input("renter i  dist"))
        jdist = int(input("renter j  dist"))
        canMoveAble = s.can_move(isource, jsource, idist, jdist, "B")
    if canMoveAble == "c":
        s.copymove(isource, jsource, idist, jdist, "B")
    elif canMoveAble == "j":
        s.jumpmove(isource, jsource, idist, jdist, "B")
    s.Board.print_board()

def creat_game():
    m = int(input("enter m board"))
    n = int(input("enter n board"))
    s = State(m, n)
    s.Board.gameboard[0][0].celltype = "B"
    s.Board.gameboard[0][n - 1].celltype = "B"
    s.Board.gameboard[m - 1][n - 1].celltype = "R"
    s.Board.gameboard[m - 1][0].celltype = "R"
    s.Board.print_board()
    return s

def min_max(state, depth, maxplayer):
    iswin, whowin, countB, countR = state.Board.goal()
    if depth == 0 or iswin == True:
        EF = state.EF("R")
        return state, EF
    out_child = None
    next_state = state.next_state("R")
    if maxplayer:
        out_ef = int("-1000000")
        for child in next_state:
            cur_child, cur_ef = min_max(child, depth - 1, not maxplayer)
            print("still run")
            if out_ef < cur_ef:
                out_ef = cur_ef
                out_child = child

    else:
        out_ef = int("1000000")
        for child in next_state:
            cur_child, cur_ef = min_max(child, depth - 1, not maxplayer)
            if out_ef > cur_ef:
                out_ef = cur_ef
                out_child = child

    return out_child, out_ef

def alpha_beta(state, depth, maxplayer, alpha=-1000000, beta=1000000):

        iswin,whowin,countB,countR=state.Board.goal()
        if depth == 0 or iswin==True:
            EF = state.EF("R")
            return state, EF
        out_child = None
        next_state = state.next_state("R")


        if maxplayer:
            out_ef = int("-1000000")
            for child in next_state:
                cur_child, cur_ef = alpha_beta(child, depth - 1, not maxplayer, alpha, beta)
                if out_ef < cur_ef:
                    out_ef = cur_ef
                    out_child = child
                alpha = max(alpha, cur_ef)
                if beta <= alpha:
                    break
        else:
            out_ef = int("1000000")
            for child in next_state:
                cur_child, cur_ef = alpha_beta(child, depth - 1, not maxplayer, alpha, beta)
                if out_ef > cur_ef:
                    out_ef = cur_ef
                    out_child = child
                beta = min(beta, cur_ef)
                if beta <= alpha:
                    break


        return out_child, out_ef
def gameWithComputer():
    print("enter 1 to  easy level MinMax")
    print("enter 2 to  difficult level MinMax")
    print("enter 3 to  easy level alphaBeta")
    print("enter 4 to  difficult level alphaBeta")

    x=int(input())
    while x !=1 and x !=2 and x!=3 and x!=4:
        x = int(input("wrong input please press 1 to easy level press 2 to deffecult "))

    if x==1:
        s=creat_game()
        iswin, whowin, countB, countR=s.Board.goal()
        print("BLUE SCORE",countB)
        print("RED SCORE",countR)
        while iswin!=True:
            userplayer(s)
            start = time.time()
            out_child, out_ef=min_max(s, 3, True)
            print(time.time() - start)
            s=out_child
            s.Board.print_board()
            iswin, whowin, countB, countR = s.Board.goal()
            print("BLUE SCORE", countB)
            print("RED SCORE", countR)

        print("-------------------win-------------------------")
        print("the winner:",whowin)
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
    elif x==2:
        s = creat_game()
        iswin, whowin, countB, countR = s.Board.goal()
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
        while iswin != True:
            userplayer(s)
            start = time.time()
            out_child, out_ef = min_max(s, 5, True)
            print(time.time() - start)
            s = out_child
            s.Board.print_board()
            iswin, whowin, countB, countR = s.Board.goal()
            print("BLUE SCORE", countB)
            print("RED SCORE", countR)

        print("-------------------win-------------------------")
        print("the winner:", whowin)
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
    elif x == 3:
        s = creat_game()
        iswin, whowin, countB, countR = s.Board.goal()
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
        while iswin != True:
            userplayer(s)
            start = time.time()
            out_child, out_ef = alpha_beta(s, 3, True)
            print(time.time() - start)
            s = out_child
            s.Board.print_board()
            iswin, whowin, countB, countR = s.Board.goal()
            print("BLUE SCORE", countB)
            print("RED SCORE", countR)

        print("-------------------win-------------------------")
        print("the winner:", whowin)
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
    elif x == 4:
        s = creat_game()
        iswin, whowin, countB, countR = s.Board.goal()
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)
        while iswin != True:
            userplayer(s)
            start = time.time()
            out_child, out_ef = alpha_beta(s, 5, True)
            print(time.time() - start)
            s = out_child
            s.Board.print_board()
            iswin, whowin, countB, countR = s.Board.goal()
            print("BLUE SCORE", countB)
            print("RED SCORE", countR)

        print("-------------------win-------------------------")
        print("the winner:", whowin)
        print("BLUE SCORE", countB)
        print("RED SCORE", countR)