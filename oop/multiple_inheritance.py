class team:
    def __init__(self,name,app):
        print("Player name:",name)
        print("Appearances:",app)
        
class stat:
    def prnt(self,runs,wickets):
        print("Runs:",runs)
        print("Wickets:",wickets)
        
class player(team,stat):
    pass
        
Kohli=player("Kohli",389)
Kohli.prnt(15000,3)