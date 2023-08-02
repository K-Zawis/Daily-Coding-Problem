"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

num_list = [10, 15, 3, 7]
k = 10

def is_sum_in_list_elem(num_list, k):
    """
    we use range iterration using the list length-1.
    This is to ensure we remove a redundant itterration
    which will involve an empty list and a number.
    """
    for index in range(len(num_list)-1):
        """
        We create a sublist consisting of the last <index> elements,
        inverting it in the process. This is to ensure each number
        is only compared once.
            eg:
                [7, 3, 15] 10
                [7, 3] 15
                [7] 3
        """
        for num in num_list[:index:-1]:
            if (num + num_list[index]) == k:
                return True
    return False

print(is_sum_in_list_elem(num_list, k))


"""
Bonus: Can you do this in one pass?
"""

def bonus(num_list, k):
    for index in range(len(num_list)):
        """
        this time we use the index to retrieve the element
        and then take it away from k to check if the remainder
        is in the sublist explained in the previous algorithm.
        """
        element = num_list[index]
        if k - element in num_list[:index:-1]:
            return True
    return False

print(bonus(num_list, k))

