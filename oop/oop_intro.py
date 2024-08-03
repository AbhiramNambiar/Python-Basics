class indian_team:
    def number(self):
        print("Number of players in team is 11")
    def name(self,a):
        print("Name of the player is",a)
        self.av=a
    def runs(self,b):
        print(self.av)
        print("Runs:",b)
        
Kohli= indian_team()

Kohli.number()
Kohli.name("Kohli")
Kohli.runs(12344)
