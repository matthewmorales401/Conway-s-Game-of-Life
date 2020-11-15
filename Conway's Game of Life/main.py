from ast import literal_eval
import time
import random
class Tile(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.coordinate = None
        self.empty = True

    def __str__(self):
        return str(self.coordinate)

class Board(object):
    def __init__(self):
        self.tiles = None
        self.space = " "
        self.rows = None
        self.columns = None
        self.tileList = {}
        self.neighborDict = {}

    def tileAsk(self, tiles):
        try:
            if len(tiles) > 1:
                return False
            return True
        except TypeError:
            return False

    def checkEmpty(self, animal):
        for key in self.tileList:
            if key.coordinate == animal.location:
                return key.empty

    def setup(self):
        while True:
            try:
                if self.tiles is None or self.tileAsk(self.tiles) is False:
                    time.sleep(1)
                    self.tiles = input("What character/symbol do you want to use?")
                    time.sleep(1)
                    self.tiles = "".join(self.tiles.split())
                    if self.tileAsk(self.tiles) is False:
                        print("Please enter a single character only.")
                        time.sleep(1)
                    continue
                if self.rows is None:
                    time.sleep(1)
                    self.rows = int(input("How many rows do you want?"))
                    if self.rows == 0:
                        time.sleep(1)
                        print("Please choose a value greater than 0")
                        self.rows = None
                    continue
                if self.columns is None:
                    time.sleep(1)
                    self.columns = int(input("How many columns do you want?"))
                    if self.columns == 0:
                        print("Please choose a value greater than 0")
                        self.columns = None
                    continue
                time.sleep(1)
                break
            except SyntaxError:
                print("Invalid character input. Please try again")
                time.sleep(1)
                continue
            except ValueError:
                print("Invalid character input. Please try again")
                time.sleep(1)
                continue

    def createDisplay(self):
        for tile in range(1, self.columns + 1):
            for oTile in range(1, self.rows + 1):
                objtile = Tile(self.tiles)
                objtile.coordinate = (oTile, tile)
                self.tileList[objtile] = None
                print(self.tiles, end=" ")
                if oTile % self.rows == 0:
                    print("")

    def randomBoard(self):
        animal = Animal()
        while True:
            if animal.species is None or self.tileAsk(animal.species) is False:
                animal.species = input("What character/symbol do you want to use for your creature?")
                time.sleep(1)
                animal.species = "".join(animal.species.split())
                if animal.species == self.tiles:
                    animal.species = None
                    print("Please use a symbol that is different from the tiles.")
                    continue
                if self.tileAsk(animal.species) is False:
                    print("Please enter a single character only.")
                    time.sleep(1)
                    continue
                break
        for tile in range(1, self.columns + 1):
            for oTile in range(1, self.rows + 1):
                objtile = Tile(self.tiles)
                objtile.coordinate = (oTile, tile)
                self.tileList[objtile] = None

        for key in self.tileList:
            randomNumber = random.choice([1, 2])
            if randomNumber == 1:
                animal.location = key.coordinate
                key.empty = False
                self.tileList[key] = animal
            else:
                self.tileList[key]
        self.startGame(animal)



    def addAnimal(self):
        coordinate = None
        copy_detect = False
        animal = Animal()
        copy_animal = Animal()
        copySpecies = None
        while True:
            try:
                if animal.species is None or self.tileAsk(animal.species) is False:
                    if copy_detect:
                        animal.species = copySpecies
                        continue
                    animal.species = input("What character/symbol do you want to use for your creature?")
                    time.sleep(1)
                    animal.species = "".join(animal.species.split())
                    copySpecies = animal.species
                    if animal.species == self.tiles:
                        animal.species = None
                        print("Please use a symbol that is different from the tiles.")
                        continue
                    if self.tileAsk(animal.species) is False:
                        print("Please enter a single character only.")
                        time.sleep(1)
                        continue
                    continue
                if coordinate is None:
                    print("Input the coordinate of where you want to place the creature (format: (x, y)):)")
                    coordinate = input("Type your coordinate:")
                    time.sleep(1)
                    "".join(coordinate.split())
                location = literal_eval(coordinate)
                if isinstance(location, int):
                    coordinate = None
                    print("Please insert a valid coordinate using the provided format.")
                    time.sleep(1)
                    continue
                if animal.location is None or copy_animal.location is None:
                    if not isinstance(location, tuple):
                        print("Please insert a valid coordinate using the provided format.")
                        time.sleep(1)
                        continue
                    elif location[0] > self.rows or location[1] > self.columns:
                        print("Please choose a coordinate that is not out of bounds")
                        time.sleep(1)
                        continue
                    elif self.checkEmpty(animal):
                        print("There's already a creature on this tile.")
                        time.sleep(1)
                        continue
                    elif location[0] < 0 or location[1] < 0:
                        print("Negative coordinate(s) are not applicable.")
                        time.sleep(1)
                        continue
                    animal.location = literal_eval(coordinate)
                    for key in self.tileList:
                        if key.coordinate == animal.location:
                            self.tileList[key] = animal
                    time.sleep(1)
                    self.updateDisplay(animal)
                answer = input("Want to add another creature? Yes/Y/y or No/N/n?")
                time.sleep(1)
                if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y":
                    animal = Animal()
                    animal.species = copySpecies
                    copy_detect = True
                    coordinate = None
                elif answer == "No" or answer == "N" or answer == "n" or answer == "no":
                    break
                else:
                    print("Please input using the provided text.")
                    time.sleep(1)
            except SyntaxError:
                print("Invalid character input. Please try again")
                coordinate = None
                time.sleep(1)
                continue
            except ValueError:
                print("Invalid character input. Please try again")
                time.sleep(1)
                continue
        self.startGame(animal)

    def updateDisplay(self, animal):
        for key in self.tileList:
            if key.coordinate == animal.location:
                key.empty = False
        for key in self.tileList:
            if not key.empty:
                print(animal.species, end=" ")
            else:
                print(self.tiles, end=" ")
            if key.coordinate[0] % self.rows == 0:
                print("")

    def startGame(self, animal):
        for x in range(0, 5):
            b = "Loading" + "." * x
            print(b, end="\r")
            time.sleep(0.5)
        for key in self.tileList:
            if not key.empty:
                print(animal.species, end=" ")
            else:
                print(self.tiles, end=" ")
            if key.coordinate[0] % self.rows == 0:
                print("")
        print("")
        time.sleep(1)
        while True:
            for key in self.tileList:
                self.checkNeighbor(key)
            for key, value in self.neighborDict.items():
                # print(str(key) + str(value))
                if not key.empty:
                    if value < 2:
                        del value
                        key.empty = True
                    elif value > 3:
                        del value
                        key.empty = True
                    elif value == 2 or value == 3:
                        key.empty = False
                        continue
                elif key.empty:
                    if value == 3:
                        new_animal = Animal()
                        new_animal.species = animal.species
                        new_animal.location = key.coordinate
                        key.empty = False
                        self.tileList[key] = new_animal
            for key in self.tileList:
                if not key.empty:
                    print(animal.species, end=" ")
                else:
                    print(self.tiles, end=" ")
                if key.coordinate[0] % self.rows == 0:
                    print("")
            print("")
            time.sleep(1)

    def checkNeighbor(self, tile):
        neighbors = 0
        stopper = 0
        for item in self.tileList:
            if stopper == 8:
                break
            if item != tile:
                if item.coordinate == (tile.coordinate[0], tile.coordinate[1] + 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0], tile.coordinate[1] - 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] + 1, tile.coordinate[1]):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] - 1, tile.coordinate[1]):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] + 1, tile.coordinate[1] + 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] - 1, tile.coordinate[1] - 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] + 1, tile.coordinate[1] - 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1
                if item.coordinate == (tile.coordinate[0] - 1, tile.coordinate[1] + 1):
                    if not item.empty:
                        neighbors = neighbors + 1
                        stopper = stopper + 1

        self.neighborDict[tile] = neighbors


class Animal(object):
    def __init__(self):
        self.location = None
        self.species = None


def main():
    board = Board()
    board.setup()
    while True:
        randChoice = input("Do you want to randomly generate the board with animals? Yes/Y or N/No?")
        if randChoice == "Yes" or randChoice == "Y" or randChoice == "yes" or randChoice == "y":
            board.randomBoard()
            break
        elif randChoice == "No" or randChoice == "N" or randChoice == "no" or randChoice == "n":
            time.sleep(1)
            board.createDisplay()
            board.addAnimal()
            break
        time.sleep(1)
        print("Please type a valid answer.")

main()

