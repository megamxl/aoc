
input = "2022/day2/input.txt"
smallInput = "2022/day2/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]

#Defing metrics
#their rock
ELF_ROCK = 'A'
ELF_PAPER = 'B'
ELF_SCISSORS = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = 'Z'

WIN_BONUS = 6
DRAW_BONUS = 3
ROCK_BONUS = 1
PAPER_BONUS = 2
SCISSOR_Bonus = 3

def getResults(option):
    if option == ELF_ROCK:
        return(MY_PAPER,MY_ROCK,MY_SCISSORS)
    elif option == ELF_PAPER:
        return(MY_SCISSORS,MY_PAPER,MY_ROCK)
    elif option == ELF_SCISSORS:
        return(MY_ROCK,MY_SCISSORS,MY_PAPER)

   
def calcIt(puzzel, sum): 
    for moves in puzzel:
        if moves[0] == ELF_ROCK:
            #draw
            if moves[1] == MY_ROCK:
                sum += ROCK_BONUS + DRAW_BONUS
            #win
            elif moves[1] == MY_PAPER:
                sum += PAPER_BONUS + WIN_BONUS
            #lose
            else:
                sum += SCISSOR_Bonus
        elif moves[0] == ELF_PAPER:
            #draw
            if moves[1] == MY_PAPER:
                sum += PAPER_BONUS + DRAW_BONUS
            #lose
            elif moves[1] == MY_ROCK:
                sum += ROCK_BONUS
            #win
            else:
                sum += SCISSOR_Bonus +WIN_BONUS
        elif moves[0] == ELF_SCISSORS:
            #draw
            if moves[1] == MY_SCISSORS:
                sum += SCISSOR_Bonus + DRAW_BONUS
            #lose
            elif moves[1] == MY_PAPER:
                sum += PAPER_BONUS
            #win
            else:
                sum += ROCK_BONUS +WIN_BONUS    
    return sum  

listi = []

for moves in testCase:
    if moves[1] == MY_ROCK:
        listi.append([moves[0], getResults(moves[0])[2]])
    elif moves[1] == MY_PAPER:
        listi.append([moves[0], getResults(moves[0])[1]])
    elif moves[1] == MY_SCISSORS:
        listi.append([moves[0], getResults(moves[0])[0]])
        

print(f'challange 1 {calcIt(testCase,0)}')
print(f'challange 2 {calcIt(listi,0)}')