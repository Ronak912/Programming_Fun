#Give a string like "BBBCADDDD", return "DDDDBBBCA" with characters sorted by frequency.


def sortByFrequency(instr):
    hashmap = {}
    for char in instr:
        hashmap[char] = hashmap.get(char, 0) + 1


    outstr = ''
    for key, value in sorted(hashmap.items(), key=lambda x: x[1], reverse=True):
        outstr += key * value

    return outstr


if __name__ == "__main__":
    print sortByFrequency('EEEEEBBBCADDDD')