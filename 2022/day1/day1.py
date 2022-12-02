input = "2022/day1/input.txt"
smallInput = "2022/day1/smalInput.txt"

with open(smallInput) as f:
    data = sorted(sum(int(line) for line in group.split()) for group in f.read().split('\n\n'))

print(data[-1])
print(sum(data[-3:]))

