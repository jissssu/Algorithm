from itertools import combinations

L, C = map(int, input().split())
letters = input().split()
letters.sort()

vowels = set('aeiou')

for comb in combinations(letters, L):
    vowel_count = sum(1 for c in comb if c in vowels)
    consonant_count = L - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))
