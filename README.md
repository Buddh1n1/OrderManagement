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
