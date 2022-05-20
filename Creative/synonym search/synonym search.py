from bs4 import BeautifulSoup
import requests
import os


class findSynonyms:
    def __init__(self, input_method, file_loc="words.txt"):
        self.input_method = input_method
        self.file_loc = file_loc
        self.main()

    def add_to_clipboard(self, text):
        command = "echo | set /p nul=" + text.strip() + "| clip"
        os.system(command)

    def search(self, word):
        if word == "EXIT" or word == "DONE":
            exit()
        page = requests.get(f"https://www.thesaurus.com/browse/{word}")
        soup = BeautifulSoup(page.content, "html5lib")
        closest = soup.find_all("a", class_="css-1kg1yv8 eh475bn0")
        closer = soup.find_all("a", class_="css-1gyuw4i eh475bn0")
        close = soup.find_all("a", class_="css-1n6g4vv eh475bn0")

        closest_list = [i.text[:-1] for i in closest]
        closer_list = [i.text[:-1] for i in closer]
        close_list = [i.text[:-1] for i in close]

        synonyms_list = closest_list + closer_list + close_list

        if len(synonyms_list) > 3:
            synonyms_list = synonyms_list[:3]

        result = word + ": " + ", ".join(synonyms_list) + "    "
        print(result)
        return result

    def main(self):

        if self.input_method.lower() == "keyboard":
            while True:
                word = input("Word: ")
                self.add_to_clipboard(self.search(word))
        if self.input_method.lower() == "text file":
            results = ""

            with open(self.file_loc, "r") as f:
                words = f.read().split()

            for word in words:
                results += self.search(word)
            self.add_to_clipboard(results)


if __name__ == "__main__":
    file_loc = "words.txt"
    input_method = input("Keyboard or text file: ")
    synonyms = findSynonyms(input_method=input_method, file_loc=file_loc)
