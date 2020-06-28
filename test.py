


def test1(list):
    for i in list:
        if i == 0:
           list.append(0)
           list.remove(0)
    print(list)

list = [4,0,5,0,3,0,0,5]



def test2():
    text = ''
    x = int(input('Какое кол-во строк ?'))
    for i in range(0,x):
         text += input()
    glasn = ['а', 'у', 'о', 'ы','и', 'э', 'я', 'ю', 'ё', 'е']
    sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п','р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    lstglasn = []
    lstsogl = []
    string = "".join(text.split())
    for i in string.lower():
        if i in glasn:
           lstglasn.append(i)
        elif i in sogl:
           lstsogl.append(i)
    print("кол-во строк : {} , гласные : {} , согласные : {}".format(x,len(lstglasn),len(lstsogl)))



def test3():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
       print('Да')
    else:
       print('НЕТ')
