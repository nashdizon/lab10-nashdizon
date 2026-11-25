# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    
    # list ["2","1","+","3","*"] stack []
    # list ["1","+","3","*"] stack [2]
    # list ["+","3","*"] stack [2,1]
    # list ["3","*"] stack[3] <- 2+1=3
    # list ["*"] stack[3,3]
    # list[] stack[9] <- 3*3
    # returns whatever is now in stack 

    # pop out the first elements in the list
    # if it's a number, store it in the stack 
    # if it's an operator, use cases to perform the math with the two numbers in the stack
    # pop them out, assign them, and then perform the math
    # put the number back in the stack
    # go until theres no more items in the list
    stack = []
    # while (len(tokens) >= 1):
    for current_token in tokens:
        # current_token = tokens.pop(0)
        # print(stack)
        # print(f"current token = {current_token}")
        value = 0
        if current_token in {"+","-","*","/"}:
            right = stack.pop()
            left = stack.pop()
            if current_token == "+":
                value = left + right
                # print(f"adding")
            elif current_token == "-":
                value = left - right
                # print(f"subtracting")
            elif current_token == "*":
                value = left * right
                # print(f"multiplying")
            else:
                value = left / right
                # print(f"dividing")
            stack.append(value)
        else:
            stack.append(int(current_token))

    return stack[0]

        
def decode_string(s):
    # Outline:
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"``

    # string "3[a2[c]]", stack = [], newstring = "", current_number = 0
    # string "[a2[c]]", stack = [], newstring = "", current_number = 3
    # string "a2[c]]", stack = [("", 3)], newstring = "", current_number = 0
    # string "2[c]]", stack = [("", 3)], newstring = "a", current_number = 0
    # string "[c]]", stack = [("", 3)], newstring = "a", current_number = 2
    # string "c]]", stack = [("", 3),("a",2)], newstring = "", current_number = 0
    # string "]]", stack = [("", 3),("a",2)], newstring = "c", current_number = 0
    # string "]", stack = [("", 3)], newstring = "a" + 2*"new_string" = "acc", current_number = 0
    # string "" , stack = [], newstring = "" + 3*"new_string" == "accaccacc", current_number = 0

    # go through each part of the string, if the number is next to a bracket, push it to stack
    # keep going and push to strings
    stack = []
    current_number = 0
    newstring = ""
    #while (s != ""):
    for char in s:
        #char = s.pop(0)
        if char.isdigit(): # if its a number, set the current number to that
            current_number = current_number * 10 + int(char) # Gemini suggested to do current numebr * 10
        elif char == "[": # if its a bracket store into stack to use later
            stack.append((newstring,current_number))
            current_number = 0
            newstring = ""
        elif char == "]": # if it's an ending bracket, start doing the math
            string, number = stack.pop()
            newstring = string + newstring*number
        else:
            newstring += char # if its a character, add it to the current string
    return newstring

    # gemini suggested things such as not using (s != "") and instead just looping through, since you cant pop a letter ouf of string
        
            
        


def daily_temperatures(temps):
    # Outline:

    # create a new list for the list of days needed to wait based on list of temps
    # set them all to 0 by default

    # the stack stores the indices to track days that still need it 
    # based on the hint provided

    # check the item in the stack and use it to compare if the current day is bigger than the last day in the stack
    # if so, take it out and use it to calculate how many days you need to wait, and then set it to the day in the corresponding index.
    # add that day to the stack since it's now in the waiting list

    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    answers = [0] * len(temps)

    stack = []

    for i, temp in enumerate(temps):
        while len(stack) > 0 and temp > temps[stack[-1]]:
            index = stack.pop()
            answers[index] = i - index
        stack.append(i)

    return answers



def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60])) # returns [1, 1, 1, 0]

if __name__ == "__main__":
    main()
