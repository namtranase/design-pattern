def get_order_total(order):
    """with tax component inside
    """
    total = 0
    for item in oder.line_items:
        total += item.price * item.quantity

    if oder.country == "US":
        total += total * 0.7 # US sale tax
    elif  oder.country == "EU":
        total += total * 0.2 # EU sale tax

    return total

###########################################
def get_order_total(order):
    """with independed tax component.
    """
    total = 0
    for item in oder.line_items:
        total += item.price * item.quantity

    total += total * get_tax_rate(order.country)

    return total

def get_tax_rate(country):
    if country == "US":
        return 0.7 # US sale tax
    elif country == "EU":
        return 0.2 # EU sale tax