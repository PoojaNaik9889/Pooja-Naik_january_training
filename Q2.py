#Order History Tracker (Mutable Parameter)
# store order ids

def add_order(order_id, orders=None):
    if orders is None:
        orders = []
    orders.append(order_id)
    return orders

print(add_order(101))
print(add_order(102))
