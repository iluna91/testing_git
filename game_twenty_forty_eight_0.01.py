"""
Clone of 2048 game.
test
"""
import merge
import random
#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

#def merge(line):
#    """
#    Helper function that merges a single row or column in 2048
#    """
    # replace with your code from the previous mini-project
#    return []
# height - filas width- columnas
class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.__height = grid_height
        self.__width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.__grid = [[ 0 for dummy_col in range(self.__width)] for dummy_row in range(self.__height)]
        for number_tiles in range(2):
            self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.__grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.__height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.__width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #Secures atleast one empty square
        possible_coordinates = []
        empty_grid_square = False
        for dummy_row in range(self.__height):
            for dummy_col in range(self.__width):
                if self.__grid[dummy_row][dummy_col] == 0:
                    empty_grid_square = True
                    possible_coordinates.append([dummy_row, dummy_col])  
        #print possible_coordinates                    
        if empty_grid_square == True:
            coordinate = rand_grid_coordinate(possible_coordinates)            
            #if self.__grid[coordinate[0]][coordinate[1]] == 0:
            #    break   
            self.__grid[coordinate[0]][coordinate[1]] = rand_tile_number()
        else:
            print "no empty square"

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0

def rand_tile_number():
    probability = random.random()
    if probability <= 0.9:
        return 2
    else:
        return 4
         
def rand_grid_coordinate(coordinates):
    #rand_height = random.randint(0, height)
    #rand_width = random.randint(0, width)
    coordinate_grid = random.choice(coordinates)
    return coordinate_grid
     
def my_test():
    
    my_game = TwentyFortyEight(6,5)
    print "----------------------"
    #my_game 
    print "----------------------"
    print str(my_game)
    print my_game.get_grid_height(), my_game.get_grid_width()
    my_game.__height = 7
    my_game.__width = 7
    my_game.grid_height = 8
    print my_game.get_grid_height(), my_game.get_grid_width()
    list_rand = []
    coordinates = []
    for index in range(15):
        list_rand.append(rand_tile_number())
        coordinates.append(rand_grid_coordinate([[0,0],[0,1],[1,0],[1,1],[1,3],[3,4],[5,6]]))
    print coordinates    
    print list_rand
    print list_rand,  "esto es una modificacoin test"

    
my_test()
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
