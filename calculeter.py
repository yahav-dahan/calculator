num_1 = input('num 1:')
num_2 = input('num 2:')
operand = input('operand:')
num_1 = float(num_1)
num_2 = float(num_2)
result = 'error'
good_result = 'the answer is:'
answer = -1
if operand == '*':
    answer = num_1 * num_2
    result = good_result + str(answer)
elif operand == '+':
    answer = num_1 + num_2
    result = good_result + str(answer)
elif operand == '/':
    if num_2 != 0:
        answer = num_1 / num_2
        result = good_result + str(answer)
elif operand == '-':
    answer = num_1 - num_2
    result = good_result + str(answer)

print(result)


