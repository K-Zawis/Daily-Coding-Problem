"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].
"""

"""
params
    num_list - List[int]

Takes an array of integers and calulates the priduct of all numbers
insdie of the array.

returns int
"""
def prod(num_list) -> int:
    product = 1
    for num in num_list:
        product *= num
    return product

"""
global variables
"""
num_list = [3, 2, 1]

def list_of_elem_prods(num_list):
    """
    we begin by calling the prod function to retrieve the product of 
    all elements in num_list
    """
    product = prod(num_list)

    """
    for each number in our num_list we map the values to the product 
    divided by number using List Comprehension:

        [ expression for element in list_to_map]

    """
    return [product // num for num in num_list]

print(list_of_elem_prods(num_list))

"""
Follow-up: what if you can't use division?
"""

def follow_up(num_list):
    final_list = []
    
    for index in range(len(num_list)):
        """
        get a copy of original list without current index
        slicing is the fastest way to copy 1-D arrays
        """
        temp = num_list[:]
        temp.pop(index)
        """
        calculate product by calling our prod function again
        """
        product = prod(temp)

        """
        append each product to our new list
        """
        final_list.append(product)

    return final_list

print(follow_up(num_list))

