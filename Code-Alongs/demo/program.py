import random




def dice(throws):
    outcomes = []
    diced_rolled = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for _ in range(throws):
        roll = random.randint(1, 6)
        outcomes.append(roll)
        diced_rolled[roll] += 1
    return diced_rolled

        

print(dice(100000))