class Cellclass:
    """each number in the sudoku include cell contains value and probability list"""

    def __init__(self):
        self.value = 0
        self.prob = [False] * 9

    def setvalue(self, value):
        self.value = value

    def setprob(self, position):
        self.prob[position] = True

    def getvalue(self):
        return self.value

    def getprob(self, position):
        return self.prob[position]


class AndokuClass:
    andukulist = []
    # position index of sudoku board
    position = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49, 50, 51, 52, 53],
        [54, 55, 56, 57, 58, 59, 60, 61, 62],
        [63, 64, 65, 66, 67, 68, 69, 70, 71],
        [72, 73, 74, 75, 76, 77, 78, 79, 80],
    ]

    """initial value"""

    def __init__(self, listsudoku):
        for _ in range(81):
            self.andukulist.append(Cellclass())
        for item in range(len(listsudoku)):
            self.andukulist[item].value = listsudoku[item]

    def getsudoku(self):
        listsudoku = [0] * 81
        for item in range(len(listsudoku)):
            listsudoku[item] = self.andukulist[item].getvalue()
        return listsudoku

    """take index and call number of true probabilities"""

    def truecount(self, index):
        count = 0
        for n in range(9):
            if self.andukulist[index].prob[n]:
                count += 1
        return count

    """return index of true prob in cell for example
    is cell can be 2 or 7 it will return [1, 6]"""

    def peektrue(self, index):
        blocks = []
        for i in range(9):
            if self.andukulist[index].prob[i]:
                blocks.append(i)
        return blocks

    """return the row indexs for any cell"""

    def rowlist(self, index):
        blocks = []
        i = index // 9
        for j in range(0, 9):
            blocks.append(self.position[i][j])
        return blocks

    def rowlistnotsolved(self, index):
        blocks = self.rowlist(index)
        for block in blocks:
            if self.andukulist[block].value != 0:
                blocks.remove(block)
        return blocks

    """return true if the row has the value equal to the checkvalue"""

    def isfoundrow(self, index, checkedvalue):
        listrow = self.rowlist(index)
        for ind in listrow:
            if self.andukulist[ind].value == checkedvalue:
                return True
        return False

    """return the column indexs for any cell"""

    def collist(self, index):
        blocks = []
        i = index % 9
        for j in range(0, 9):
            blocks.append(self.position[j][i])
        return blocks

    """return true if the col has the value equal to the checkvalue"""

    def collistnotsolved(self, index):
        blocks = self.collist(index)
        for block in blocks:
            if self.andukulist[block].value != 0:
                blocks.remove(block)
        return blocks

    def isfoundcol(self, index, checkedvalue):
        listcol = self.collist(index)
        for ind in listcol:
            if self.andukulist[ind].value == checkedvalue:
                return True
        return False

    """return the box indexs for any cell (box is the 3*3 matrix and we have 9 boxes)"""

    def boxlist(self, index):
        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blocks.append(self.position[i][j:j + 3] + self.position[i + 1][j:j + 3] + self.position[i + 2][j:j + 3])
        for n in range(9):
            if index in blocks[n]:
                return blocks[n]

    def boxlistnotsolved(self, index):
        blocks = self.boxlist(index)
        for block in blocks:
            if self.andukulist[block].value != 0:
                blocks.remove(block)
        return blocks

    """return true if the box has the value equal to the checkvalue"""

    def isfoundbox(self, index, checkedvalue):
        listbox = self.boxlist(index)
        for ind in listbox:
            if self.andukulist[ind].value == checkedvalue:
                return True
        return False

    def istwobox(self, index1, index2):
        if index1 in self.boxlist(index2):
            return True
        else:
            return False

    """input is the index of list "a" 
    return cells with two true probability"""

    def peektwocellsinrow(self, index):
        row = self.rowlist(index)
        blocks = []
        for n in row:
            if self.truecount(n) == 2:
                blocks.append(n)
        return blocks

    def peektwocellsincol(self, index):
        col = self.collist(index)
        blocks = []
        for n in col:
            if self.truecount(n) == 2:
                blocks.append(n)
        return blocks

    def peektwocellsinbox(self, index):
        box = self.boxlist(index)
        blocks = []
        for n in box:
            if self.truecount(n) == 2:
                blocks.append(n)
        return blocks

    """input must be list of cells which has two true values
    output is a list of equal cells with respect ot values"""

    def peekequalcells(self, twolist):
        for index1 in twolist:
            for index2 in twolist[twolist.index(index1) + 1:]:
                if self.andukulist[index1].value == self.andukulist[index2].value:
                    return [index1, index2]

    """input must be list of cells which has two true values
    output is a list of equal cells with respect ot probability"""

    def peekequalprobcells(self, twolist):
        for index1 in twolist:
            for index2 in twolist[twolist.index(index1) + 1:]:
                for n in range(9):
                    if self.peektrue(index1) == self.peektrue(index2):
                        return [index1, index2]

    """check if all cells in the list has false results for given probability "m" """

    def isallfalse(self, m, listindex):
        count = 0
        for index in listindex:
            if self.andukulist[index].prob[m]:
                count += 1
        if count == 0:
            return True
        else:
            return False

    """take the cells and add the probability to by 1 or 2 and so on to 9"""

    def fullprob(self):
        for checkvalue in range(1, 10):
            for index in range(81):
                if self.andukulist[index].value == 0 and \
                        (not self.isfoundrow(index, checkvalue)) and \
                        (not self.isfoundcol(index, checkvalue)) and \
                        (not self.isfoundbox(index, checkvalue)):
                    self.andukulist[index].prob[checkvalue - 1] = True
                else:
                    self.andukulist[index].prob[checkvalue - 1] = False

    """this function called after one cell changed to it's true value and update it's row, 
    column and box by removing it from it's probability"""

    def partialprob(self, index, checkvalue):
        listprob = []
        listprob.extend(self.rowlist(index))
        listprob.extend(self.collist(index))
        listprob.extend(self.boxlist(index))
        for ind in listprob:
            self.andukulist[ind].prob[checkvalue - 1] = False
        for n in range(9):
            self.andukulist[index].prob[n] = False

    """if two cells in the same row has for example 2, 7 as probabiltity so for sure
    there is no other cells in the same row and box has 2, 7 so it should by removed 
    from it's row beside if it is in the same box it is also suppose to be removed
    from the box."""

    def solvetwovaluesrow(self):
        for index in range(0, 81, 9):
            listequal = self.peektwocellsinrow(index)
            if listequal is not None:
                m = self.peekequalprobcells(listequal)
                if m is not None:
                    problist = self.peektrue(m[0])
                    for n in self.rowlist(m[0]):
                        if n != m[0] and n != m[1]:
                            self.andukulist[n].prob[problist[0]] = False
                            self.andukulist[n].prob[problist[1]] = False

    def solvetwovaluescol(self):
        for index in range(0, 9):
            listequal = self.peektwocellsincol(index)
            if listequal is not None:
                m = self.peekequalprobcells(listequal)
                if m is not None:
                    problist = self.peektrue(m[0])
                    for n in self.collist(m[0]):
                        if n != m[0] and n != m[1]:
                            self.andukulist[n].prob[problist[0]] = False
                            self.andukulist[n].prob[problist[1]] = False

    def solvetwovaluesbox(self):
        for index in range(0, 9):
            listequal = self.peektwocellsinbox(index)
            if listequal is not None:
                m = self.peekequalprobcells(listequal)
                if m is not None:
                    problist = self.peektrue(m[0])
                    for n in self.boxlist(m[0]):
                        if n != m[0] and n != m[1]:
                            self.andukulist[n].prob[problist[0]] = False
                            self.andukulist[n].prob[problist[1]] = False

    """if the probability of cell is for example 5 and no other probability so
    the actual value for sure is 5, the below function scan about that idea"""

    def solveonevalues(self):
        for index in range(81):
            if self.truecount(index) == 1:
                self.solveone(index)

    def solvonlyvalues(self):
        for index in range(81):
            self.solveonly(index)

    """update the cell value by the actual value and remove any probability"""

    def solveone(self, index):
        for n in range(9):
            if self.andukulist[index].prob[n]:
                self.andukulist[index].value = n + 1
                self.andukulist[index].prob[n] = False
                self.partialprob(index, n + 1)

    def solveoneprob(self, n, index):
        self.andukulist[index].value = n + 1
        self.andukulist[index].prob[n] = False
        self.partialprob(index, n + 1)

    def solveonly(self, index):
        listrow = self.rowlistnotsolved(index)
        if index in listrow:
            listrow.remove(index)
        listcol = self.collistnotsolved(index)
        if index in listcol:
            listcol.remove(index)
        listbox = self.boxlistnotsolved(index)
        if index in listbox:
            listbox.remove(index)
        listtrue = self.peektrue(index)
        for m in listtrue:
            if self.isallfalse(m, listrow) and self.andukulist[index].prob[m]:
                self.solveoneprob(m, index)
                return
        for m in listtrue:
            if self.isallfalse(m, listcol) and self.andukulist[index].prob[m]:
                self.solveoneprob(m, index)
                return
        for m in listtrue:
            if self.isallfalse(m, listbox) and self.andukulist[index].prob[m]:
                self.solveoneprob(m, index)
                return

    """the below code solve the sudoku puzzle using the two cells idea described above
    then check for unique probablity for each cell but before any solution fullprob() add 
    the suitable probability for each cell"""

    def solvesudoku(self):
        self.fullprob()
        for _ in range(9):
            self.solveonevalues()  # case 1: only one probability for certain cell
            self.solvonlyvalues()  # case 2: more than one probability for certain cell
            # but one is unique in certain row or coumn or box
            self.solvetwovaluesrow()  # case 3: two probability in to cells on same row
            self.solvetwovaluescol()  # case 4: two probability in to cells on same column
            self.solvetwovaluesbox()  # case 5: two probability in to cells on same box

        for m in range(len(self.andukulist)):
            print(self.andukulist[m].value, end=" ")
            if (m + 1) % 3 == 0:
                print(end="    ")
            if (m + 1) % 9 == 0:
                print()
            if (m + 1) % 27 == 0:
                print()
        sumprob = 0
        for index in range(81):
            for prob in range(9):
                if self.andukulist[index].value == 0:
                    sumprob += 1
        if sumprob == 0:
            print("solved")
            # grinning face
            print("\U0001f60A")
        else:
            print("not solved")
            print("\U0001f60F")

    """for debugging purpose help to visualize ech cell probability"""

    def printanduku(self):
        print("*" * 20)
        for n in range(81):
            print("index: ", n, "value =", self.andukulist[n].value)
            for m in range(0, 9, 3):
                print(m + 1 if self.andukulist[n].prob[m] else " ",
                      m + 2 if self.andukulist[n].prob[m + 1] else " ",
                      m + 3 if self.andukulist[n].prob[m + 2] else " ")

    """for debugging purpose help to visualize one cell probability"""

    def printandukucell(self, n):
        print("index: ", n, "value =", self.andukulist[n].value)
        for m in range(0, 9, 3):
            print(m + 1 if self.andukulist[n].prob[m] else " ",
                  m + 2 if self.andukulist[n].prob[m + 1] else " ",
                  m + 3 if self.andukulist[n].prob[m + 2] else " ")

    """for debugging purpose help to visualize one box probability, box number is the index of any 
    cell basedon list "a" """

    def printandukubox(self, boxnumber):
        print("box: ", boxnumber)
        for n in self.boxlist(boxnumber):
            print("index: ", n, "value =", self.andukulist[n].value)
            for m in range(0, 9, 3):
                print(m + 1 if self.andukulist[n].prob[m] else " ",
                      m + 2 if self.andukulist[n].prob[m + 1] else " ",
                      m + 3 if self.andukulist[n].prob[m + 2] else " ")

    def printandukurow(self, rownumber):
        print("box: ", rownumber)
        for n in self.rowlist(rownumber):
            print("index: ", n, "value =", self.andukulist[n].value)
            for m in range(0, 9, 3):
                print(m + 1 if self.andukulist[n].prob[m] else " ",
                      m + 2 if self.andukulist[n].prob[m + 1] else " ",
                      m + 3 if self.andukulist[n].prob[m + 2] else " ")

    def printandukucol(self, colnumber):
        print("box: ", colnumber)
        for n in self.collist(colnumber):
            print("index: ", n, "value =", self.andukulist[n].value)
            for m in range(0, 9, 3):
                print(m + 1 if self.andukulist[n].prob[m] else " ",
                      m + 2 if self.andukulist[n].prob[m + 1] else " ",
                      m + 3 if self.andukulist[n].prob[m + 2] else " ")


