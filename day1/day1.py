#f = open("C:/Users/gerha/Desktop/aoc 2021/day1/input.txt", "r")
#lines = [int(e) for e in set(f.read().split("\n"))]

from typing import List


lines = []
with open("C:/Users/gerha/Desktop/aoc 2021/day1/input.txt") as f:
    lines = f.readlines()
    
def partOne(lines):
    cont = 0
    for i in range(len(lines)):
        if i >= 1:
            if int(lines[i]) > int(lines[i-1]):
                cont += 1
    print(" Ergebnis ist " +  str(cont))
    
def partTow(list):
    cont = 0
    summedUp = []
    for i in range(len(list)):
        if i >= 2:
            summedUp.append(int(list[i]) + int(lines[i-1]) + int(lines[i-2]))
    partOne(summedUp)

print("part 1 Lösung ")
partOne(lines)
print("part 2 Lösung ")
partTow(lines)