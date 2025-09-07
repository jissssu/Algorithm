X = int(input())

diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

if diagonal % 2 == 0:
    numerator = X
    denominator = diagonal - X + 1
else:
  
    numerator = diagonal - X + 1
    denominator = X

print(f"{numerator}/{denominator}")