if __name__ == "__main__":
    """sudoku puzzle to be solved"""
    """testcase one (solved :) )"""
    # listsudoku = [8, 0, 0, 5, 0, 0, 0, 0, 0,
    #               4, 0, 0, 0, 0, 0, 6, 1, 7,
    #               9, 0, 0, 2, 0, 0, 0, 0, 0,
    #               3, 9, 2, 0, 0, 0, 0, 0, 0,
    #               0, 0, 0, 0, 0, 8, 0, 3, 1,
    #               0, 0, 0, 0, 4, 6, 0, 0, 2,
    #               0, 3, 7, 0, 0, 0, 0, 0, 0,
    #               0, 0, 0, 0, 0, 0, 4, 7, 5,
    #               0, 8, 0, 0, 5, 1, 0, 0, 0]
    """testcase two (solved :) )"""
    # listsudoku = [0, 8, 0, 0, 6, 2, 0, 0, 0,
    #               0, 9, 0, 0, 5, 0, 0, 0, 8,
    #               0, 3, 0, 0, 0, 0, 0, 0, 5,
    #               0, 0, 0, 0, 4, 8, 0, 9, 0,
    #               0, 0, 0, 0, 0, 7, 0, 4, 0,
    #               2, 0, 5, 0, 0, 0, 0, 6, 0,
    #               3, 0, 7, 1, 0, 0, 0, 0, 0,
    #               0, 0, 4, 2, 0, 0, 3, 0, 0,
    #               0, 0, 0, 7, 0, 0, 9, 0, 4]

    """testcase three (solved :) )"""
    # listsudoku = [2, 7, 0, 0, 0, 0, 0, 5, 0,
    #               3, 0, 0, 8, 0, 0, 0, 1, 0,
    #               8, 0, 0, 5, 0, 0, 0, 7, 0,
    #               0, 4, 6, 0, 0, 0, 1, 0, 0,
    #               0, 0, 0, 4, 7, 0, 0, 0, 0,
    #               0, 0, 0, 0, 2, 0, 3, 0, 4,
    #               0, 8, 7, 0, 0, 9, 0, 0, 0,
    #               0, 0, 0, 0, 0, 5, 7, 0, 6,
    #               0, 0, 1, 0, 0, 4, 0, 0, 5]
    """testcase four (solved :) )"""
    # listsudoku = [2, 7, 0, 0, 0, 0, 0, 5, 0,
    #               3, 0, 0, 8, 0, 0, 0, 1, 0,
    #               8, 0, 0, 5, 0, 0, 0, 7, 0,
    #               0, 4, 6, 0, 0, 0, 1, 0, 0,
    #               0, 0, 0, 4, 7, 0, 0, 0, 0,
    #               0, 0, 0, 0, 2, 0, 3, 0, 4,
    #               0, 8, 7, 0, 0, 9, 0, 0, 0,
    #               0, 0, 0, 0, 0, 5, 7, 0, 6,
    #               0, 0, 1, 0, 0, 4, 0, 0, 5]

    listsudoku = [0, 0, 0, 6, 4, 1, 0, 0, 0,
                  1, 2, 0, 0, 0, 0, 0, 0, 3,
                  0, 8, 0, 0, 0, 0, 4, 5, 0,
                  8, 0, 0, 9, 6, 0, 0, 0, 0,
                  3, 0, 1, 0, 0, 4, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 3, 2, 9,
                  0, 4, 8, 1, 0, 0, 0, 0, 0,
                  0, 0, 7, 3, 9, 2, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 2, 1, 5]

    """testcase five (not solved :( )"""
    # listsudoku = [8, 0, 0, 0, 0, 0, 0, 0, 0,
    #               0, 0, 3, 6, 0, 0, 0, 0, 0,
    #               0, 7, 0, 0, 9, 0, 2, 0, 0,
    #               0, 5, 0, 0, 0, 7, 0, 0, 0,
    #               0, 0, 0, 0, 4, 5, 7, 0, 0,
    #               0, 0, 0, 1, 0, 0, 0, 3, 0,
    #               0, 0, 1, 0, 0, 0, 0, 6, 8,
    #               0, 0, 8, 5, 0, 0, 0, 1, 0,
    #               0, 9, 0, 0, 0, 0, 4, 0, 0]

    """In 2012, Finnish mathematician Arto Inkala claimed to have created the 
        "World's Hardest Sudoku". According to the British newspaper The Telegraph, 
        on the difficulty scale by which most Sudoku grids are graded, with one star 
        signifying the simplest and five stars the hardest, the above puzzle would 
        "score an eleven"."""

    """print the puzzle as """
    for n in range(len(listsudoku)):
        print(listsudoku[n] if listsudoku[n] != 0 else "_", end=" ")
        if (n + 1) % 3 == 0:
            print(end="    ")
        if (n + 1) % 9 == 0:
            print()
        if (n + 1) % 27 == 0:
            print()
    print("=" * 80)
    """instantiate object from Andoku class then call the solvesudoku() function to do the job"""
    sudoku = AndokuClass(listsudoku)
    sudoku.solvesudoku()
    # Debug is not solved using the below command
    # sudoku.printanduku()
    """This code is contributed by Moustafa Ali"""
