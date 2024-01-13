from Cell import Cell


class Board:

    def __init__(self,m,n) -> object:
        self.m = m
        self.n = n
        self.gameboard = []
        for i in range(m):
            self.list = [Cell(i, j) for j in range(n)]
            self.gameboard.append(self.list)

    def prRed(self,skk):
        print("\033[91m {}\033[00m".format(skk),end="")

    def prCyan(self,skk):
        print("\033[96m {}\033[00m".format(skk),end="")

    def print_board(self):
        print('                  ',end='')
        for j in range(self.n):
            print(j,'  ',end="")
        print("")
        x=0
        for i in self.gameboard:
            print("             ",end="")
            print(x,' |', end='')
            for j in i:
                if j.celltype == "B":
                    print('',end="")
                    self.prCyan("B")
                    print(' |', end="")
                if j.celltype == "R":
                    print('',end="")
                    self.prRed("R")
                    print(' |', end="")
                if j.celltype == "-":
                    print(' ', end="")
                    print("-",end="")
                    print(' |', end="")
            x = x + 1
            print(' ')

        print('-------------------------------------------------------------------------------------------------------------------------------')

    def positonsymbol(self,RorB):
        position=[]
        for i in range(self.m):
            for j in range(self.n):
                if self.gameboard[i][j].celltype==RorB:
                    position.append((i,j))
        return  position

    def goal(self):
        countB=0
        countR=0
        countE=0
        iswin=False
        whowin=None
        for i in range(self.m):
            for j in range(self.n):
                if self.gameboard[i][j].celltype == "B":
                    countB = countB + 1
                elif self.gameboard[i][j].celltype == "R":
                    countR = countR + 1
                else:
                    countE = countE + 1
        if countB > countR:
            whowin = "B"
        elif countR > countB:
            whowin = "R"

        if countE == 0 or countR==0 or countB==0:
            iswin=True


        return iswin,whowin,countB,countR
