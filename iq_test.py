def iq_test(numbers):
    evens = []
    odds = []
    idx = -1
    for number in numbers:
        num = int(number)
        if num % 2 == 0:
            evens.append(number)
        else:
            odds.append(num)
    if len(evens) > len(odds):
        idx = numbers.index(odds[0])
    else:
        idx = numbers.index(evens[0])
    return idx + 1