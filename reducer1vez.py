import sys

class Reducer:
    def __init__(self):
        self.H = {}

    def Reduce(self, key, value):
        if value == 1:
            self.H[key] = value

    def Close(self):
        for word, count in self.H.items():
            print('%s\t%s' % (word, count))

reducer = Reducer()

current_word = None
word_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        word_count += count
    else:
        if current_word is not None:
            reducer.Reduce(current_word, word_count)
        current_word = word
        word_count = count

if current_word is not None:
    reducer.Reduce(current_word, word_count)

reducer.Close()
