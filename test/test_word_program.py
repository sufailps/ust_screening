import unittest
from src.word_program import check_count


class TestWordProgram(unittest.TestCase):
    def test_word_program(self):
        line="which is better python 2 or python 3"
        result=check_count(line)
        expected=[('2', 1),('3', 1),( 'better', 1), ('is', 1), ('or', 1), ('python', 2),( 'which', 1)]
        self.assertEqual(result,expected)

if __name__=="__main__":
    unittest.main()