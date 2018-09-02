'''We want to see if 67 is prime and how many operations performed'''


def naive(primes, element, count):
    '''Naive

    0(n)
    '''
    for num in primes:
        if num == element:
                return count
        count += 1
    return -1


def binary_search(array, element, count):
    '''Binary Search

    O(log^2n)
    '''
    count += 1
    length = len(array) - 1
    if length >= 1:
        mid = 1 + int((len(array) - 1)/2)
        if array[mid] == element:
            return count
        elif array[mid] > element:
            array = array[:mid]
            return binary_search(array, element, count)
        elif array[mid] < element:
            array = array[mid:]
            return binary_search(array, element, count)
    else:
        return -1


# Helper function to gen Primes
def _gen_primes(max_num):
    rval = []
    print('Generating list of primes from 2 to {}'.format(max_num))
    for num in range(2, max_num):
        if all(num % i != 0 for i in range(2, num)):
            rval.append(num)
    print('Done')
    return rval


primes = _gen_primes(90000)

count = naive(primes, 641, 0)
if count != -1:
    print("Naive: 67 is prime and the count is " + str(count))

count = binary_search(primes, 641, 0)
if count != -1:
    print("Binary Search: 67 is prime and the count is " + str(count))
