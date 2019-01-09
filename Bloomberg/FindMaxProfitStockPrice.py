# find maximum profit by buying-selling stock only once

import sys

def findMaxProfit(pricelst):
    maxprofit = sys.maxint * -1
    minprice = pricelst[0]
    buyprice, sellprice = -1, -1
    for idx, price in enumerate(pricelst):
        if idx == 0:
            continue

        profit = price - minprice

        if profit > maxprofit:
            maxprofit = profit
            buyprice = minprice
            sellprice = price

        if price < minprice:
            minprice = price



    print "Bought at price ${0} and Sold at price ${1} and earned profit of ${2}".format(buyprice, sellprice, maxprofit)


if __name__ == "__main__":
    # price of stock through out the day
    findMaxProfit([5, 9, 6, 1, 4, 3, 4, 5, 11, 2, 4, 5, 10])