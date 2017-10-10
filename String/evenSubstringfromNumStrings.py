# http://www.geeksforgeeks.org/number-of-even-substrings-in-a-string-of-digits/

# Number of even substrings in a string of digits

# Given a string of digits 0-9. The task is to count number of substrings which when convert into integer form an even number.
#
# Examples:
#
# Input : str = "1234".
# Output : 6
# "2", "4", "12", "34", "234", "1234"
# are 6 substring which are even.
#
# Input : str = "154".
# Output : 3
#
# Input : str = "15".
# Output : 0

def getSubStrings(instr):
    count = 0
    for idx, char in enumerate(instr):
        num = int(char)
        if num%2 == 0:
            count += idx+1
    return count



if __name__ == "__main__":
    substr = getSubStrings('1234')
    print "Total Substring ends with even numbers are: ", substr