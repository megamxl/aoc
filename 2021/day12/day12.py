from itertools import product,starmap


with open("day12\input.txt") as puzzle_input:
    puzzle_input = [[int(nums) for nums in line.rstrip("\n")] for line in puzzle_input.readlines()]
    #print(puzzle_input)

        
def partOne(lines):
    pass    

def partTow(lines):
    pass
        
if __name__ == '__main__':
    print(f"P1 {partOne(puzzle_input)}")
    print(f"P2 {partTow(puzzle_input)}")
