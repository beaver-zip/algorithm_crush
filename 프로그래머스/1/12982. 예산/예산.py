def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget == 0: return i+1
        elif budget < 0: return i
    return i+1
        
# i=0; 9-1=8
# i=1; 8-2=6
# i=2; 6-3=3
# i=3; 6-4=-1

# i   d[i]  budget
# 초기;      10
# i=0; -2 = 8
# i=1; -2 = 6 
# i=2; -3 = 3
# i=3; -3 = 0

# [2, 2, 3], 10
        
        