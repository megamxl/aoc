f = open("C:/Users/gerha/Desktop/aoc 2021/day1/input.txt", "r")
entries = [int(e) for e in set(f.read().split("\n"))]

for e in entries:
    print(e)

print("git")
