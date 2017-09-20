wordlst = ["cat","lion","act","dog"]

def findWords(inputword):
    global wordlst
    hashmap = {}
    #O(MN): where N: numer of words and M:size of each word
    for word in wordlst:
        hashcode = 0
        for char in word:
            hashcode += ord(char)
        if hashcode not in hashmap:
            hashmap[hashcode] = [word]
        else:
            hashmap[hashcode].append(word)

    hashcode = 0
    # O(M): length of word
    for char in inputword:
        hashcode += ord(char)

    # O(1)
    if hashcode not in hashmap:
        return False

    newsortedword = ''.join(sorted(inputword)).lower()
    wordlst = hashmap[hashcode]
    for word in wordlst:
        if newsortedword == ''.join(sorted(word)).lower():
            print word,

    # below is more pythonic way but not efficient in terms of time complexity
    print ""
    for word in wordlst:
        tmpwrd = "".join(sorted(list(word)))
        if "".join(sorted(list(inputword))).lower() == tmpwrd.lower():
            print word,

if __name__ == "__main__":
    findWords('tac')