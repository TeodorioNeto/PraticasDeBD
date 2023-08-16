import sys
import operator

class Reducer:
    def __init__(self):
        self.H = {}

    def Reduce(self, key, value):
        self.H[key] = value

    def Close(self):
        sorted_items = sorted(self.H.items(), key=operator.itemgetter(1), reverse=True)
        for word, count in sorted_items:
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

