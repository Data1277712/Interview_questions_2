
#Write a Python function that takes a list of numbers and returns a new list containing the square of each number. 
However, if the input list contains any non-numeric values, the function should skip those values without raising an error. Assume the input list can contain integers, floats, and non-numeric values.

def square_numbers(nums):
    
   result=[]
   for i in nums:
        if isinstance(i,(int,float)):
             result.append(i**2)
        else:
             result.append(i)
   return result

nums = [1, 2, 'a', 3, 4.5, 'hello', 6] 
squared_list = square_numbers(nums)
print(squared_list)
