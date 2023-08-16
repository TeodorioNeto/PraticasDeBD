import io
import re
import sys

class Mapper:
    def __init__(self):
        self.H = {}

    def Map(self, a, d):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        d = d.strip()
        d = re.sub(r'[^\w\s]', '', d)
        d = d.lower()

        for x in d:
            if x in punctuations:
                d = d.replace(x, " ")

        words = d.split()
        for word in words:
            if word in self.H:
                self.H[word] += 1
            else:
                self.H[word] = 1

    def Close(self):
        for word, count in self.H.items():
            print('%s\t%s' % (word, count))
          
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
mapper = Mapper()

for line in input_stream:
    mapper.Map("doc1", line)

mapper.Close()

