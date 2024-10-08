import unittest
from src.password_program import passvalidate

class TestPasswordProgram(unittest.TestCase):
    def test_passvalidate(self):
        passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
        actual=passvalidate(passwords)
        expected="aF145#"
        self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()