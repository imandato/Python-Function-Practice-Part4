def max_num(num1, num2, num3):
    return(max(num1,num2,num3))

print(max_num(4,7,8))
print(max_num(4,11,8))

def mult_list(*numbers):
    product = 1
    for i in numbers:
        # print (i)
        product = product * i
        # print(i)
    return(product)

print(mult_list(2,2,6,8))


def rev_string(string):
    reverse = string [::-1]
    return(reverse)

print(rev_string("hello"))

def num_within(num, range_start, range_end):
    if num < range_start:
        return False
    elif num >range_end:
        return False
    else:
        return True

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))


triangle = [[1],[1,1]]
def pascal(num):
    if num <1:
        print("please provide a digit equal to or greater than 1")
    elif num == 1: 
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < num:
            row = []
            row_previous = triangle[row_number-1]
            length = len(row_previous)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(row_previous[i-1]+ row_previous[i])
                    # row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

pascal(5)
pascal(8)
        
    