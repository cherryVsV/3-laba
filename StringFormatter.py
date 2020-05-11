'''Напишите простой класс StringFormatter для форматирования строк со
следующим функционалом:
– удаление всех слов из строки, длина которых меньше n букв;
– замена всех цифр в строке на знак «*»;
– вставка по одному пробелу между всеми символами в строке;
– сортировка слов по размеру;
– сортировка слов в лексикографическом порядке.
Примечание. Разделители слов можно задавать отдельно. По
умолчанию в качестве разделителя принимается только символ
пробела.'''

class StringFormatter(object):
    @staticmethod
    def DelWords(string,n):
        words = string.split(' ')
        for i in range(len(words)):
            if (len(words[i])<n):
                words[i] = ''
        return ' '.join(words)

    @staticmethod    
    def ReplaceNum(string):
         words = string.split(' ')
         for i in range(len(words)):
             lit = list(words[i])
             for j in range(len(lit)):
                 if lit[j].isdigit():
                     lit[j]='*'
             words[i] = ''.join(lit)
         return ' '.join(words)
    @staticmethod
    def CreateSpace(string):
        words = string.split(' ')
        for i in range(len(words)):
            lit = list(words[i])
            words[i] = ' '.join(lit)
        return ' '.join(words)
        
    @staticmethod    
    def SortSize(string):
        words =  string.split(' ')
        return ' '.join(sorted(words, key=lambda word: len(word))).lstrip()
    @staticmethod
    def SortLex(string):
        words =  string.split(' ')
        return ' '.join(sorted(words)).lstrip()