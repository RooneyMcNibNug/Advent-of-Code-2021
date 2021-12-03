from collections import Counter

string = "hello world"
print ''.join(char[0] for char in Counter(string).most_common())
