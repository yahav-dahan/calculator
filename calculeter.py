num_1 = input('num 1:')
num_2 = input('num 2:')
operand = input('operand:')
num_1 = float(num_1)
num_2 = float(num_2)
answer = -1
if operand == '*':
    answer = num_1 * num_2
elif operand == '+':
    answer = num_1 + num_2
elif operand == '/':
    answer = num_1 / num_2
elif operand == '-':
    answer = num_1 - num_2
else:
    print('EROR')
print('the answer is:'+ str (answer))


