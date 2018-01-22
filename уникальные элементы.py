def num_unique_numbers(values):
    counter = 0
    for i in range(len(values)):
        if i == values.index(values[i]):
            counter+=1
    return counter