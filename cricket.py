class Player:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
  def run(self):  
   print( f'{self.name} is running'  )
  
class Cricketer(Player):  
  def catch_ball(self):  
    print( f'{self.name} Caught the ball'  )
  
class Batsman(Cricketer):  
  def swing_bat(self):  
    print( f'what a shot by {self.name}'  )
  
player1 = Batsman('Virat Kohli', 31)  
  
print(isinstance(player1, Batsman)) # True  
print(isinstance(player1, Cricketer)) # True  
print(isinstance(player1, Player)) # True  
print(isinstance(player1, object)) # True 
