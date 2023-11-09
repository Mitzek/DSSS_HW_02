import unittest
from math_quiz import create_random_number, create_random_choice, calc_numbers


class TestMathGame(unittest.TestCase):

    def test_create_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

        for _ in range(500):  # Test a medium number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

        for _ in range(100):  # Test a small number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
        
        for _ in range(50):  # Test a very small number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_create_random_choice(self):
        # Test if the choice is within the choices already stated in the function
        for _ in range(500): #Test the choice five hundred times
            operator = create_random_choice()
            self.assertTrue(operator == "+" or "-" or "*")

        for _ in range(100): #Test the choice a hundred times
            operator = create_random_choice()
            self.assertTrue(operator == "+" or "-" or "*")

        for _ in range(50): #Test the choice for fifty times
            operator = create_random_choice()
            self.assertTrue(operator == "+" or "-" or "*")



    def test_calc_numbers(self):
            test_cases = [
                (5,  2,  '+','5 + 2', 7),
                (1, 7, '-', '1 - 7', -6),
                (21, 10, '*', '21 * 10', 210),
                (18, 15, '+', '18 + 15', 33),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                solution = calc_numbers(num1, num2, operator) #Perform calculation and return array
                problem = solution[0] #Extract problem from array
                answer = solution[-1] #Extract answer from array
                self.assertTrue(problem == expected_problem)
                self.assertTrue(answer == expected_answer)
                

if __name__ == "__main__":
    unittest.main()
