with open('names.txt', 'r') as f:
    names = f.read()

names_list = names.split(', ')
names_list.sort()

for name in names_list:
    print(name)

print(f'Sorted a total of {len(names_list)} names.')
