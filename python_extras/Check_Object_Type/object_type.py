"""

Check object Type

"""


lista = ['a', 1,1.2,True , (1,2) , [6,7,8], {0,1},{'nome': 'Regis'}]


for item in lista:

    if isinstance(item, set):
        print("SET")
        item.add(5)
        print(item,isinstance(item,set))

    elif isinstance(item, str):
        print("STR")
        print(item.upper())
    
    elif isinstance(item, (int,float)):
        print('NUM')
        print(item, item * 2)

    else:
        print("Outro")