def get_net_price(price,tax_rate,discount=0):
    return (price * tax_rate -discount) + price

def get_tax(price, tax_rate=0):
    return price * tax_rate

