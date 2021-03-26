# core functionalities of bot go here
import random

# randomly selects a quote from phrases.txt
def reader(file_path):
    quotes = []
    with open(file_path, 'r') as file:
        for line in file:
            quotes.append(line)
    return quotes


# quotes = reader('../replies/phrases.txt')

def get_random(quotes:list):
    list_len = len(quotes)-1
    rand = random.randint(0, list_len)
    return rand


# print(get_random(quotes))
if __name__ == '__main__':
    reader
    get_random