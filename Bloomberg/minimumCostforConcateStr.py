# http://www.careercup.com/question?id=5634291264389120

# There's a function that concatenates two strings and returns the length of the resultant string. When called upon a series of strings how do we minimize the cost of using this function. Let's say we have 3 strings, A= "abc", B="def", C = "gh".
# Now cost of merging AB = 6 and cost of merging the resultant string with C is 8. Thus the total cost is 6 + 8 = 14. However, if we merge A and C, then the cost is 5 and then merge B with this, the cost is 8, so the total cost is 13.
# Find an algorithm that minimizes the cost of adding such a series of strings.

totalcost = 0
class Queue:

    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)
        self.items.sort()
        print "Items: ", self.items

    def popFirst(self):
        return self.items.pop(0)

    def popLast(self):
        return self.items.pop()

    def peekFirst(self):
        return self.items[0]

    def peekLast(self):
        return self.items[len(self.items)-1]

    def __len__(self):
        return len(self.items)


def calculateCost(lst):
    global totalcost
    # here we should use sophisticated sort ex: quicksort or merge sort
    lst.sort()
    print lst
    queue = Queue()
    idx = 0
    while idx < len(lst):
        if idx == 0:
            concatecost = lst[0] + lst[1]
            idx += 2
            queue.push(concatecost)
            print "Adding cost: ", totalcost, concatecost
            totalcost += concatecost

            # qidx +=1
        else:
            currlstval = lst[idx]
            if queue.peekFirst() < currlstval:
                firstval = queue.popFirst()
                if queue.peekFirst() < currlstval:
                    concatecost = firstval + queue.popFirst()
                    queue.push(concatecost)
                else:
                    concatecost = firstval + currlstval
                    idx += 1
                    queue.push(concatecost)
            else:
                # go to next val
                idx += 1
                if idx >= len(lst) or queue.peekFirst() < lst[idx]:
                    concatecost = currlstval + queue.popFirst()
                    queue.push(concatecost)
                else:
                    concatecost = currlstval + lst[idx]
                    queue.push(concatecost)
                    idx += 1
            print "Adding cost: ", totalcost, concatecost
            totalcost += concatecost

    while len(queue) > 1:
        concatecost = queue.popFirst() + queue.popFirst()
        print "Adding cost: ", totalcost, concatecost
        totalcost += concatecost
        queue.push(concatecost)

    return totalcost



if __name__ == "__main__":
    lst = ['abc', 'def', 'gh']
    print calculateCost([len(val) for val in lst])