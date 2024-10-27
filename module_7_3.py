import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i,'r+' , encoding='utf-8') as file:
                text_of_words = file.read().lower()
                text_of_words = re.sub(' - ', ' ', text_of_words)
                text_of_words = re.sub('[,|.|!|=|?|;|:]', '', text_of_words)
                # for char in text_of_words:
                #     if char == ',' or char == '.' or char == '=' or char == '!' or char == '?' or char == ';' or char == ':':
                #         text_of_words = text_of_words.replace(char, '')
                list_of_words = text_of_words.split()
                all_words.update({i:list_of_words})
            #print(f'fineshed fork with file: {i}')
        return all_words


    def find(self, word):
        name_file = self.get_all_words()
        list_of_keys = name_file.keys()
        for i in list_of_keys:
            list_of_words = name_file[i]
            for j in range(len(list_of_words)):
                if list_of_words[j] == word.lower():
                    return {i:j}
        print("sorry this word can't be find")
        return {}

    def count(self, word):
        name_file = self.get_all_words()
        list_of_keys = name_file.keys()
        dict_word_count = {}
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
                dict_word_count.update({i: count_of_word})
        if len(dict_word_count) == 0:
            print("sorry this word can't be find")
            return {}
        else:
            return dict_word_count


finder2 = WordsFinder('test_file.txt', 'sample.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

