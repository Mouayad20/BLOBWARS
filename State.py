from typing import List
from Board import Board
import copy


class State:
    def __init__(self, m, n):

        self.Board = Board(m, n)
        self.parent: State = None

    def can_move(self, isource, jsource, idest, jdest, RorB):
        cORp = "no"
        if self.Board.gameboard[isource][jsource].celltype != RorB:
            return cORp
        if self.Board.gameboard[idest][jdest].celltype == "-" and (isource != idest or jsource != jdest):
            copy = self.Board.gameboard[isource][jsource].cell_can_copy_to_it(self.Board.m, self.Board.n)
            jump = self.Board.gameboard[isource][jsource].cell_can_jump_to_it(self.Board.m, self.Board.n)
            # print (copy)
            # print(jump)
            if (idest, jdest) in copy:
                cORp = "c"
            elif (idest, jdest) in jump:
                cORp = "j"

            return cORp
        else:
            return cORp

    def deepcopyy(self):
        Board2 = copy.deepcopy(self.Board)
        y = State(self.Board.m, self.Board.n)
        y.Board = Board2
        return y

    def copymove(self, isource, jsource, idest, jdest, RorB):
        self.Board.gameboard[idest][jdest].celltype = RorB

        small_range = self.Board.gameboard[idest][jdest].cell_can_copy_to_it(self.Board.m, self.Board.n)

        for k in range(len(small_range)):
            i = small_range[k][0]
            j = small_range[k][1]
            if self.Board.gameboard[i][j].celltype != "-":
                self.Board.gameboard[i][j].celltype = RorB

        return self

    def jumpmove(self, isource, jsource, idest, jdest, RorB):
        self.Board.gameboard[isource][jsource].celltype = "-"
        self.Board.gameboard[idest][jdest].celltype = RorB

        small_range = self.Board.gameboard[idest][jdest].cell_can_copy_to_it(self.Board.m, self.Board.n)

        for k in range(len(small_range)):
            i = small_range[k][0]
            j = small_range[k][1]
            if self.Board.gameboard[i][j].celltype != "-":
                self.Board.gameboard[i][j].celltype = RorB

        return self

    def next_state(self, RorB):
        nextstate: List[State] = []
        position = self.Board.positonsymbol(RorB)
        for o in range(len(position)):
            isource = position[o][0]
            jsource = position[o][1]

            small_range = self.Board.gameboard[isource][jsource].cell_can_copy_to_it(self.Board.m, self.Board.n)
            big_range=self.Board.gameboard[isource][jsource].cell_can_jump_to_it(self.Board.m, self.Board.n)
            for k in range(len(small_range)):
                i = small_range[k][0]
                j = small_range[k][1]
                if self.can_move(isource, jsource, i, j, RorB) == "c":
                    nextstate.append(self.deepcopyy().copymove(isource, jsource, i, j, RorB))
            for k in range(len(big_range)):
                i = big_range[k][0]
                j = big_range[k][1]

                if self.can_move(isource, jsource, i, j, RorB) == "j":
                    nextstate.append(self.deepcopyy().jumpmove(isource, jsource, i, j, RorB))




            # for i in range(self.Board.m):0

            #     for j in range(self.Board.n):
            #
            #         if self.can_move(isource, jsource, i, j, RorB) == "c":
            #             nextstate.append(self.deepcopyy().copymove(isource, jsource, i, j, RorB))
            #         if self.can_move(isource, jsource, i, j, RorB) == "j":
            #             nextstate.append(self.deepcopyy().jumpmove(isource, jsource, i, j, RorB))
            for i in range(len(nextstate)):
                nextstate[i].parent = self

        return nextstate

    def EF(self, RorB):
        countB = 0
        countR = 0
        countE = 0

        for i in range(self.Board.m):
            for j in range(self.Board.n):
                if self.Board.gameboard[i][j].celltype == "B":
                    countB = countB + 1
                elif self.Board.gameboard[i][j].celltype == "R":
                    countR = countR + 1
                else:
                    countE = countE + 1

        if RorB == "R":
            return countR - countB
        elif RorB == "B":
            return countB - countR
