class c:
    def a(x):
        print(x)

    def b(y):
        if y == 2:
            a(y)
        else:
            a(y+1)

obj = c()
obj.b(3)

