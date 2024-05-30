def solution(nums):
    dict = {num: 0 for num in nums}

    if len(dict) > len(nums)//2:
        return len(nums)//2
    return len(dict)