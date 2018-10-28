import random

def toss():
    if random.random() < 2 / 3:
        return 0
    else:
        return 1

def get_index(probability):
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    r = random.random()
    for index, sp in enumerate(sum_probability):
        if r <= sp:
            return index
    return len(probability) - 1

def dispense():
    dollar_bills = [5, 10, 20, 50]
    probability = [1 / 6, 1 / 6, 1 / 3, 1 / 3]
    bill_index = get_index(probability)
    return dollar_bills[bill_index]
