ages = {'Tod':35, 'Jane':23, 'Paul':62}

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
