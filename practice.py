import unittest


class Solution:
    def convert(self, hours, minutes):
        c1 = hours * 3600
        c2 = minutes * 60
        return c1 + c2


class TestValue(unittest.TestCase):
    def test(self):
        example = Solution()
        self.assertEqual(example.convert(1,0), 3600)



class Result:
    def check_string(self,word):
        if type(word) == str:
            return True
        else:
            return False
        
class TestString(unittest.TestCase):
    def test_word(self):
        example = Result()
        self.assertEqual(example.check_string(12), True)


if __name__ == '__main__':
    unittest.main()
