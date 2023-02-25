Calculates best possible limit order prices and volumes to maximize gains and take profits.

Set 
- startprice: to the minimum price you are willing to sell for
- endprice: to the maximum price you are willing to sell for
- n: the amount of tokens/stocks in your portfolio
- M: the amount of orders between min and max price
- c: determines the jump in profit between orders. 
A value of 1 means you take the same profit at each order. 
A value of 2 means you take double the profit from order to order.
The higher the value, the bigger your overall profit, but the less profit you will have taken on the way up.

Example:

How to sell 1000000 tokens with 5 orders from start price 1 to end price 100 with 1.5-growing payout from step to step

step 0 - price: 1.0000000 - volume: 538591.9 - payout: 538591.9

step 1 - price: 3.1622777 - volume: 255476.5 - payout: 807887.8

step 2 - price: 10.0000000 - volume: 121183.2 - payout: 1211831.7

step 3 - price: 31.6227766 - volume: 57482.2 - payout: 1817747.5

step 4 - price: 100.0000000 - volume: 27266.2 - payout: 2726621.2

total payout: 7102680.0

average payout per share: 7.1