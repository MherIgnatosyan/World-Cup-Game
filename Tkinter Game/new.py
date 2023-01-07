import random
import tkinter as tk
from tkinter import *

cheatend = False
game_status = True
movedir = 0
balls_collected = 0
window = Tk()
window.geometry("800x600")
window.title("World Cup")
window.resizable(False, False)

introimg = PhotoImage(file = "intropng.png")
bglabel = Label(window , image= introimg)
bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)


def choosingateam():

    parent = Toplevel(window)
    parent.title("Choosing a Team")
    parent.geometry("800x600")
    parent.resizable(False, False)


    introimg = PhotoImage(file = "intropng.png")
    bglabel = Label(parent , image= introimg)
    bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)
    argimg = PhotoImage(file = "argimg.png")
    portimg = PhotoImage(file = "portugimg.png")
    
    argbutton = Button(parent , image=argimg , command= lambda :gamescreen("ronaldoface.png", "messiface.png"))

    argbutton.place(x = 100 , y = 200)

    portugbutton = Button(parent , image=portimg , command= lambda: gamescreen("messiface.png", "ronaldoface.png"))

    portugbutton.place(x = 550 , y = 200)

    parent.mainloop()

startbutton = Button(window , text ="Choose a Team and Play!", bg="green", fg = "white", height = 5, command= choosingateam)
startbutton.place(x = 100, y = 100)



grid = [
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,2],
    [0,0,0,0,0,0,1,2,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,2,0,0,0,0,0,2,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,1,2,0,0],
    [0,2,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    
def gamescreen(playername,  defendername):

    global grid
    global game_status

    window.destroy()
    child = Tk()
    child.title("World Cup")
    child.geometry("800x600")
    child.resizable(False, False)
    playground = Canvas(child, width=800 , height = 600, bg = "blue")
    playground.pack()
    scoredimage = PhotoImage(file="scoredimg.png")
    background_image = PhotoImage(file="backgroundimage.png")    
    maguire = PhotoImage(file="maguire.png")
    defender_image = PhotoImage(file= defendername)
    playerimage = PhotoImage(file=playername)
    bacground = playground.create_image(400, 300, image = background_image)
    player = playground.create_image(400 , 300, image = playerimage)
    ballImg = PhotoImage(file = "ballimg.png")
    flagImg  = PhotoImage(file="boudflag.png")
    balls = []
    flags = []

    for i in range(16):
        for j in range(12):
            if grid[j][i]==0:
                continue
            elif grid[j][i]==1:
                temp_flag = playground.create_image(i*50+25 , j*50+25, image = flagImg)
                flags.append(temp_flag)
            elif grid [j][i] == 2:
                temp_ball = playground.create_image(i*50+25 , j*50+25, image = ballImg)
                balls.append(temp_ball)

    def boundry_reach(obj):

        playerboundry = playground.bbox(obj)
        playerleft = playerboundry[0]
        playerright = playerboundry[2]
        playertop = playerboundry[1]
        playerbottom = playerboundry[3]

        if playerleft <10:
            playground.move(obj,10 , 0)
        elif playerright > 790 :
            playground.move(obj,-10 , 0)
        elif playertop < 10:
            playground.move(obj,0 , 10)
        elif playerbottom >590:
            playground.move(obj,0 , -10)

    # def ball_collision():
    #         global balls_collected
    #         print(len(balls))
    #         playerboundry = playground.bbox(player)
    #         playerleft = playerboundry[0]
    #         playerright = playerboundry[2]
    #         playertop = playerboundry[1]
    #         playerbottom = playerboundry[3]
        
    #         for i in range(len(balls)):
    
    #             temporary_ball = balls[i]
    #             temp_ball_cords = playground.bbox(temporary_ball)

            
    #             if temp_ball_cords[0] < playerboundry[2] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[3]< temp_ball_cords[3] and movedir == 4:

    #                 playground.itemconfig(balls[i] , image = scoredimage)
    #                 balls_collected = balls_collected + 1
    #                 balls.pop(i)
    #             elif temp_ball_cords[0] < playerboundry[0] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[3]< temp_ball_cords[3] and movedir == 3 : 
    #                 playground.itemconfig( balls[i]  , image = scoredimage)

    #                 balls_collected += balls_collected + 1
 
    #                 balls.pop(i)
    #             elif temp_ball_cords[0] < playerboundry[0] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[1]< temp_ball_cords[3] and movedir == 2:
    #                 playground.itemconfig( balls[i]  , image = scoredimage)
    
    #                 balls_collected += balls_collected + 1
 
    #                 balls.pop(i)
    #             elif temp_ball_cords[0] < playerboundry[2] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[1]< temp_ball_cords[3] and movedir ==1 :
    #                 playground.itemconfig(balls[i]  , image = scoredimage)
    #                 balls_collected = balls_collected + 1
 
    #                 balls.pop(i)

    def collision_detection(obj):

        for i in range(len(flags)):
            flag_boudry = playground.bbox(flags[i])
            flagleft = flag_boudry[0]
            flagright = flag_boudry[2]
            flagtop = flag_boudry[1]
            flagbottom = flag_boudry[3]

            playerboundry = playground.bbox(obj)
            playerleft = playerboundry[0]
            playerright = playerboundry[2]
            playertop = playerboundry[1]
            playerbottom = playerboundry[3]


            if  flagleft< playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and movedir == 1: 

                playground.move(obj ,-10,0)


            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom and movedir == 2: 
                playground.move(obj, 10 , 0)


            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom and movedir == 4:
                playground.move(obj , 0 , -10)

            elif flagleft < playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and movedir == 3:
                playground.move(obj, 0 , 10)

    def moveright(event):

        global movedir
        movedir = 1
        playground.move(player , 10 , 0)
        boundry_reach(player)
        collision_detection(player)
        # ball_collision()



    def moveleft(event):
  
        global movedir
        movedir = 2
        playground.move(player , -10 , 0)
        boundry_reach(player)
        collision_detection(player)
        # ball_collision()
    
    def moveup(event):
        global movedir
        movedir = 3
        playground.move(player , 0 , -10)
        boundry_reach(player)
        collision_detection(player)
        # ball_collision()


 
   


    # def game_status_change(event):
    #     global game_status
    #     print(game_status)
    #     game_status = not game_status  
    #     child.update() 

    # playground.bind_all("p", game_status_change)



    playground.bind_all("<Right>", moveright)
    playground.bind_all("<Left>", moveleft)
    playground.bind_all("<Up>", moveup)



     



    child.mainloop()


window.mainloop()