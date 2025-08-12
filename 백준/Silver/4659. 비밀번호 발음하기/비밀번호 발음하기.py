def is_acceptable(pw: str) -> bool:
    vowels = set("aeiou")
    
    # 규칙 1: 모음 포함 여부
    if not any(ch in vowels for ch in pw):
        return False
    
    # 규칙 2: 3연속 모음/자음 금지
    for i in range(len(pw) - 2):
        if (pw[i] in vowels and pw[i+1] in vowels and pw[i+2] in vowels) or \
           (pw[i] not in vowels and pw[i+1] not in vowels and pw[i+2] not in vowels):
            return False
    
    # 규칙 3: 같은 글자 2번 연속 금지 (ee, oo 예외)
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1] and pw[i] not in ('e', 'o'):
            return False
    
    return True


while True:
    pw = input().strip()
    if pw == "end":
        break
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
