# http://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/
#
# Find Itinerary from a given list of tickets
# Given a list of tickets, find itinerary in order using the given list.
#
# Example:
#
# Input:
# "Chennai" -> "Banglore"
# "Bombay" -> "Delhi"
# "Goa"    -> "Chennai"
# "Delhi"  -> "Goa"
#
# Output:
# Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,


def findItinerary(lst):
    hashmap = {val[0]: val[1] for val in lst}

    # starting point is not val of any key in original map, so we can create revmap and look for country which
    # does not exit in keyset
    revhashmap = {val[1]: val[0] for val in lst}

    fromplace = None
    for key, val in hashmap.iteritems():
        if not revhashmap.get(key, False):
            fromplace = key
            break

    toplace = hashmap.get(fromplace, None)
    while toplace:
        print "{}->{}".format(fromplace, toplace)
        fromplace = toplace
        toplace = hashmap.get(fromplace, None)

if __name__ == "__main__":
    lst = [("Chennai", "Banglore"), ("Bombay", "Delhi"), ("Goa", "Chennai"), ("Delhi", "Goa")]
    findItinerary(lst)