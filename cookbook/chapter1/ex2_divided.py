def drop_first_last(grades):
    first, *middle, last = grades
    return avg[middle]

record = ['ajioy', 'ajioy@hotmail.com', '010-2233111', '13545123211']
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)
print(middle) # [2, 3, 4]
print(last)

*trailing, current = [10, 9, 8, 7, 6, 5, 4, 3]
print(trailing)
print(current) # last element
