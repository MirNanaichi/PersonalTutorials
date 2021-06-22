print("Fibonacci")

def Fibo(input_num):
    if input_num == 0:
        return 0
    elif input_num == 1 or input_num == 2:
        return 1
    else:
        return Fibo(input_num - 1) + Fibo(input_num - 2)

input_num = int(input("give a number: "))
result = Fibo(input_num)

print(f'Fibonacci number for {input_num} is: {result}')
