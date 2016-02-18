# http://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/

# Python program recursively print all sentences that can be
# formed from list of word lists
R = 3
C = 3

# A recursive function to print all possible sentences that can
# be formed from a list of word list
def printUtil(arr, m, n, output):

    # Add current word to output array
    output[m] = arr[m][n]

    # If this is last word of current output sentence, then print
    # the output sentence
    if m==R-1:
        for i in xrange(R):
            print output[i] + " ",
        print "\n",
        return

    # Recur for next row
    for i in xrange(C):
        if arr[m+1][i] != "":
            printUtil(arr, m+1, i, output)

# A wrapper over printUtil
def printf(arr):

    # Create an array to store sentence
    output = [""] * R

    # Consider all words for first row as starting
    #  points and print all sentences
    for i in xrange(C):
        if arr[0][i] != "":
            printUtil(arr, 0, i, output)

# Driver program
arr = [ ["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]
printf(arr)