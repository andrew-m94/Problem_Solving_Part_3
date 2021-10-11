#Problem 1

def find_sum_to_target(number_list,target):

    element = 0
    last_element = len(number_list) - 1
    dupe_count = 0

    for set_1 in number_list:

        for set_2 in number_list:

            if set_2 == number_list[element] and dupe_count == 0:
                dupe_count += 1
                continue

            elif set_1 + set_2 == target:
                print(f'{set_1} {set_2}')
                break

        if set_1 + set_2 == target:
            break
        
        elif set_1 == number_list[last_element] and set_2 == number_list[last_element]:
            print('No match found')

        element += 1

list_of_numbers = [5,77,10,50]
target = 15

find_sum_to_target(list_of_numbers,target)

list_of_numbers = [5,22,5,50]
target = 10

find_sum_to_target(list_of_numbers,target)

list_of_numbers = [4,77,10,1]
target = 15

find_sum_to_target(list_of_numbers,target)

#Problem 2

def is_incremental(number_list):
    number_list.sort()
    increment = number_list[1] - number_list[0]
    result = True

    iterations = len(list_of_numbers) - 1

    for pair in list_of_numbers:

        if list_of_numbers[iterations] - increment == list_of_numbers[iterations - 1]:
            result = True

        elif iterations == 0:
            break
        
        else:
            result = False
            break

        iterations -= 1

    return result

list_of_numbers = [18,15,20,19,21,16,17]
print(list_of_numbers)
result = is_incremental(list_of_numbers)
print(result)

list_of_numbers = [5, 7, 3, 8, 6]
print(list_of_numbers)
result = is_incremental(list_of_numbers)
print(result)

list_of_numbers = [15,25,35,30,20]
print(list_of_numbers)
result = is_incremental(list_of_numbers)
print(result)

#Problem 3

def count_pos_sum_neg(list_of_numbers):

    positives = []
    negatives = []
    count_pos_sum_neg = []
    
    for number in list_of_numbers:
        
        if number < 0:
            negatives.append(number)

        elif number > 0:
            positives.append(number)

    count_pos_sum_neg.append(len(positives))

    sum_of_neg = 0

    for number in negatives:
        sum_of_neg += number

    count_pos_sum_neg.append(sum_of_neg)

    print(count_pos_sum_neg)

case_list = [7,9,-3,-32,107,-1,36,95,-14,-99,21]
count_pos_sum_neg(case_list)

#Problem 4

def highest_lowest(number_string):
    
    number_string = number_string.split()
    element = 0

    for string in number_string:
        number_string[element] = int(string)
        element += 1

    number_string.sort()
    result = f'{number_string[0]} {number_string[len(number_string) - 1]}'
    return result

case_string = '3 9 0 1 4 8 10 2'
result = highest_lowest(case_string)
print(result)

#Problem 5

def validate_email_address(email_address):

    if '@' in email_address:
        split_address = email_address.split('@',1)

    else:
        return False

    local = split_address[0]
    domain = split_address[1]

    if local == '':
        return False

    elif '@' in local or '@' in domain:
        return False

    elif '.' not in domain:
        return False

    bad_chars = {'<','>','(',')','[',']',';',':',',','@','\\'}
    first_char = {'-','_','.','+'}

    if any(char in bad_chars for char in local):
        return False

    elif any(char in first_char for char in local[0]):
        return False

    else:
        return True

email_address = 'johndoe123@gmail.com'
valid_email = (validate_email_address(email_address))
print(valid_email)

email_address = '@gmail.com'
valid_email = (validate_email_address(email_address))
print(valid_email)

email_address = '_johndoe123@gmail.com'
valid_email = (validate_email_address(email_address))
print(valid_email)

