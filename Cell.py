from typing import List


class Cell:


    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.celltype="-"

    def cell_can_copy_to_it(self,m,n):
        carray=[]
        if 0 <= self.i-1 < m and 0 <= self.j < n :#up
            carray.append((self.i-1,self.j))
        if 0 <= self.i+1 < m and 0 <= self.j < n :#down
            carray.append((self.i+1,self.j))
        if 0 <= self.i < m and 0 <= self.j+1 < n :#right
            carray.append((self.i,self.j+1))
        if 0 <= self.i < m and 0 <= self.j-1 < n :#left
            carray.append((self.i,self.j-1))
        if 0 <= self.i-1 < m and 0 <= self.j-1 < n :#ul
            carray.append((self.i-1,self.j-1))
        if 0 <= self.i+1 < m and 0 <= self.j-1 < n :#dl
            carray.append((self.i+1,self.j-1))
        if 0 <= self.i-1 < m and 0 <= self.j+1 < n :#ur
            carray.append((self.i-1,self.j+1))
        if 0 <= self.i+1 < m and 0 <= self.j+1 < n :#dr
            carray.append((self.i+1,self.j+1))

        return carray

    def cell_can_jump_to_it(self,m,n):
        jarray: List[tuple] = []
        if 0 <= self.i - 2 < m and 0 <= self.j - 2 < n :  # a
            jarray.append((self.i - 2, self.j - 2))
        if 0 <= self.i - 2 < m and 0 <= self.j - 1 < n :  # b
            jarray.append((self.i - 2, self.j - 1))
        if 0 <= self.i - 2 < m and 0 <= self.j < n :  # c
            jarray.append((self.i - 2, self.j))
        if 0 <= self.i - 2 < m and 0 <= self.j + 1 < n :  # d
            jarray.append((self.i - 2, self.j + 1))
        if 0 <= self.i - 2 < m and 0 <= self.j + 2 < n :  # e
            jarray.append((self.i - 2, self.j + 2))

        if 0 <= self.i - 1 < m and 0 <= self.j - 2 < n :  # f
            jarray.append((self.i - 1, self.j - 2))
        if 0 <= self.i - 1 < m and 0 <= self.j + 2 < n :  # g
            jarray.append((self.i - 1, self.j + 2))
        if 0 <= self.i < m and 0 <= self.j - 2 < n :  # h
            jarray.append((self.i, self.j - 2))
        if 0 <= self.i < m and 0 <= self.j + 2 < n :  # i
            jarray.append((self.i, self.j + 2))
        if 0 <= self.i + 1 < m and 0 <= self.j - 2 < n :  # j
            jarray.append((self.i + 1, self.j - 2))
        if 0 <= self.i + 1 < m and 0 <= self.j + 2 < n :  # k
            jarray.append((self.i + 1, self.j + 2))

        if 0 <= self.i + 2 < m and 0 <= self.j - 2 < n :  # l
            jarray.append((self.i + 2, self.j - 2))
        if 0 <= self.i + 2 < m and 0 <= self.j - 1 < n :  # m
            jarray.append((self.i + 2, self.j - 1))
        if 0 <= self.i + 2 < m and 0 <= self.j < n :  # n
            jarray.append((self.i + 2, self.j))
        if 0 <= self.i + 2 < m and 0 <= self.j + 1 < n:  # o
            jarray.append((self.i + 2, self.j + 1))
        if 0 <= self.i + 2 < m and 0 <= self.j + 2 < n :  # p
            jarray.append((self.i + 2, self.j + 2))

        return jarray




