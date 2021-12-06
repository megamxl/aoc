
with open("day6\input.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(",") for line in puzzle_input.readlines()]
    puzzle_input = [[int(n) for n in l] for l in puzzle_input]
    puzzle_input2 = []
    print(type(puzzle_input))
    
# with open('day6\input.txt') as f:
#     puzzle_input = f.readlines()
#     puzzle_input = puzzle_input.split()
# print(puzzle_input)

    
def partOne(lines):
    lines2 = lines
    for t in range(80): 
        for i in range(len(lines[0])):
            if lines[0][i] == 0:
                lines[0][i] = 6
                lines[0].append(8)
            else:
                lines[0][i] -= 1
        #print(lines)
        print(t)
    print(len(lines[len(lines)-1]))
                

def partTow(lines):
    with open("day6\input.txt", "r") as file:
        fish_dict = {i: 0 for i in range(9)}
        for fish in file.readline().split(","):
            fish_dict[int(fish)] += 1
        for day in range(256):
            fish_0 = fish_dict[0]
            for i in range(1, 9):
                fish_dict[i-1] = fish_dict[i]
            fish_dict[8] = fish_0
            fish_dict[6] += fish_0
        print(sum(fish_dict.values()))
    

if __name__ == '__main__':
    partOne(puzzle_input)
    partTow(puzzle_input)
    