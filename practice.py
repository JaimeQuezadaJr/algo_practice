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
#     def min_max(self, arr: list):
#         min_value = arr[0]
#         max_value = arr[0]
#         for i in arr:
#             if i < min_value:
#                 min_value = i
#         for i in arr:
#             if i > max_value:
#                 max_value = i
#         return list([min_value, max_value])
 

# class TestValue(unittest.TestCase):
#     def test(self):
#         example = Solution()
#         self.assertEqual(example.min_max([4,2,7,10,6]), [2,10])  



# if __name__ == '__main__':
#     unittest.main()
def reverse_arr(arr):
    left = 0
    right = len(arr) -1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left +1
        right = right - 1
    return arr
print(reverse_arr([1,2,3,4]))

# def tri_recursion(k):
#     if k > 0:
#         result = k * tri_recursion(k-1)
#         print(result)
#     else:
#         result = 1
#     return result

# tri_recursion(5)