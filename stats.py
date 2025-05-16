def count_words(path):
    with open(path) as f:
        temp = f.read()
    count = len(temp.split())
    return count


def count_char(path):
    with open(path) as file:
        text = file.read()
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"] 

def sort_shit(shit):
    return sorted(shit.items(), key=lambda item: item[1], reverse=True)

    