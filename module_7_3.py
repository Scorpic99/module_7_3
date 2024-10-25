
class WordsFinder:
    def __init__(self, *args):
        self.args = list(args)

    def get_all_words(self):
        all_words = {}
        for i in self.args:
            with open(i,'r+' , encoding='utf-8') as file:
                text_of_words = file.read().lower()
                for char in text_of_words:
                    if char == ',' or char == '.' or char == '=' or char == '!' or char == '?' or char == ';' or char == ':' or char == ' - ':
                        if char != ' - ':
                            text_of_words = text_of_words.replace(char, '')
                        else:
                            text_of_words = text_of_words.replace(char, ' ' )
                list_of_words = text_of_words.split()
                all_words.update({i:list_of_words})
            #print(f'fineshed fork with file: {i}')
        return all_words


    def find(self, word):
        name_file = self.get_all_words()
        list_of_keys = name_file.keys()
        for i in list_of_keys:
            list_of_words = name_file[i]
            for j in list_of_words:
                if j == word.lower():
                    with open(i, 'r', encoding='utf-8') as file:
                        my_file = file.read()
                        pos_of_word = my_file.find(word.lower())
                        return {i:pos_of_word}
        print("sorry this word can't be find")
        return {}

    def count(self, word):
        name_file = self.get_all_words()
        list_of_keys = name_file.keys()
        for i in list_of_keys:
            list_of_words = name_file[i]
            count_of_word = 0
            for j in list_of_words:
                if j == word.lower():
                    count_of_word += 1
                    continue
            if count_of_word == 0:
                continue
            else:
                return {i: count_of_word}

        print("sorry this word can't be find")
        return {}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

