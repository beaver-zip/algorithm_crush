def solution(participant, completion):
    dict = {p: 0 for p in participant}
    
    for p in participant:
        dict[p] += 1
    
    for c in completion:
        dict[c] -= 1
        if dict[c] == 0:
            del dict[c]
    
    for key in dict.keys():
        return key