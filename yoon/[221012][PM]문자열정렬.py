# sorted는 list로 안감싸도 알아서 list로 반환해줌

def solution(s):
    answer = sorted(s,reverse=True)
    return "".join(answer)