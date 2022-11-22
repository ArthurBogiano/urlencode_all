a = input('Encode: ')

print()

for i in list(a):
	print(f'%{i.encode().hex()}', end='')