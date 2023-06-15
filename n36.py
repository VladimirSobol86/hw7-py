def print_operation_table(operation, num_rows=6, num_columns=7):
   for x in range (1, num_rows + 1):
        nums = []
        for y in range (1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print(*nums)

print_operation_table(lambda x, y: x * y)