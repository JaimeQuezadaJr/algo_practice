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

# def left_negative(arr):
#     n = len(arr)
#     j = 0
#     for i in range(0, n):
#         if arr[i] < 0:
#             temp = arr[i]
#             arr[i]= arr[j]
#             arr[j] = temp
#             j = j + 1
#     return arr

# print(left_negative([-12,11,-13,-5,6,-7,5,-3,-6]))

# def move_to_front(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] > 0 :
#             arr.insert(arr[i-1], arr[i])
#             arr.pop(i)

#     return arr

# print(move_to_front([-1,2,-3,4, 7]))


# def majority(arr):
#     n = len(arr)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 count +=1
#         if count > n // 2:
#             return arr[i]
#     return -1

# print(majority([1,1,2,1,3,5,1]))


# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n):
#             if nums[i] + nums[j] == target and i != j:
#                 return i , j
            
# print(two_sum([3,2,4], 6))

# def palindrome(x):
#     new_arr=[]
#     for i in str(x):
#         new_arr.append(i)
#     if new_arr == new_arr[::-1]:
#         return True
#     else:
#         return False    
# print(palindrome(121))

def romanToInt(numeral):
    roman = {'I': 1,'V': 5,'X':10,'L':50,'C':100,'D' :500,'M' :1000 }
    count = 0
    new_arr = []
    for char in numeral:
        for i in roman.keys():
            if i < char:
                count += 1
            elif i == char:
                count += roman[i]
                new_arr.append()
    return count 
    

print(romanToInt('XIV'))

# def longestCommonPrefix(arr):
#     min_s = min(arr)
#     max_s = max(arr)
#     if not min_s:
#         return ""
#     for i in range(len(min_s)):
#         if max_s[i] != min_s[i]:
#             return max_s[:i]
#     return min_s[:]


# print(longestCommonPrefix(["flower", "flow", "flight"]))

# l = [1,2,3]
# m = l[:0]

# print(m)

# m = ["flower", "flow"]
# for i in str(m):
#     print(i)

# def isValid(s:str):
#     openers = ['(', '[', '{']
#     closers = [')', ']', '}']
#     stack = []
#     for char in s:
#         if char in openers:
#             stack.append(char)
#         elif not stack or openers.index(stack[-1]) != closers.index(char):
#             return False
#         else:
#             stack.pop()
#     return not stack


# print(isValid('(([])}'))

# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# def mergeTwoLists(list1:ListNode, list2:ListNode):
#     dummy = ListNode()
#     curr = dummy
#     while list1 and list2:
#         if list1.val < list2.val:
#             curr.next = list1
#             curr = list1
#             list1 = list1.next
#         else:
#             curr.next = list2
#             curr = list2
#             list2 = list2.next
#     if list1:
#         curr.next = list1 
#     else:
#         curr.next = list2
#     return dummy.next


# dumm1 = ListNode([1,2,4])
# dumm2 = ListNode([1,3,4])
# print(mergeTwoLists(dumm1, dumm2))

# remove duplicates not in place
# def removeDuplicates(nums):
#     n = len(nums)
#     nums_set = []
#     new_arr = []

#     for i in nums:
#         if i in nums_set:
#             new_arr.append(i)
#         else:
#             nums_set.append(i)
#     for i in range(len(new_arr)):
#         new_arr[i]= 0
#     k = len(nums_set)
#     return nums_set + new_arr, k

# print(removeDuplicates([1,1,1,2,2,3,4,4]))


# remove duplicates in place

# def removeDuplicates(nums):
#     n = len(nums)
#     nums_set = set()

#     for i in range(n):
#         print(i)
#         if nums[i] in nums_set:
#             nums[i] = 0
#         else:
#             nums_set.add(nums[i])
#             print("added to set", i)
#     nums.sort()
#     return nums

# print(removeDuplicates([1,1,1,2,2,3,4,4,4]))

# def removeDuplicates(nums):
#     j = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]:
#             nums[j] = nums[i]
#             j+=1
#     return nums,j

# print(removeDuplicates([0,1,1,2,2,3,4,4]))

# def removeElement(nums, val):
#     n = len(nums)
#     j = 0
#     for i in range(n):
#         if nums[i] != val:
#             nums[j] = nums[i]
#             j +=1
#     return nums, j

# print(removeElement([3,2,2,3], 3))

# arr = [1,2,3,4]

# arr[3], arr[0]= arr[0], arr[3]

# print(arr)

