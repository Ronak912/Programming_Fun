"""
mynameisronak and ronakismyname are anagram (ovreall they both contains same characters)
"""

def isAnagram(str1, str2):

    if len(str1) != len(str2):
        return False

    dict1, dict2 = {}, {}

    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    for char in str2:
        if char in dict1:
            dict1[char] -= 1
        else:
            dict1[char] = -1

    print dict1

    isanagram = True
    for key, value in dict1.iteritems():
        if value != 0:
            isanagram = False
            break
    return isanagram


def isAnagram1(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    isanagram = True
    for i, j in zip(str1, str2):
        if i != j:
            isanagram = False
            break
    return isanagram



if __name__ == '__main__':
    print isAnagram('ronakismyname', 'mynameisronak')
    print isAnagram1('ronakismyname', 'mynameisronak')