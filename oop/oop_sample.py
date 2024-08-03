class calc:
    def sum(self,a,b):
        self.s=a+b
    def sub(self,a,b):
        self.d=a-b
    def pro(self):
        self.z=(self.s)*(self.d)
    def div(self):
        self.q=((self.s)+(self.d))/(self.z)
    def disp(self):
        print("sum is",self.s)
        print("difference is",self.d)
        print("product is",self.z)
        print("quotient is",self.q)
        
Trial=calc()

Trial.sum(3,2)
Trial.sub(3,2)
Trial.pro()
Trial.div()
Trial.disp()