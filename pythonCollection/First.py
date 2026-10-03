# n=int(input("Enter a number: "))
# arr=[]

# print("Enter the elements of the array:")

# for i in range(n):
#     element=int(input())
#     arr.append(element)

# print("The elements of the array are:")

# for i in range(n):
#      print(arr[i] ,end=" ")


#2--------------------------

"""
n=int(input("Enter a number: "))
arr=[]

print("Enter the elements of the array:")

for i in range(n):
    element=int(input())
    arr.append(element)

sum=0
for i in range(n):
    sum+=arr[i]

print("The sum of the elements of the array is:",sum)

"""
""" 
3 

arr = [11, 20, 33, 42, 55, 60]

even =[]
odd=[]

for i in range(len(arr)):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print("The even elements of the array are:",even)
print("The odd elements of the array are:",odd)

"""

"""
4
arr = [5, 10, 15, 20, 25, 30]

print("Value of even index elements of the array are:")
for i in range(0, len(arr), 2):
    print(arr[i], end=" ")


print("\nValue of odd index elements of the array are:")
for i in range(1, len(arr), 2):
    print(arr[i], end=" ")

"""
"""
5
Input:
Array Size = 7
Array Elements = 12 17 24 39 40 55 70
Output:
Count of Even Values = 4
Count of Odd Values = 3
Explanation:
? Initialize counters: evenCount = 0, oddCount = 0.
? For each element in the array:

? If divisible by 2 ? increase evenCount.
? Otherwise ? increase oddCount.

? Final counts are displayed.


n=int(input("Enter a number: "))
arr=[]

for i in range(n):
    element=int(input())
    arr.append(element)

evenCnt=0
oddCnt=0

for i in range(n):
    if arr[i]%2==0:
        evenCnt+=1
    else:
        oddCnt+=1

print("Count of Even Values =",evenCnt)
print("Count of Odd Values =",oddCnt)

"""

"""
6
Question 6: Write a java program to search an element in an array , its element found or not.
Asked In Practice assignment
Input:
Array = {10, 20, 30, 40, 50}
Element to search = 30
Output : Element 30 found at index 2
Explanation :

n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)

searchElement=int(input("Enter the element to search: "))
found=False
for i in range(n):
    if arr[i]==searchElement:
        print(f"Element {searchElement} found at index {i}")
        found=True
        break

if not found:
    print(f"Element {searchElement} not found in the array")

"""
"""
7

Input : Array = {1, 2, 3, 4, 5}
Output : Reverse array = {5, 4, 3, 2, 1}
Explanation :
The last element becomes the first, and the first becomes the last by traversing from the end to the start.
n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)

left=0
right=n-1

while left<right:
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    left+=1
    right-=1

print("Reverse array =",arr)

"""
"""Input : Array = {1, 2, 4, 5, 7} (numbers from 1 to 7 should be present)
Output : Missing elements = {3, 6}
Explanation:
Check sequence numbers one by one. If a number from 1 to maximum (7) is not in the array, it is missing.

n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)

maxElement=7

missingElements=[]
for i in range(1, maxElement + 1):
    if i not in arr:
        missingElements.append(i)

print("Missing elements =",missingElements)

"""

"""
array1 = [5, 10, 15, 20]

array2 = []

for i in range(len(array1)):
    array2.append(array1[i])

print("Array2 =", array2)
"""

"""10

Question 10: Write a program in java to delete an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 5

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to delete : 3

Expected Output : The new list is : 1 2 3 5


arr = [1, 2, 3, 4, 5]
position = 3
for i in range(position - 1, len(arr) - 1):
    arr[i] = arr[i + 1]


print("The new list is:")

for i in range(len(arr) - 1):
    print(arr[i], end=" ")

"""

"""
11
arr = [12, 35, 1, 10, 34, 1]

largest=float('-inf')
secondLargest=float('-inf')

for i in range(len(arr)):
    if arr[i]>largest:
        secondLargest=largest
        largest=arr[i]
    elif arr[i]>secondLargest and arr[i]!=largest:
        secondLargest=arr[i]

print("The second largest element in the array is:",secondLargest)
"""

"""
12
Question 12: Write a program in java to insert an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 6

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to insert : 2
Value : 200

Expected Output : The new list is : 1 2 200 3 4 5
"""


arr = [1, 2, 3, 4, 5]
position = 2
value = 200

arr.insert(position, value)
print("The new list is:", arr)


arr = [1, 2, 3, 4, 5]

position=int(input("Enter the position where to insert: "))
value=int(input("Enter the value to insert: "))

for i in range(len(arr)-1,position-1,-1):
    arr[i+1]=arr[i]
arr[position]=value

print("The new list is:")
for i in range(len(arr)):
    print(arr[i], end=" ")
        
