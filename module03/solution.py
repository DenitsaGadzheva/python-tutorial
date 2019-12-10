
def sum_of_digits(n) : 
    num = abs(n)
    sum = 0
    while (num != 0) : 
        sum = sum + num % 10
        num  = num // 10
    return sum
	

def to_digits(n):
    lst = [int(digit) for digit in str(n)]
    return lst
	

def to_number(digits):
    n=0
    for index in range(len(digits)):
        n=10*n+digits[index]
    return n

    
def count_vowels(str):
        count = 0 
        string = str.lower()
        for char in string:
            if char in 'aeiouy':
                count += 1
        return count
		

def count_consonants(str):
        count = 0 
        string = str.lower()
        for char in string:
            if char in 'bcdfghjklmnpqrstvwxz':
                count += 1
        return count


def prime_number(number):
    if number < 3 :
        prime = True
        return prime
    for i in range(2, number-1): 
        if (number % i == 0):
            prime = False
            return prime
    prime = True
    return  prime

	
def fact_digits(n):
	    sum = 0
	    fact = 1
	    num = str(n)
	    for k in range( len(num) ):
	        fact = 1
	        for i in range(1, ( int(num[k]) + 1) ):
	            fact = i*fact
	        sum = sum + fact
	    return sum
	

def fibonacci(n):
        if n == 1:
	        return [1]
        fib = [1, 1]
        for i in range(2,n):
            new_fn= fib[i-1]+ fib[i-2]
            fib.append(new_fn)
        return fib



def fib_number(n):
    # Convert integer list to string list 
	    str_lst = [str(i) for i in fibonacci(n)]
    # Convert string list  into a single integer 
	    result = int("".join(str_lst))
	    return result
	

def palindrome(obj):
	    pali = str(obj) == str(obj)[::-1]
	    return pali
	

def char_histogram(string):
	    list_fill = []
	    for i in string:
	        list_fill.append( string.count(i) )
	        res = {k:v for k, v in zip( string, list_fill )}
	    return res
