class carshowroom:
    def __init__(self):
        print("Are you a registered customer in the showroom?")
        c=input()
        det={"abhi":"1234","ram":"5678"}
        if(c=="yes"):
            while(1):
                usr=input("Enter username:")
                pswd=input("Enter password:")
                if(usr in det and det[usr]==pswd):
                    print("Logged in!")
                    self.brand()
                    break
                else:
                    print("invalid credentials!")
        else:
            usr=input("Enter a username:")
            pswd=input("Enter a password:")
            det[usr]=pswd
            print("Your account has been registered!")
            while(1):
                usr=input("Enter username:")
                pswd=input("Enter password:")
                if(usr in det and det[usr]==pswd):
                    print("Logged in!")
                    self.brand()
                    break
                else:
                    print("invalid credentials!")
    def brand(self):
        brands=["Hyundai","Suzuki","Tata"]
        brnd=input("Enter Brand name:")
        while(1):
            if(brnd==brands[0] or brnd==brands[1] or brnd==brands[2]):
                self.brnd=brnd
                break
            else:
                brnd=input("We don't have this brand.Choose another:")
                
        

a1=carshowroom()


            