from collections import Counter

def solution(s):
    counter = Counter(s.lower())
    print(counter)
    if counter['p'] == counter['y']:
    # if counter['p'] + counter['P'] == counter['y'] + counter['Y']:
        return True
    else:
        return False