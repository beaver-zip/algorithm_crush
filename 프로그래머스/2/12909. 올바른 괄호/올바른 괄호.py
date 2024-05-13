# def solution(s):
#     stack = [0] * len(s)
#     top = -1
#     for c in s:
#         if c == '(':
#             top += 1
#             stack.append(c)
#         elif c == ')':
#             if top == -1:
#                 return False
#             stack[top] = None
#             top -= 1
#     return top == -1

def solution(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
