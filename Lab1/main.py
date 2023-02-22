from calculate_func import calculate_func
import list_creater


print("Hello world!")

print("Mini calculator\nOperations: +(add), -(sub), /(div), *(mul)")
value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))
operator = input("Enter operator: ")
print(calculate_func(value1, value2, operator))

print("List manipulation\nStart...")
len_list = int(input("Enter list length: "))
list_creater.create_list(len_list)

