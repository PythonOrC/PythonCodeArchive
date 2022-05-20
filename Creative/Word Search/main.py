class wordSearch():
    def __init__(self):
        self.setup()
        self.search()

    def setup(self):
        self.letters = []
        # self.row = int(input("Number of Rows: "))
        # for i in range(self.row):
        #     self.row = list(input(f"{i+1}:"))
        #     self.letters.append(self.row)
        self.letters = [
        ['s','p','f','i','s','i','c','a','b','q','g','n','e'],
        ['o','e','s','p','a','n','o','l','e','u','s','b','r'],
        ['c','x','b','e','c','o','n','o','m','i','a','i','m'],
        ['i','a','r','t','e','g','q','f','a','m','f','o','i'],
        ['o','m','c','a','c','l','o','u','r','i','v','l','n'],
        ['l','e','p','r','u','e','b','a','a','c','d','o','g'],
        ['o','n','u','e','o','n','e','z','h','a','u','g','l'],
        ['g','n','d','a','m','c','l','a','s','e','t','i','e'],
        ['i','e','j','i','l','c','i','e','n','c','i','a','s'],
        ['a','p','e','r','i','o','d','i','s','m','o','p','i'],
        ['d','s','t','h','o','r','a','r','i','o','q','x','a'],
        ['h','u','m','a','n','i','d','a','d','e','s','m','o'],
    ]

        self.first_letter = []
        self.last_letter = []

    def validity(self):
        length = len(self.letters[0])
        for i in range(len(self.letters)):
            if len(self.letters[i]) != length:
                print(f"Unmatching length on row {i+1}")
                return False
            else:
                return True

    def search(self):
        valid = self.validity()
        if valid:
            self.word = input("Word: ")
            for i in range(len(self.letters)):
                for j in range(len(self.letters[i])):
                    if self.letters[i][j] == self.word[0]:
                        self.first_letter = [i+1, j+1]
                        self.horizontal = True
                        self.vertical = True
                        for n in range(1, len(self.word)):
                            if (j+n <= (len(self.letters[i])-1)) and self.horizontal:
                                if self.letters[i][j+n] == self.word[n]:
                                    if n == (len(self.word)-1):
                                        self.last_letter = [i+1, j+n+1]
                                        print(f"\"{self.word}\" is horizontal,")
                                        print(f"starting at row {self.first_letter[0]}, column {self.first_letter[1]}")
                                        print(f"ending at row {self.last_letter[0]}, column {self.last_letter[1]}")
                                else:
                                    self.horizontal = False

                            if (i+n <= len(self.letters)-1) and self.vertical:
                                if self.letters[i+n][j] == self.word[n]:
                                    if n == (len(self.word)-1):
                                        self.last_letter = [i+n+1, j+1]
                                        print(f"\"{self.word}\" is vertical,")
                                        print(f"starting at row {self.first_letter[0]}, column {self.first_letter[1]}")
                                        print(f"ending at row {self.last_letter[0]}, column {self.last_letter[1]}")
                                else:
                                    self.vertical = False

            if not self.last_letter:
                print('Not found')



if __name__ == "__main__":
    word_search = wordSearch()
