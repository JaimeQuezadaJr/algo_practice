import unittest


# class Solution:
#     def convert(self, hours, minutes):
#         c1 = hours * 3600
#         c2 = minutes * 60
#         return c1 + c2


# class TestValue(unittest.TestCase):
#     def test(self):
#         example = Solution()
#         self.assertEqual(example.convert(1,0), 3600)



# class Result:
#     def check_string(self,word):
#         if type(word) == str:
#             return True
#         else:
#             return False
        
# class TestString(unittest.TestCase):
#     def test_word(self):
#         example = Result()
#         self.assertEqual(example.check_string(12), True)

# class Solution:
#     def addUp(self, num):
#         count = 0
#         for i in range(1, num+1):
#             count = count + i
#         return count
        
    
# class TestValue(unittest.TestCase):
#     def test(self):
#         example = Solution()
#         self.assertEqual(example.addUp(13), 91)    

# class Solution:
def min_max(arr: list):
    min_value = arr[0]
    max_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
    for i in arr:
        if i > max_value:
            max_value = i
    return list([min_value, max_value])

print(min_max([6,4,5,9,2]))     

# class TestValue(unittest.TestCase):
#     def test(self):
#         example = Solution()
#         self.assertEqual(example.matchHouses(87), 436)  



# if __name__ == '__main__':
#     unittest.main()

# def tri_recursion(k):
#     if k > 0:
#         result = k * tri_recursion(k-1)
#         print(result)
#     else:
#         result = 1
#     return result

# tri_recursion(5)