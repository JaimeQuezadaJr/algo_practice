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
# def reverse_arr(arr):
#     left = 0
#     right = len(arr) -1
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left = left +1
#         right = right - 1
#     return arr
# print(reverse_arr([1,2,3,4,5,6,7,8]))

# def rotate_arr(arr):
#     temp = arr[len(arr)-1]
#     arr.pop()
#     arr.insert(0,temp)
#     return arr

# print(rotate_arr([1,2,3,4,5]))

# def contain_duplicate(nums):
#     s = set()
#     for x in nums:
#         if x in s:
#             return True
#         else:
#             s.add(x)
#     return False

# def remove_duplicate(nums):
#     s = set(nums)
#     nums = list(s)
#     return nums
# print(remove_duplicate([1,2,3,1,6]))
    
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 print("swapped", i, j)
#         print(i,j)
#         print(arr)
#     return arr

# print(bubble_sort([15,9,3,7,1,11]))

# def bubble_sort(arr):
#     n = len(arr)
#     flag = True
#     while flag:
#         flag = False
#         for i in range(1,n):
#             if arr[i-1] > arr[i]:
#                 flag = True
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#         print(flag, i)
#     return arr


# print(bubble_sort([15,9,3,7,1,11]))

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         for j in range(i, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#             else:
#                 break
#     return arr
# print(insertion_sort([15,9,3,7,1,11]))    

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# print(selection_sort([15,9,3,7,1,11])) 

# def contain_duplicate(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] == nums[j]:
#                 return True
#     return False





# def tri_recursion(k):
#     if k > 0:
#         result = k * tri_recursion(k-1)
#         print(result)
#     else:
#         result = 1
#     return result

# tri_recursion(5)

# def duplicates(arr):
#     new_arr = set()
#     d = []
#     for i in arr:
#         if i in new_arr:
#             d.append(i)
#         else:
#             new_arr.add(i)    
#     return d

# print(duplicates([1,2,3,1,6,6]))

# def occurences(arr, x):
#     o = 0
#     for i in arr:
#         if i == x:
#             o +=1
#     return o

# print(occurences([1,1,2,2,2,2,3], 2))

def left_negative(arr):
    n = len(arr)
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i]= arr[j]
            arr[j] = temp
            j = j + 1
    return arr

print(left_negative([-12,11,-13,-5,6,-7,5,-3,-6]))