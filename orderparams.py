s = 1         #startprice
t = 100       #endprice
n = 1000000   #token amount
M = 5         #ordercount
c = 1.5       #factor between payouts

m = M-1
p = [0]*(m+1)
v = [0]*(m+1)
k = (t/s)**(1/m)
v0 = n * (1-c/k) / (1-(c/k)**(m+1))
print(f'How to sell {n} tokens with {M} orders from start price {s} to end price {t} with {c}-growing payout from step to step')
for i in range(M):
    p[i] = s * (t/s)**(i/m)
    v[i] = v0 * (c/k)**i
    print(f'step {i} - price: {p[i]:.7f} - volume: {v[i]:.1f} - payout: {p[i]*v[i]:.1f}')

total = sum(p[i]*v[i] for i in range(M))
print(f'total payout: {total:.1f}')
print(f'average payout per share: {total/n:.1f}')