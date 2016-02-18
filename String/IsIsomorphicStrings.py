# http://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

# Check if two given strings are isomorphic to each other

#
# Examples:
#
# Input:  str1 = "aab", str2 = "xxy"
# Output: True
# 'a' is mapped to 'x' and 'b' is mapped to 'y'.
#
# Input:  str1 = "aab", str2 = "xyz"
# Output: False
# One occurrence of 'a' in str1 has 'x' in str2 and
# other occurrence of 'a' has 'y'.


def areIsomorphic(str1, str2):
    m = len(str1)
    n = len(str2)

    if m != n:
        return False

    hashmap = {}
    for idx, char1 in enumerate(str1):
        char2 = str2[idx]
        if char1 not in hashmap:
            hashmap[char1] = char2
        elif hashmap.get(char1, '') != char2:
            return False
    return True


if __name__ == '__main__':
    print areIsomorphic("aabbaacc", "xxyyxxzz")
    print areIsomorphic("aab", "xyz")