
def load_dictionary():

        dictionary = {}

        with open('words.txt', 'r') as file:

            for line in file:

                word = line.strip()

                dictionary[word] = True

        return dictionary