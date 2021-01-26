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

    def extended_euclid_gcd(self,a, b):
        s = 0; old_s = 1
        t = 1; old_t = 0
        r = b; old_r = a

        while r != 0:
            quotient = old_r//r 
            old_r, r = r, old_r - quotient*r
            old_s, s = s, old_s - quotient*s
            old_t, t = t, old_t - quotient*t
        return [old_r, old_s, old_t]



