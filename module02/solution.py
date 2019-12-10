    

def num_add(a,b):
    return a+b

def num_sub(a, b):
    return a-b

def num_mul(a, b):
    return a*b

def num_div(a, b):
    return a/b

def num_floor(a, b):
    return a // b

def num_rem(a, b):
    return a % b

'''
print("suma=",num_add(3,5))
print("sub=",num_sub(3,5))
print("mul=",num_mul(3,5))
print("div=",num_div(3,5))
'''

'''
print("floor=",num_floor(5,2))
print("rem=",num_rem(5,3))
'''
IS_TRUE = True
IS_FALSE = False
'''
print("IS_TRUE=",IS_TRUE)
print("IS_FALSE=",IS_FALSE)
'''
PANCAKE_INGREDIENTS = {'flour': 2, 'eggs': 4, 'milk': 200, 'butter': False, 'salt': 0.001}
'''
print("pancake_ingredients=", pancake_ingredients)
'''

def ingredient_exists(ingr, dict):
    if ingr in dict:
        return IS_TRUE
    else:
        return IS_FALSE
'''    
print("pancake_ingredients=", pancake_ingredients)
'''

def fatten_pancakes(dict):
    dict['eggs'] = 6
    dict['butter'] = True
    return   dict.copy()
'''
print("fatten_pancakes = ", fatten_pancakes(pancake_ingredients))
'''

def add_sugar(dict):
    dict['sugar']=True
    return dict.copy()
   
def remove_salt(dict):
   dict.pop("salt") 
   return dict.copy()

'''
print("pancake_ingredients=", pancake_ingredients)
print("pancake_with_sugar = ", add_sugar(pancake_ingredients))
print ("remove_salt=", remove_salt(pancake_ingredients))
'''

FIBONACCI_NUMBERS = []


for i in range(12):
    if ( i < 2 ):
        FIBONACCI_NUMBERS.append(1)
    else:
        FIBONACCI_NUMBERS.append(FIBONACCI_NUMBERS[i-1] + FIBONACCI_NUMBERS[i-2])



'''
if (n in lst): 
      fib_exists = True 
   return fib_exists

'''

def add_fibonacci(lst):
    l=len(lst)
    lst.append(lst[l-1]+lst[l-2])
    return lst.copy()

def fib_exists(lst, n):
    if n in lst:
        return IS_TRUE
    else:
        return IS_FALSE

def which_fib(lst, n):
    if lst.index(n) > 0:
        return lst.index(n)+1
    else:
        return 1

    
