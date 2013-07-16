# counting inversions
filename = 'IntegerArray.txt'
with open(filename) as f:
    num_list = f.read().splitlines()
# don't forget to convert string to integer
num_list = [int(i) for i in num_list]
number = len(num_list)

def sort_and_count(l,n):
    if n <= 1:
        return (l,0)
    elif n == 2:
        if l[0] <= l[1]:
            return (l,0)
        else:
            return ([l[1], l[0]], 1)
    else:
        (half_first, x) = sort_and_count(l[:len(l)/2], n/2)
        (half_second, y) = sort_and_count(l[len(l)/2:], n-n/2)
        (whole, z) = merge_and_count(half_first, half_second, n)
    return (whole, x+y+z)

def merge_and_count(l_left, l_right, n):
    i = 0
    j = 0
    whole = []
    count = 0
    k = 0
    for k in range(n):
        if l_left[i] <= l_right[j]:
            whole.append(l_left[i])          
            i += 1
            if i == n/2:
                whole += l_right[j:]
                break          
        else:
            whole.append(l_right[j])
            count += n/2 - i
            j += 1
            if j == n - n/2:
                whole += l_left[i:]
                break            
    return (whole, count)        

#tests
test = [[1,3,5],[2,4,6],6]
print merge_and_count(test[0],test[1],test[2])

test_list = [1,3,5,2,4,6]
print sort_and_count(test_list,6)  

# don't print the sorted list, it is too long
print sort_and_count(num_list,number)[1]
