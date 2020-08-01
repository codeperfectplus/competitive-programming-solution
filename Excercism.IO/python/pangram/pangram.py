import string

def is_pangram(sentence):
    s = sentence.lower().replace(" ","")
    return set(s.lower()) >= set(string.ascii_lowercase)
