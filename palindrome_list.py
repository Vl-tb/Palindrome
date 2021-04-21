"""
Palindrome class realization.
"""

from linkedstack import LinkedStack

class Palindrome:
    """
    This class represents
    """
    def __init__(self):
        self.stack = LinkedStack()
        self.palindroms = []

    def read_file(self, file):
        """
        This method reads words from file, and
        returns them in list.
        """
        with open(file, "r", encoding="utf-8") as dictionary:
            output = dictionary.readlines()
        if file == "words.txt":
            for i in range(len(output)):
                output[i] = output[i][:-1]
        else:
            i = 0
            while i < len(output):
                if output[i].split(" ")[0] != '':
                    output[i] = output[i].split(" ")[0]
                    i += 1
                else:
                    output.remove(output[i])
        return output

    def write_to_file(self, file):
        """
        This method writes found palindromes to file.
        """
        with open(file, "w", encoding="utf-8") as palindromes:
            for i in range(len(self.palindroms)):
                line = f"{self.palindroms[i]}\n"
                if i != len(self.palindroms) - 1:
                    palindromes.write(line)
                else:
                    palindromes.write(line[:-1])

    def find_palindromes(self, read_f, write_f):
        """
        This method finds palindromes in list of words.
        """
        counter = 0
        i = 0
        self.palindroms = []
        words = self.read_file(read_f)
        while i < len(words):
            if words[i] != '':
                word = words[i]
                if len(word) % 2 != 0:
                    counter = 1
                for index_start in range(len(word)//2):
                    self.stack.push(word[index_start])
                for index_end in range(len(word)//2 + counter, len(word)):
                    if word[index_end] == self.stack.peek():
                        self.stack.pop()
                if self.stack.isEmpty():
                    self.palindroms.append(word)
                self.stack.clear()
            counter = 0
            i += 1
        self.write_to_file(write_f)
        return self.palindroms
