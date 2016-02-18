# find maximum profit by buying-selling stock only once

def findMaxProfit(pricelst):
    maxprofit = -1
    minprice, maxprice = -1, -1
    buyprice, sellprice = -1, -1
    for idx, price in enumerate(pricelst):
        if idx == 0:
            minprice, maxprice = price, price

        if price > maxprice:
            maxprice = price
        elif price < minprice:
            minprice = price

        profit = price - minprice
        if profit > maxprofit:
            maxprofit = profit
            buyprice = minprice
            sellprice = price


    print "Bought at price ${0} and Sold at price ${1} and earned profit of ${2}".format(buyprice, sellprice, maxprofit)


if __name__ == "__main__":
    # price of stock through out the day
    findMaxProfit([5, 9, 6, 1, 4, 3, 4, 5, 1, 2, 4, 5, 10])