

items_list = []
prev_transaction_list = []
# total = 0

def add_item(item, price, quanity=3):
    
    purchase = {"item": item, "price": price, "quanity": quanity}
    items_list.extend([item] * quanity)
    total = price * quanity
    prev_transaction_list.append(purchase)
    return items_list
    
print(add_item())