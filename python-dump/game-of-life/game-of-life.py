#!python

def var_count(elems):
    count = 0;
    for elem in elems:
        yield count, elem
        count += 1

class GameOfLife(object):

    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.rows = len(gameboard)
        self.columns = len(gameboard[0])
        
    def step_forward(self):
        gameboard = self.gameboard
        next_gameboard = [[0 for x in range(len(gameboard[0]))] for x in range(len(gameboard))] 
   
        
        top = 0
        bottom = 0
        left = 0
        right = 0
        for i, row in var_count(gameboard):
            if (i == 0):
                bottom = 1
            elif (i == (len(gameboard)-1)):
                top = 1
            else:
                top = 0
                bottom = 0
            for j, item in var_count(row):
                colony_count = 0
                
                if (j == 0):
                    left = 1
                elif (j == (len(row)-1)):
                    right = 1
                else:
                    left = 0
                    right = 0
            
                if (not right):
                    colony_count += (gameboard[i][j+1] == 1)
                if (not top):
                    colony_count += (gameboard[i+1][j] == 1)
                if  (not left):
                    colony_count += (gameboard[i][j-1] == 1)
                if (not bottom):
                    colony_count += (gameboard[i-1][j] == 1)
                if (not right and not top):
                    colony_count += (gameboard[i+1][j+1] == 1)
                if (not right and not bottom):
                    colony_count += (gameboard[i-1][j+1] == 1)
                if (not left and not top):
                    colony_count += (gameboard[i+1][j-1] == 1)
                if (not left and not bottom):
                    colony_count += (gameboard[i-1][j-1] == 1)
            
                if (colony_count < 2):
                    next_gameboard[i][j] = 0
                elif (colony_count == 2 and item):
                    next_gameboard[i][j] = 1
                elif (colony_count == 3):
                    next_gameboard[i][j] = 1
                else:
                    next_gameboard[i][j] = 0

        self.gameboard = next_gameboard
        
    def __str__(self):
        gameboard_string = ""
        for rows in self.gameboard:
            for item in rows:
                gameboard_string += " %d " % item
            gameboard_string += "\n"
        return gameboard_string
    
if __name__ == "__main__":
    gameboard = [[0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0,0],
                 [0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0]]

    print "Initial State"
    game = GameOfLife(gameboard)
    print game

    #for i in range(1, 10):
    #    print "Step %d" % i
    #    game.step_forward()
    #    print game
    cont = 1
    question = ""
    count = 1
    while (cont):
        question = raw_input("Step forward? ")
        if (question is "y"):
            game.step_forward()
            print "State %d" % count
            print game
            count += 1
        elif question is "n":
            cont = 0

