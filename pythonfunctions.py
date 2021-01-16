n = int(input("enter a number: "))
# sum = 0
# def sum_to(n):
#     sum = n
#     i = 0 

#     while i < n:
#         sum = sum +1
#         i += 1
#     return sum
def sum_to(num):
  sum = 0
  for i in range(num + 1):
    sum += i
  return sum
print(sum_to(n))

numbersarray1 = [10, 4, 2, 231, 91, 54]
numbersarray2 = [1,2,3,4,0]
def largest(ls):
    largest = 0
    for num in ls:
        if num > largest:
            largest = num
    return largest
print(largest(numbersarray1))
print(largest(numbersarray2))

string1 = 'fleep floop'
string2 = 'e', 'p', 'ee', 'fe'
def occurances(s1, s2):
    count = s1.count(s2)
    return count
print(occurances(string1, string2))

def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(product(2,4))