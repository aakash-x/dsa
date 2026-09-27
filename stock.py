
def max_profit(prices):
    """
    Calculate the maximum profit from a list of stock prices.
    
    :param prices: List of stock prices where prices[i] is the price of a given stock on day i.
    :return: Maximum profit that can be achieved by buying and selling once.
    """
    if not prices:
        return 0
    buy = float('inf')
    sell_ans = None
    profit = 0
    for sell in prices:
        buy = min(buy, sell)
        if profit < sell - buy:
            profit = sell - buy
            sell_ans = sell
    return (buy, sell_ans)

print(max_profit([7, 15,1,4,5,6,3]))