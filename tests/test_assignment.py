import unittest

class TestControlStructures(unittest.TestCase):

    def test_while_loop(self):
        result = []
        number = 0
        while number <= 20:
            if number == 18:
                break
            if number % 2 == 0:
                result.append(number)
            number += 2
        self.assertEqual(result, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_for_loop_continue(self):
        result = []
        for num in range(1, 16):
            if num % 3 == 0:
                continue
            result.append(num)
        expected_output = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]
        self.assertEqual(result, expected_output)

    def test_if_else(self):
        test_cases = {
            -5: "Negative",
            0: "Zero",
            7: "Positive"
        }

        for num, expected in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(self.run_if_else(num), expected)
    
    def run_if_else(self, num):
        if num < 0:
            return "Negative"
        elif num == 0:
            return "Zero"
        else:
            return "Positive"
              
                
        

    def test_nested_loops(self):
        expected_output = [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],
            [4, 8, 12, 16, 20],
            [5, 10, 15, 20, 25]
        ]
        self.assertEqual(self.run_multiplication_table(5), expected_output)

    def run_multiplication_table(self, size):
        table = []
        for i in range(1, size + 1):
            row = []
            for j in range(1, size + 1):
                row.append(i * j)
            table.append(row)
        return table
        
            

if __name__ == "__main__":
    unittest.main()




   
   

    


 