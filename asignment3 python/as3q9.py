def word_count(fname, word):
    with open(fname) as f:
        return Counter(f.read().split())[word]

print("Number of occurrences of the word '{}' in the file is: {}".format(word, word_count("text.txt", word)))