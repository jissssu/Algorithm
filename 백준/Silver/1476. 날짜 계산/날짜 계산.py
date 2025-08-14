import sys

def main():
    data = sys.stdin.read().strip().split()
    E, S, M = map(int, data)

    year = E
    while True:
        if (year - S) % 28 == 0 and (year - M) % 19 == 0:
            print(year)
            break
        year += 15  # E 주기가 15이므로 15씩 증가

if __name__ == "__main__":
    main()
