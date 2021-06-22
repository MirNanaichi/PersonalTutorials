print ("Hello world!")

i = 0
res = 0

x = input("how many loops?: ")
print(f'this one will loop {x} times')

while i < int(x):
    a = input("give number: ")
    print(f'{a} was input nr. {i + 1}')
    res += int(a)
    i += 1

print (f'sum of all nubers are: {res}')
