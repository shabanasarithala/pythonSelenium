class S1:
    a, b = 1, 2

    def m1(self):
        print(self.a + self.b)


class S2(S1):
    c, d = 52, 33

    def m2(self):
        print(self.c - self.d)


objs2 = S2()
objs2.m2()
objs2.m1()
