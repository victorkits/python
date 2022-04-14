def reverse(attr):
    if len(attr) == 1:
        return attr
    else:
        tail = attr[1:]
        return reverse(tail) + [attr[0]]


class T:
    def __init__(self):
        print('tetttt')



if __name__ == '__main__':

    a = T
    a.makro = '1234'



