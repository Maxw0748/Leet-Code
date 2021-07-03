def maxProfit(prices):
#base Case where there is only one price where there wouldnt be any change in price since hte buys and sell prices would be the same
    if len(prices) == 0:
        return 0
    #this is the set case where the first is initilied as what we start with, this is hte general case
    minimum = prices[0]
    result = 0
    #iterating between all the cases
    for i in range(len(prices)):
        #Check the new price is smaller then the the minimum and store whichever one is smaller
        if prices[i] > minimum:
            result = max(result, prices[i] - minimum)
        else:
            minimum = prices[i]
        #returning the results  
    return result

print(maxProfit([7,1,5,3,6,4]))