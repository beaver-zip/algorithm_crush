def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    new = ''
    
    now = ''
    for c in s:
        if c.isdigit():
            new += c
            continue
        now += c
        if now in arr:
            new += str(arr.index(now))
            now = ''
    return int(new)
            