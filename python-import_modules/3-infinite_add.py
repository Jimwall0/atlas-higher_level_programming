#!/usr/bin/python3
def main():
    import sys
    total = len(sys.argv)
    sum = 0
    for n in range (1, total):
        sum += int(sys.argv[n])
    print(f"{sum}")


if __name__ == "__main__":
    main()
