import random
def create_random_number(min, max):
    """
    (int, int) --> (int)
    Generates a random integer within the given values: min and max.
    >>>create_random_integer(4, 8)
    5
    """    
    return random.randint(min, max) #Return the random integer

def create_random_choice():
    """
    (none) --> (operator)
    Generates a random choice of operator from '+', '-','*'
    >>>create_random_choice()
    *
    """
    return random.choice(['+', '-', '*']) #Return one of the operator

def calc_numbers(num1, num2, op):
    """
    (int, int, char) --> string, int
    Generate a number based on the choice of operator and calculate the given numbers
    >>>calc_number(4, 8, +)
    12
    """
    result = f"{num1} {op} {num2}" #Print the calculation
    if op == '+': num = num1 + num2 #Add if the op is +
    elif op == '-': num = num1 - num2 #Sub if the op is - 
    else: num = num1 * num2 #Multiply if the op is *
    return result, num #Return the string and calculated number

def math_quiz():
    """
    (none) --> string
    Begins the quiz, Takes a number as user input, compares the number to already calculated number and outputs score.
    >>>math_quiz()
    Welcome to the Math Quiz Game!
    You will be presented with math problems, and you need to provide the correct answers.
    Question: 3 + 3
    Your answer: 6
    Correct! You earned a point.
    Question: 4 + 5
    2
    Wrong answer. The correct answer is 9
    Game over! Your score is: 0.318

    >>>math_quiz()
    Welcome to the Math Quiz Game!
    You will be presented with math problems, and you need to provide the correct answers.
    Question: 3 + 3
    Your answer: a
    Invalid Input! Input numbers only
    Your answer: 
    ...
    """
    score = 0
    total_questions = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions): #Start a loop for questions to repeat incase of right answers
        num1 = create_random_number(1, 10); num2 = create_random_number(1, 5); 
        op = create_random_choice() #Generate random numbers and operator

        PROBLEM, ANSWER = calc_numbers(num1, num2, op) #Create question and its answer
        print(f"\nQuestion: {PROBLEM}") #Print question
        try:
            user_answer = input("Your answer: ") #Input user number.
            user_answer = int(user_answer) #Parse to int.
        except:
            print("Invalid Input! Input numbers only") #Handle error if the input is a non-integer.

        if user_answer == ANSWER:
            print("Correct! You earned a point.") 
            score += -(-1)  #Increase point and give new question
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.") #Return the correct answer

    print(f"\nGame over! Your score is: {score}/{total_questions}") #Return the total score for user and end quiz.

if __name__ == "__main__":
    math_quiz() #Call the quiz function in main.
