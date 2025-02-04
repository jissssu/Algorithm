def solution(myString, pat):
    return int(pat.lower() in myString.replace("A", 'b').replace("B", 'a'))
