import random

feet_in_mile = 5200
meters_in_kilometers = 1000
beatles = ["REd", "Blue", "Green", "Yellow"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]
def roll_dice(num ):
    return random.randint(1,num)