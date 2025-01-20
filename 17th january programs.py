1)
def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]
user_input=input("Enter the String to reverse:")
reverse=reverse(user_input)
print("Reversed string:",reverse)


2)
def is_palindrome(s): 
    if len(s) <= 1:   
        return True 
    if s[0] != s[-1]:   
        return False 
    return is_palindrome(s[1:-1])    
 
string = "madam" 
print("Is palindrome:", is_palindrome(string))

3)
def power(x, n): 
    if n == 0: 
        return 1 
    return x * power(x, n-1) 
x = 2 
n = 3 
print(f"{x} raised to the power {n} is:", power(x, n))

4)
def sum(n): 
    if n==0: 
        return 0 
    return n%10+sum(n//10) 
number=125 
print(sum(number))

5)
def 2darray_(arr): 
    total=0 
    for i in arr: 
        total+=sum(i) 
    return total 
array= [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
] 
print(2darray_(array))