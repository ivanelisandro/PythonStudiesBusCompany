def discounts(x, y):
    fifty_percent = 0.5
    discount = 1 - (y / x)
    assert discount > fifty_percent
    return "I will buy it!"
