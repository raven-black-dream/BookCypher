import string
import random


class Book:

    def __init__(self, filename):
        self.text: dict = self.get_book_text(filename=filename)
        self.word_list: list = self.get_word_list()

    @staticmethod
    def get_book_text(filename: str) -> dict:
        text = {}
        book = open(filename, 'r')
        book_txt = book.read()
        translator = str.maketrans('', '', string.punctuation)
        book_txt = book_txt.translate(translator)
        page_num = 1
        for page in book_txt.split('PAGE'):
            line_num = 1
            lines = page.split('\n')
            for line in lines:
                words = line.split(' ')
                word_num = 1
                for word in words:
                    if word.lower() not in text.keys():
                        text[word.lower()] = []
                    text[word.lower()].append(Word(word.lower(), page_num, line_num, word_num))
                    word_num += 1
                line_num += 1
            page_num += 1
        return text

    def encode(self, filename: str) -> str:

        encoded = ''
        with open(filename, 'r') as f:
            text: list[str] = f.read().split(' ')
            for text_word in text:
                punctuation = None
                if any(punct in text_word for punct in string.punctuation):
                    punctuation = text_word[-1]
                    text_word = text_word[:-1]

                try:
                    words = self.text[text_word.lower()]
                    rand_num = random.randint(0, len(words) - 1)
                    word = words[rand_num].encode()
                except KeyError as e:
                    word = text_word
                    pass
                if not punctuation:
                    encoded += f'{word} '
                else:
                    encoded += f'{word}{punctuation} '

        return encoded

    def decode(self, filename: str) -> str:
        decoded = ''
        with open(filename, 'r') as f:
            encoded = f.read()
            for encoded_word in encoded.split(' '):
                split = encoded_word.split(':')
                for word in self.word_list:
                    try:
                        if not word.check_encoded(int(split[0]), int(split[1]), int(split[2])):
                            continue
                        else:
                            decoded += f'{word.text} '
                            break
                    except ValueError:
                        decoded += f'{encoded_word} '
                        break
                    except IndexError:
                        decoded += f'{encoded_word} '
                        break
        return decoded

    def get_word_list(self):
        word_list = []
        for word in self.text.keys():
            for item in self.text[word]:
                word_list.append(item)
        return word_list


class Word:

    def __init__(self, text: str, page: int, line: int, word: int):
        self.text = text
        self.page = page
        self.line = line
        self.word = word

    def __repr__(self):
        return f'{self.text} ({self.page}, {self.line}, {self.word})'

    def encode(self):
        return f'{self.page}:{self.line}:{self.word}'

    def check_encoded(self, page: int, line: int, word: int):
        return page == self.page and line == self.line and word == self.word


if __name__ == '__main__':
    book = Book('BookOfNod.txt')
    encoded = book.encode('text_to_be_encoded.txt')
    with open('encoded.txt', 'w') as f:
        f.write(encoded)

    decoded = book.decode('encoded.txt')
    with open('decoded.txt', 'w') as f:
        f.write(decoded)

