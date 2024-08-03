class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a)
        print(b)
    def sum(self):
        self.s=(self.a)+(self.b)
    def sub(self):
        self.d=(self.a)-(self.b)   
    def pro(self):
        self.z=(self.s)*(self.d)
    def div(self):
        self.q=((self.s)+(self.d))/(self.z)
    def disp(self):
        print("sum is",self.s)
        print("difference is",self.d)
        print("product is",self.z)
        print("quotient is",self.q)
        
Trial=calc(3,2)

Trial.sum()
Trial.sub()
Trial.pro()
Trial.div()
Trial.disp()
