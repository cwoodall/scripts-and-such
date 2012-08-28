class ByteArray(list):
    def __setitem__(self, key, item):
        alt_item = item > 0;
        return super(ByteArray, self).__setitem__(key, alt_item)

    def __or__(self, b):
        a = self
        c = []
        if (len(a) > len(b)):
            b = [False in range(0,len(a)-len(b))] + a
        elif (len(b) > len(a)):
            a =  [False for x in range(0, len(b)-len(a))] + a

        for i in range(0, len(a)):
            c.append(a[i] | b[i])

        return ByteArray(c)

    def __and__(self, b):
        a = self
        c = []
        if (len(a) > len(b)):
            b = [False in range(0,len(a)-len(b))] + b
        elif (len(b) > len(a)):
            a = [False for x in range(0, len(b)-len(a))] + a

        for i in range(0, len(a)):
            c =  [a[i] & b[i]] + c 

        return ByteArray(c)

    def __invert__(self):
        a = []
        for i in range(len(self)):
            a = a + [not self[i]]

        print a
        return ByteArray(a)

    def __lshift__(self, b):
        a = self
        a = a + [False for x in range(b)]
        
        return ByteArray(a)

    def __rshift__(self, b):
        a = self
        for i in range(b):
            a.pop()
            a = [False] + a
            
        return ByteArray(a)

    def __str__(self):
        string = ""
        for i in range(len(self)):
            if (self[i]):
                string = string + "1"
            else:
                string = string + "0"
        return string
                
    def alter(self, bits, values):
        for b_loc in range(0,len(bits)):
            bit = bits[b_loc]
            value = values[b_loc]
            self[bit] = value
                
if __name__ == "__main__":
    a = ByteArray([True, False, True, False])
    b = ByteArray([False, True, True, True, True])
    print(a )
    print(b)
    print("%s | %s = %s" % (a,b,a|b))
    print("%s & %s = %s" % (a,b,a&b))


    print("not %s = %s" % (b, ~b))

    print(a << 1)
    print(a >> 1)
