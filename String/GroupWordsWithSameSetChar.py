# http://www.geeksforgeeks.org/print-words-together-set-characters/

"""Group words with same set of characters
Given a list of words with lower cases. Implement a function to find all Words that have the same unique character set .

Example:

Input: words[] = { "may", "student", "students", "dog",
                 "studentssess", "god", "cat", "act",
                 "tab", "bat", "flow", "wolf", "lambs",
                 "amy", "yam", "balms", "looped",
                 "poodle"};
Output :
looped, poodle,
lambs, balms,
flow, wolf,
tab, bat,
may, amy, yam,
student, students, studentssess,
dog, god,
cat, act,

All words with same set of characters are printed
together in a line."""


def getKey(word):
    uniquechars= set([char for char in word])
    return ''.join(sorted(uniquechars))



def wordsWithSameCharSet(words, n):
    haspmap = {}
    for idx, word in enumerate(words):
        key = getKey(word)
        if key not in haspmap:
            haspmap[key] = [idx]
        else:
            haspmap[key].append(idx)

    for key in haspmap:
        similarwords = haspmap[key]
        if len(similarwords) > 1:
            print ', '.join(words[i] for i in similarwords)



if __name__ == "__main__":
    words = ["may", "student", "students", "dog", "studentssess", "god", "cat", "act", "tab",
             "bat", "flow", "wolf", "lambs", "amy", "yam", "balms", "looped", "poodle"]
    n = len(words)
    wordsWithSameCharSet(words, n)