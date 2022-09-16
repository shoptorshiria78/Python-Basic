import pricing
price = 200
tax_rate = 0.075
discount = 5
net_price= pricing.get_net_price(
    price,
    tax_rate,
    discount
)

print(net_price)

net_tax = pricing.get_tax(
    price,
    tax_rate
)

print(net_tax)