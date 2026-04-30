#Task 1
def smallest_number(a, b, c):
    smallest_num = a
    if(smallest_num > b):
        smallest_num = b
    if(smallest_num > c):
        smallest_num = c
    return smallest_num

def smallest_number_(a, b, c):
    return min(a, b, c)

#Task 2

def reverse_word(word):
   result = ""
   index = len(word) - 1
   while index >= 0:
       result += word[index]
       index -= 1
   return result

def reverse_word_(word):
    return word[::-1]


#Task 3
def palindrome(word):
    letters = list(word)
    i = 0
    j = len(word) - 1
    while (j > i):
        if(letters[i] != letters[j]):
           return False
        else:
            i += 1 
            j -= 1
            continue
    return True

def palindrome_(word):
    return word == word[::-1]


#Task 4

def quick_sort(array_nums):
    if(len(array_nums) <= 1):
        return array_nums
    else:
        pivot = array_nums[len(array_nums) // 2]
    bigger = []
    smaller = []
    equal = []
    for num in array_nums:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            bigger.append(num)
        else:
            equal.append(num)
    return quick_sort(smaller) + quick_sort(equal) + quick_sort(bigger)