# Add all numbers between 1 and n


def sum_all_naive(n):
    """O(n) Linear Time-Complexity

    Sum all the numbers linearly

    >>> sum_all_naive(100)
    5050
    """
    rval = 0
    for num in range(n + 1):
        rval += num
    return rval


def sum_all(n):
    '''O(1) Constant Time-Complexity

    Sum all the numbers in constant time

    >>> sum_all(100)
    5050
    '''
    return int(n * (n + 1)/2)

# Example of logrithmic time-complexity is binary search


def find_duplicate(array):
    '''O(n^2) Quadratic Time-Complexity

    return the first duplicate found or none if none

    >>> find_duplicate([2,3,4,5,2])
    2

    >>> find_duplicate([2,3,4,5,6])
    '''
    for index1, num1 in enumerate(array):
        for index2, num2 in enumerate(array):
            if num1 == num2 and index1 != index2:
                return num1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
