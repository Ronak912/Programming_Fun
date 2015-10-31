wordlst = ["cat","lion","act","dog"]

def findWords(inputword):
    for word in wordlst:
        tmpwrd = "".join(sorted(list(word)))
        if "".join(sorted(list(inputword))).lower() == tmpwrd.lower():
            print word

if __name__ == "__main__":
    findWords('tac')