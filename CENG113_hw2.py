# 240201046...

# # # # # # # # # # # # # # # # # # # #
# Monsters' World
from random import randint

n = 4
object_number = 4  #1G, 3M
flag = True

while flag:
    obj_cell_list = []
    flag = False
    
    #randomly select cells of objects that should not overlap with each other
    while True:
        cell = randint(0, n**2-1)
        if cell not in obj_cell_list:
            obj_cell_list.append(cell)    #first position for G, others for W 
        if len(obj_cell_list) == object_number:
            break  
   
    #determine whether objects are in proper cells 
    monsters = obj_cell_list[1:object_number]
    gold = obj_cell_list[0]
    if 0 in obj_cell_list: #G and Ms are not in cell 0
        flag = True
    elif (1 in monsters) and (n in monsters): #both cells adjacent to 0 does not include M.
        flag = True
    elif gold==(n-1): #if G is in the second corner
        if (n-2 in monsters) and (2*n-1 in monsters):
            flag = True
    elif gold==(n**2-n): #if G is in the third corner
        if (n**2-2*n in monsters) and (n**2-n+1 in monsters):
            flag = True
    elif gold==(n**2-1): #if G is in the last corner
        if (n**2-n-1 in monsters) and (n**2-2 in monsters):
            flag = True
    elif gold>0 and gold<(n-1): #the upper edge
        if (gold-1 in monsters) and (gold+n in monsters) and (gold+1 in monsters):
            flag = True
    elif gold>(n-1) and gold<(n**2-1): #the right edge
        if (gold-n in monsters) and (gold-1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>0 and gold<(n**2-n): #the left edge
        if (gold-n in monsters) and (gold+1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>(n**2-n) and gold<(n**2-1): #the lower edge
        if (gold-1 in monsters) and (gold-n in monsters) and (gold+1 in monsters):
            flag = True

#write the world to the file
f = open("monstersworld.txt", "w")
for i in range(n**2):
    if i==0:
        line = "P"
    elif i in obj_cell_list:
        if i==gold:
            line = "G"
        else:
            line = "M"
    else:
        line = "0" 
        
    if i != (n**2-1):
        f.write(line + "\n")
    else:
        f.write(line) 
f.close()

# INSERT YOUR CODE HERE ...

maap=open("monstersworld.txt","r")
red=maap.readlines()
mapp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
i=0
a=0
while i<4:
    f=0
    while f<4:
        mapp[i][f]=red[a]
        f+=1
        a+=1
    i+=1
"""above loop make my monster's world map"""
mapp2=[["P","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]]
"""my virtual monster's world map"""
x=0
y=0
"""my position variables"""
player="P"
score=0
step_counter=0
while True:
    monster_detector=False
    if x+1<4:
        if mapp[x+1][y]=="M\n" or mapp[x][y]=="M"   :    
            monster_detector=True
    if x-1>=0:
        if mapp[x-1][y]=="M\n" or mapp[x][y]=="M":
            monster_detector=True
    if y+1<4:
        if mapp[x][y+1]=="M\n" or mapp[x][y]=="M":
            monster_detector=True
    if y-1>=0:
        if mapp[x][y-1]=="M\n" or mapp[x][y]=="M":
            monster_detector=True
    """to detect monster around player"""
    if monster_detector==True:
        previous="H"
        print("You​ ​ just​ ​ heard​ ​ a​ ​ howl.​ ​ Be​ ​ careful!")
    else:
        previous="S"
        print("You​ ​ are​ ​ in​ ​ a​ ​ safe​ ​ room.​ ​ Don’t​ ​ worry!")
    """player's foot track"""
    print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
    for i in mapp2:
        print(i)
    move=input("What is your move? ")
    move =move.title()
    move_list=["W","S","A","D"]
    step_counter+=1
    while move not in move_list:
        print("There​ ​ is​ ​ no​ ​ such​ ​ direction!​ ​ Choose​ ​ right​ ​ (d),​ ​ left​ ​ (a),​ ​ up​ ​ (w)​ ​ or​ ​ down​ ​ (s).")
        print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
        move=input("What is your move? ")
        move=move.title()
        step_counter+=1
    """if player enter wrong character ,warn player""" 
    mapp2[x][y]=previous
    if move =="W":
        x-=1
    elif move=="S":
        x+=1
    elif move=="D":
        y+=1
    else:
        y-=1
    """moves"""
    while x<0 or y<0 or x==4 or y==4:
        if x<0:
            x+=1
        elif y<0:
            y+=1
        elif x==4:
            x-=1
        else:
            y-=1
        print("You​ ​ hit​ ​ the​ ​ wall.​ ​ Try​ ​ another​ ​ move!")
        print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
        move=input("What is your move? ")
        """if player hit the wall ,marn player"""
        move=move.title()
        while move not in move_list:
            print("There​ ​ is​ ​ no​ ​ such​ ​ direction!​ ​ Choose​ ​ right​ ​ (d),​ ​ left​ ​ (a),​ ​ up​ ​ (w)​ ​ or​ ​ down​ ​ (s).")
            print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
            move=input("What is your move? ")
            move=move.title()
            step_counter+=1
        """again if player enter wrong character, warn player"""
        if move =="W":
            x-=1
        elif move=="S":
            x+=1
        elif move=="D":
            y+=1
        else:
            y-=1
        step_counter+=1
    mapp2[x][y]=player
    if mapp[x][y]=="G\n" or mapp[x][y]=="G":
        print("Yay!​ ​ You​ ​ have​ ​ found​ ​ the​ ​ gold.")
        print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
        score=100
        break
    elif mapp[x][y]=="M\n" or mapp[x][y]=="M":
        print("Oh​ ​ no!​ ​ You​ ​ are​ ​ eaten​ ​ by​ ​ a​ ​ monster.")
        print("Number​ ​ of​ ​ steps​ ​ taken​ ​ so​ ​ far​ ​ is​",step_counter,".")
        break
    """game is over"""
print("Game Over")
score=score/step_counter
print("Score:",score)


maap.close()




