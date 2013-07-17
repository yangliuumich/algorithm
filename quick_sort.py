#QuickSort
filename = "QuickSort.txt"
def create_number_list(filename):
    with open(filename) as f:
        numbers = f.read().splitlines()
    numbers = [int(i) for i in numbers]
    return numbers

def quicksort(numbers, n, method):
    if n <= 1:
        return numbers,0    
    p = choose_pivot(numbers, n, method)
    numbers[p], numbers[0] = numbers[0], numbers[p]
    numbers, pivot = partition(numbers, 0, n)
    left,left_count = quicksort(numbers[:pivot], pivot, method)
    right, right_count = quicksort(numbers[pivot+1:], n-1-pivot, method)
    numbers =left + [numbers[pivot]] + right
    return numbers, left_count + right_count + n-1

def choose_pivot(numbers, n, method):
    if method == 1:
        return 0
    elif method == 2:
        return n-1
    elif method == 3:
        if n == 2:
            if numbers[0]>numbers[1]:
                return 1
            else:
                return 0
        index = [0, int((n-0.5)/2), n-1]
        pivot = [i for i in index if numbers[i]!=max([numbers[j] for j in index]) and numbers[i]!=min([numbers[k] for k in index])]
        return pivot[0]
    else:
        print 'No pivot defined.'
        return None

def partition(numbers, l, r):
    pivot = numbers[l]
    i = l + 1
    for j in range(l + 1, r):
        if numbers[j] < pivot:
           numbers[i], numbers[j] = numbers[j], numbers[i]
           i += 1
    numbers[l], numbers[i-1] = numbers[i-1], numbers[l]
    return numbers,i-1

# print result
# MUST re-create number list every time before sorting
for i in [1,2,3]:
    numbers = create_number_list(filename)
    print quicksort(numbers, len(numbers), i)[1]
