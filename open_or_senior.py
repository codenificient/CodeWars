def open_or_senior(data):
    result = []
    for age, handi in data:
        if age >= 55 and handi > 7:
            result.append("Senior")
        else:
            result.append("Open")   
    return result