list1 = [1, 2, 3, 4, 7, 9, 11, 27]
list2 = [1, 2, 6, 7, 11, 17, 27]

result = list(filter(lambda x: x in list1, list2))

print(f'List one: {list1}\nList two: {list2}\nThe instersection of two lists: ', result)
