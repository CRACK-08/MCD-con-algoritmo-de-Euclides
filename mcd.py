class maximoDivisor:
    c = ""
    def __init__(self):
        print("creado")

    def prueba(self,a,b):
        if b > a:
            return self.prueba(b,a)
        if b == 0:
            return a,self.c
        else:
            q,r = divmod(a,b)
            print(a,"=",q,"*",b,"+",r)
            self.c += str(a) + " = " + str(q) + " * " + str(b) + " + " + str(r) + "\n"
            return self.prueba(b,r)


