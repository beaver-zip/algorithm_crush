def solution(s):
    new = ''
    for word in s.split(' '): 
        for i in range(len(word)):
            if i % 2 == 0:
                new += word[i].upper()
            else:
                new += word[i].lower()
        new += ' '
    return new[:-1]
