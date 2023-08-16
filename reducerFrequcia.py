from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
word_count_pairs = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.lower()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            word_count_pairs.append((current_word, current_count))
        current_count = count
        current_word = word

# do not forget to store the last word's count if needed!
if current_word == word:
    word_count_pairs.append((current_word, current_count))

# Sort the word_count_pairs in descending order of counts
sorted_pairs = sorted(word_count_pairs, key=lambda x: x[1], reverse=True)

# Print the sorted results
for word, count in sorted_pairs:
    print('%s\t%s' % (word, count))

