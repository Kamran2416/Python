#wap in which we have two teams rangers and pirates team a has 5 players wherease team b has 7 players 
#find palyer in rangers but not in pirates
#find players in rangers or pirates
#find palyers in rangers and pirates
#find palyers in rangers or pirates both but not in both

rangers={'Kamran','Hassan','Irqan','Hamza','Saqlain'}
pirates={'Kamran','Hassan','Irqan','Nikhil','Saqlain','Shezan','Altamash'}

print("Players in a but not in b",rangers - pirates)
print("Players in a or b",rangers | pirates)
print("Players in a and b",rangers & pirates)
print("Players in a or b but not in both",rangers ^ pirates)

#wrong method approach - z= set('a','b','c','d')