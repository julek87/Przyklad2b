from json import load, dump
from random import choice


class EglishDictionary:
    def __init__(self, filename='english_dict.json'):
        self.filename = filename
        self.words = self.load_words()

    def load_words(self):
        with open(self.filename, encoding='utf8') as file:
            return load(file)

    def display_random_words(self, number_of_words):
        random_words = []
        for _ in range(number_of_words):
            word = choice(self.words)
            random_words.append((word.get('english'), word.get('polish')))
        return random_words

    def add_word(self, english_word, polish_word):
        self.words.append({
            'english': english_word,
            'polish': polish_word
        })
        self.save_words()

    def save_words(self):
        with open(self.filename, 'w', encoding="utf8") as file:
            dump(self.words, file)

if __name__ == '__main__':
    english_dict = EglishDictionary()

    while True:
        print('''\n[1] - Ćwicz,
[2] - Wyświetl losowe słówka na dziś,
[3] - Wprowadź nowe słowo do słownika,
[0] - Zamknij Program.''')
        your_choice = int(input('Co chcesz zrobić: '))

        if your_choice == 1:
            number_of_words_to_practice = int(input("Ile słów chcesz powtórzyć: "))
            words_to_practice = english_dict.display_random_words(number_of_words_to_practice)

            for english, polish in words_to_practice:
                print(f'\nAngielskie słowo: {english}')
                attempts = 3

                while attempts > 0:
                    user_translate = input('Podaj tłumaczenie w języku polskim: ')

                    if user_translate == polish:
                        print("Prawidłowa odpowiedź.")
                        break
                    else:
                        attempts -= 1
                        print(f'Nieprawidłowa odpowiedź. Pozostało {attempts} prób.')

                if attempts == 0:
                    print(f'Prawidłowe tłumaczenie: {polish}')

        elif your_choice == 2:
            number_of_words_to_display = int(input('Ile słów mam wyświetlić? '))
            english_dict.display_random_words(number_of_words_to_display)

        elif your_choice == 3:
            english_word_input = input('Podaj angielskie słowo: ')
            polish_word_input = input(f'Podaj tłumaczenie {english_word_input} w języku polskim: ')
            english_dict.add_word(english_word_input, polish_word_input)

        elif your_choice == 0:
            print("Zamykam program.")
            break

        else:
            print('Nieprawidłowy wybór. Spróbuj ponownie.')