# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Hackerrank.Game_of_Thrones_I import gameOfThrones


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

class SubRectangle(Rectangle):
    def __init__(self, length, width, offset):
        super().__init__(length, width)  # Appel du constructeur de la classe parente pour initialiser length et width
        self.offset = offset

    def calculTotal(self):
        return super().area() * self.offset  # Appel correct de la méthode area() de la classe parente



class Vehicule:

    def __init__(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

class Scooter(Vehicule):

    def __init__(self, speed, consumtion):
        super().__init__(speed)
        self.consumtion = consumtion

    def calculPower(self):
        return super().getSpeed()/ self.consumtion

def find_closest(my_list, target):
    # Use the min function with a key that calculates the absolute difference
    # between each number and the target
    closest_num = min(my_list, key=lambda x: abs(x - target))
    return closest_num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm ghghjj')


word = "cdefghmnopqrstuvw"

testFunc = gameOfThrones(word)

print(testFunc)