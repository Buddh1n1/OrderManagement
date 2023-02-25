Calculates best possible limit order prices and volumes at regular steps to maximize gains and take profits.

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

How to sell 1000000 tokens with 6 orders from start price 1 to end price 100 with 2-growing payout from step to step

step 0 - price: 1.0000000 - volume: 273460.2 - payout: 273460.2

step 1 - price: 2.5118864 - volume: 217732.9 - payout: 546920.4

step 2 - price: 6.3095734 - volume: 173362.1 - payout: 1093840.8

step 3 - price: 15.8489319 - volume: 138033.4 - payout: 2187681.6

step 4 - price: 39.8107171 - volume: 109904.2 - payout: 4375363.1

step 5 - price: 100.0000000 - volume: 87507.3 - payout: 8750726.3

total payout: 17227992.4

average payout per share: 17.2