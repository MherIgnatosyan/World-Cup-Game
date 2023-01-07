import random
import tkinter as tk
from tkinter import *
import os
from timeit import default_timer as timer
import time
game_save_indicator = False
cheatend = False
game_not_paused = True
player_win = False
movedir = 0
balls_collected = 0
key_up = " "
key_right = " "
key_left = " "
key_down = " "
key_config = " "
player_x_cord = 0
player_y_cord = 0
key_config = " "
player_lose = False
defender_dir = [0 , 0]
start_time = 0
time_spent = 0
player_save = {'name' : '' , 'time' : ''}
score_balls = 0
defender_movement_dir = [0,0]
leader_keys = []
leader_values = []

load_file_text = {'playercords': '' , 'defedercords' : '' , 'userconfig': ''}
window = Tk()

window.geometry("800x600")
window.title("World Cup")
window.resizable(False, False)
windows_canvas = Canvas(width=800 , height= 600 , bg = "white" )
windows_canvas.pack()
introimg = PhotoImage(file = "intropng.png")
windows_canvas.create_image(400 , 300 , image = introimg)

# bglabel = Label(window , image= introimg)
# bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)

username_entered = " "
name_var=tk.StringVar()

def leaderboard_sort():
    global leader_keys
    global leader_values

    lead_wind = open("leaderboard.txt" , "r")
    leaderb = lead_wind.read()
    leader_list = leaderb.split("\n")
    userreg = {}
    
    for i in range(len(leader_list)):
        leadersplit = leader_list[i].split(":")
        userreg[leadersplit[0]] = int(leadersplit[1])

    sortedusers = dict(sorted(userreg.items(), key=lambda x:x[1]))
    leader_keys  =  list(sortedusers.keys())
    leader_values = list(sortedusers.values())

def leaderboard_menu():
    global leader_keys
    global leader_values

    lead_menu = Toplevel(window)
    lead_menu.title("Leaderboard")
    lead_menu.geometry("800x600")
    lead_menu.resizable(False, False)
    lead_canvas = Canvas(width=800 , height= 600 , bg = "blue")
    lead_canvas.pack()
    introimg = PhotoImage(file = "leaderimg.png")
    bglabel = Label(lead_menu , image= introimg)
    leaderboard_sort()
    bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)
    firstplace_text = str(leader_keys[0]) + " : " + str(leader_values[0])+ " s."
    
    first_label = Label(lead_menu , text = firstplace_text , font=('calibre',12, 'bold'),  bg="black" , fg = "gold" )
    first_label.place(x = 400 , y = 25, anchor= 'center' )

    secondplace_text = str(leader_keys[1]) + " : " + str(leader_values[1])+ " s."
    
    second_label = Label(lead_menu , text = secondplace_text , font=('calibre',10, 'bold'),  bg="black" , fg = "silver" )
    second_label.place(x = 300, y = 80, anchor= 'center' )

    thirdplace_text = str(leader_keys[2]) + " : " + str(leader_values[2]) + " s."
    
    third_label = Label(lead_menu , text = thirdplace_text , font=('calibre',10, 'bold'),  bg="black" , fg = "#CD7F32" )
    third_label.place(x = 500 , y = 90, anchor= 'center' )
    

    print(leader_keys)
    scrollbar = Scrollbar(lead_menu , bg= "black" )
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(lead_menu, yscrollcommand = scrollbar.set )
    for i in range(len(leader_keys)):
        k = i +1
        mylist.insert(END, str(k)+ ") " + str(leader_keys[i]) + " : " + str(leader_values[i])+ " s." )

    mylist.pack( side = LEFT, fill = BOTH )
    mylist.place(x = 325 , y = 300 )
    scrollbar.config( command = mylist.yview )




    lead_menu.mainloop()



def setting_window():
    global key_down
    global key_up
    global key_right
    global key_left
    global key_config

    key_window = Toplevel(window)
    key_window.title("Key Config")
    key_window.geometry("800x600")
    key_window.resizable(False, False)


    def key_arrow():
        global key_down
        global key_up
        global key_right
        global key_left
        global key_config

        key_down = "<Down>"

        key_up = "<Up>"

        key_right = "<Right>"

        key_left = "<Left>"

        key_config = "You have Chosen Key Configuration You Can Now Close The Window"

        outcome = tk.Label(key_window , text= key_config , font=('calibre',15, 'bold'),  bg="yellow" , fg = "red" )

        outcome.place(relx = 0.5 , rely = 0.7, anchor= 'center' )
        key_window.destroy()



    def key_wasd():
        global key_down
        global key_up
        global key_right
        global key_left
        global key_config

        key_down = "s"

        key_up = "w"

        key_right = "d"

        key_left = "a"

        key_config = "You have Chosen Key Configuration You Can Now Close The Window"
        outcome = tk.Label(key_window , text= key_config , font=('calibre',15, 'bold'), bg="yellow" , fg = "red" )

        outcome.place(relx = 0.5 , rely = 0.7, anchor= 'center' )

        print(key_down , key_up , key_left)
        key_window.destroy()



    introimg = PhotoImage(file = "intropng.png")
    bglabel = Label(key_window , image= introimg)
    bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)
    wasdimg = PhotoImage(file = "wasd.png") 
    arrowimg = PhotoImage(file = "arrow.png")
    
    wasdbutton = Button(key_window , image=wasdimg , bg = "yellow", fg= "white", command= key_wasd)

    wasdbutton.place(x = 100 , y = 200)

    portugbutton = Button(key_window , image=arrowimg , bg = "yellow" , fg = "white", command= key_arrow)

    portugbutton.place(x = 550 , y = 200)



    key_window.mainloop()

 
def submit():
    global username_entered
    global player_save
    username_entered=name_var.get()
    player_save["name"] = username_entered
 
    print("The name is : " + username_entered)
     
    name_var.set("")


     
user = {
    "username" : 0,
    "score" : 0 }
name_label = tk.Label(windows_canvas, text = 'Your Name', font=('calibre',10, 'bold'))

name_entry = tk.Entry(windows_canvas, textvariable = name_var, font=('calibre',10,'normal') , bg="gold")
  

sub_btn=tk.Button(windows_canvas,text = 'Submit', bg="gold", command = submit)
  
windows_canvas.create_window(650, 250, window=name_entry, height=35, width=200)
windows_canvas.create_window(650, 300 , window=sub_btn , height=50, width=200)   



def choosingateam():
    global key_down
    global username_entered
    parent = Toplevel(window)
    parent.title("Choosing a Team")
    parent.geometry("800x600")
    parent.resizable(False, False)




    

    introimg = PhotoImage(file = "intropng.png")
    bglabel = Label(parent , image= introimg)
    bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)

    if username_entered != " ":
        if key_down != " ":
            argimg = PhotoImage(file = "argimg.png")
            portimg = PhotoImage(file = "portugimg.png")
            
            argbutton = Button(parent , image=argimg , fg= "white", command= lambda :gamescreen("ronaldoface.png", "messiface.png" , 400 , 300 , 50 , 300 , 700 , 500, "messilose.png", "messiwin.png" , username_entered ,  key_up , key_down , key_right , key_left  ))

            argbutton.place(x = 100 , y = 200)

            portugbutton = Button(parent , image=portimg , fg = "white", command= lambda: gamescreen("messiface.png", "ronaldoface.png" , 400 , 300, 50 , 300 , 700 , 500 ,"ronaldolose.png" , "ronaldowin.png" , username_entered,  key_up , key_down , key_right , key_left))

            portugbutton.place(x = 550 , y = 200)
        else:                   
            error_text = "Please Choose Key Configuration"
        
            error_label = Label(parent , text = error_text , font=('calibre',15, 'bold'),  bg="yellow" , fg = "red" )
            error_label.place(relx=0.5 , rely=0.5 , anchor= 'center' )

    else:
        
        error_text = "Please Enter A Username"
        
        error_label = Label(parent , text = error_text , font=('calibre',15, 'bold'),  bg="yellow" , fg = "red" )
        error_label.place(relx=0.5 , rely=0.5 , anchor= 'center' )




    parent.mainloop()

def load_game():

    saved_text = open("gamesave.txt", "r")
    saved_text_read = saved_text.read()
    saved_list =saved_text_read.split(":")
    ball_list_numbers = saved_list[-2]
    ball_list_numbers = ball_list_numbers.replace("[" , "")
    ball_list_numbers =  ball_list_numbers.replace("]" , "")
    ball_int_list = ball_list_numbers.split(",")
    list_of_balls = []
    print(saved_list)


    for i in range(len(ball_int_list)):
        x = int(ball_int_list[i])
        list_of_balls.append(x)


    playercordsx = int(saved_list[2])

    playercordsy = int(saved_list[3])
    defendercordsx = int(saved_list[4])
    defendercordsy = int(saved_list[5])
    defender1cordsx = int(saved_list[6])
    defender1cordsy = int(saved_list[7])


    gamescreen(saved_list[0], saved_list[1],playercordsx,playercordsy ,defendercordsx , defendercordsy,defender1cordsx,defender1cordsy,saved_list[8],saved_list[9],saved_list[10],saved_list[11], saved_list[12],saved_list[13], saved_list[14], list_of_balls , int(saved_list[-1]))


def gamescreen(defendername , playername , playerxcords , playerycords , defenderxcord , defenderycord , defender1xcord, defender1ycord, loser_image_cr , winner_image_cr , username_enter, keyup = "<Up>" , keydown = "<Down>" , keyright = "<Right>" , keyleft =" <Left>", ball_number = [9, 12, 14, 22, 24, 26, 37, 40], starting_time = 0 , ):
    global player_lose
    global player_x_cord
    global player_y_cord
    global game_save_indicator
    global player_win
    global defender_dir
    global time_spent
    global start_time
    global score_balls
    global defender_movement_dir
    global username_entered
    global user
 

    child = Toplevel(window)
    child.title("World Cup")

    child.geometry("800x600")
    child.resizable(False, False)
    playground = Canvas(child, width=800 , height = 600, bg = "white")
    playground.pack()
    user["username"] = username_enter
    backimg = PhotoImage(file="backgroundimage.png")    
    maguire = PhotoImage(file="maguire.png")
    scoredimage = PhotoImage(file="scoredimg.png")

    Ramos = PhotoImage(file= defendername)
    Messi = PhotoImage(file=playername)
    bacground = playground.create_image(400, 300, image = backimg)
    player = playground.create_image(playerxcords , playerycords, image = Messi)
    defender = playground.create_image(defenderxcord, defenderycord , image = Ramos)
    defender1 = playground.create_image(defender1xcord, defender1ycord , image = Ramos)
    
    ballImg = PhotoImage(file = "ballimg.png")

    flagImg  = PhotoImage(file="boudflag.png")
    balls = []
    flags = []
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

    def save_game(event):
        global player_x_cord
        global player_y_cord
        global game_not_paused
        global time_spent
        game_not_paused = False

        playercords = playground.bbox(player)
        defedercords = playground.bbox(defender)
        defeder1cords = playground.bbox(defender1)

        player_y_cord = playercords[1] +25
        player_x_cord = playercords[0]+ 25

        defender_y_cord = defedercords[1] +25
        defender_x_cord = defedercords[0]+ 25

        defender1_y_cord = defeder1cords[1] +25
        defender1_x_cord = defeder1cords[0]+ 25


        string_cords = str(defendername) + ":" + str(playername) +":"+  str(player_x_cord) +":" + str(player_y_cord) + ":" + str(defender_x_cord) +":" + str(defender_y_cord) + ":"+ str(defender1_x_cord) + ":" + str(defender1_y_cord) + ":" +loser_image_cr  + ":" +  str(winner_image_cr)+ ":" + str(user["username"])+":" + str(keyup) + ":" + str(keydown) + ":" + str(keyright) + ":" +  str(keyleft) + ":" + str(ball_number) + ":" + str(time_spent)
        game_save = open('gamesave.txt', 'w')
        game_save.write(string_cords)

        print(string_cords)

    def saving_leaderboard():

        lead_file = open("leaderboard.txt", "a+")
        text = "\n" + user["username"] + ":" + str(user["score"]) 
        lead_file.write(text)
        lead_file.close()



    def game_paused(event):

        global game_not_paused
        global player_x_cord
        global player_y_cord

        game_not_paused = not game_not_paused
        print(game_not_paused)

        child.update()

    time_spent = starting_time
    def time_played():
        global time_spent
        if game_not_paused == True:
            time_spent += 1
        playground.after(1000 , time_played)


    playground.after(1000, time_played)



    def cheatcode_maguire(event):
        

        global cheatend
        
        cheatend = not cheatend

        print(cheatend , "After Cheat")
        if cheatend:

            playground.itemconfig( defender , image = maguire)
            playground.itemconfig( defender1 , image = maguire)
        else:
            playground.itemconfig( defender , image = Ramos)
            playground.itemconfig( defender1 , image = Ramos)


    for i in range(16):
        for j in range(12):
            if grid[j][i]==0:
                continue
            elif grid[j][i]==1:
                temp_flag = playground.create_image(i*50+25 , j*50+25, image = flagImg)
                flags.append(temp_flag)

            elif grid [j][i] == 2:
                temp_ball = playground.create_image(i*50+25 , j*50+25, image = scoredimage)
                balls.append(temp_ball)
 
    balls = ball_number

    for i in range(len(balls)):
        playground.itemconfig(balls[i], image = ballImg)

    
        

    def ball_collision():
        global balls_collected
        print(len(balls))
        playerboundry = playground.bbox(player)
        playerleft = playerboundry[0]
        playerright = playerboundry[2]
        playertop = playerboundry[1]
        playerbottom = playerboundry[3]
    
        for i in range(len(balls)):

            temporary_ball = balls[i]
            temp_ball_cords = playground.bbox(temporary_ball)

            if temp_ball_cords[0] < playerboundry[0] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[3]< temp_ball_cords[3]:

                playground.itemconfig(balls[i] , image = scoredimage)
                balls_collected = balls_collected + 1
                balls.pop(i)
            elif temp_ball_cords[0] < playerboundry[2] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[3]< temp_ball_cords[3]: 
                playground.itemconfig( balls[i]  , image = scoredimage)

                balls_collected += balls_collected + 1

                balls.pop(i)
            elif temp_ball_cords[0] < playerboundry[0] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[1]< temp_ball_cords[3]:
                playground.itemconfig( balls[i]  , image = scoredimage)

                balls_collected += balls_collected + 1

                balls.pop(i)
            elif temp_ball_cords[0] < playerboundry[2] < temp_ball_cords[2] and temp_ball_cords[1] < playerboundry[1]< temp_ball_cords[3]:
                playground.itemconfig(balls[i]  , image = scoredimage)
                balls_collected = balls_collected + 1
                balls.pop(i)
    defender_movement_dir = [0,0]

    def collision_detection(obj , direction):
        global movedir

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


            if  flagleft< playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 1: 
                playground.move(obj ,-10,0)


            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 2: 
                playground.move(obj, 10 , 0)


            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom and direction == 4:
                playground.move(obj, 0 , -10)

            elif flagleft < playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 3:
                playground.move(obj, 0 , 10)

    # def collision_detection_defender(obj):


    #     for i in range(len(flags)):
    #         flag_boudry = playground.bbox(flags[i])
    #         flagleft = flag_boudry[0]
    #         flagright = flag_boudry[2]
    #         flagtop = flag_boudry[1]
    #         flagbottom = flag_boudry[3]

    #         playerboundry = playground.bbox(obj)
    #         playerleft = playerboundry[0]
    #         playerright = playerboundry[2]
    #         playertop = playerboundry[1]
    #         playerbottom = playerboundry[3]


    #         if  flagleft< playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom: 
    #             playground.move(obj ,-10,0)


    #         elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom: 
    #             playground.move(obj, 10 , 10)


    #         elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom:
    #             playground.move(obj, 0 , -10)

    #         elif flagleft < playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom:
    #             playground.move(obj, 0 , 10)

    def player_win_func():
        global player_win
        global time_spent
        global user

        global time_spent
        if len(balls)==0:

            user["score"] = time_spent
            saving_leaderboard()

            player_win = True

    def boundry_reach(obj):
        boundry_reached = False
        playerboundry = playground.bbox(obj)
        playerleft = playerboundry[0]
        playerright = playerboundry[2]
        playertop = playerboundry[1]
        playerbottom = playerboundry[3]
        if playerleft <10:
            playground.move(obj,10 , 0)
            boundry_reached = True
        elif playerright > 790 :
            playground.move(obj,-10 , 0)
            boundry_reached = True
        elif playertop < 10:
            playground.move(obj,0 , 10)
            boundry_reached = True
        elif playerbottom >590:
            playground.move(obj,0 , -10)
            boundry_reached = True

    def player_defender_collision(defender_name):
        global player_lose
 
        defenderpos_boudry = playground.bbox(defender_name)
        defenderposleft = defenderpos_boudry[0]
        defenderposright = defenderpos_boudry[2]
        defenderpostop = defenderpos_boudry[1]
        defenderposbottom = defenderpos_boudry[3]

        playerboundry = playground.bbox(player)
        playerleft = playerboundry[0]
        playerright = playerboundry[2]
        playertop = playerboundry[1]
        playerbottom = playerboundry[3]


        if  defenderposleft< playerboundry[2] < defenderposright and defenderpostop < playerboundry[1]< defenderposbottom: 
            player_lose = True
            print("Defender Touched Player")



        elif defenderposleft < playerboundry[0] < defenderposright and defenderpostop < playerboundry[1]< defenderposbottom: 

            player_lose = True
            print("Defender Touched Player")
            print(player_lose)


        elif defenderposleft < playerboundry[0] < defenderposright and defenderpostop < playerboundry[3]< defenderposbottom:
            player_lose = True
            print("Defender Touched Player")
            print(player_lose)


        elif defenderposleft < playerboundry[2] < defenderposright and defenderpostop < playerboundry[3]< defenderposbottom:
            player_lose = True
            print("Defender Touched Player")
            print(player_lose)

    def player_lost():
        if player_lose:
            child.destroy()
            loserpage = Toplevel(window)
            loserpage.title("Loser Page")
            loserpage.geometry("800x600")
            loserpage.resizable(False, False)


            loser_canvas = Canvas(loserpage, width=800 , height=600 , bg = "blue")
            loser_canvas.pack()


            loser_image_png = PhotoImage( file= loser_image_cr)

            loser_canvas.create_image(400 , 300 , image = loser_image_png)

            loserpage.mainloop()

    def player_won():
        global time_spent
        if player_win:
            child.destroy()
            loserpage = Toplevel(window)
            loserpage.title("Winner Page")
            loserpage.geometry("800x600")
            loserpage.resizable(False, False)


            loser_canvas = Canvas(loserpage, width=800 , height=600 , bg = "blue")


            loser_image_png = PhotoImage( file= winner_image_cr)
            
            loser_canvas.create_image(400 , 300 , image = loser_image_png)
            loser_canvas.create_text(100 , 30 , text="Time Spent: "+ str(time_spent) , fill = "gold" , font=('Helvetica 20 bold'))
            loser_canvas.pack()

            loserpage.mainloop()

    def moverightdef(against , z):
        global velocityofdef
        global defender_movement_dir
        velocityofdef = 20
        defender_movement_dir[z] = 1

        playground.move(against,8 , 0)

        boundry_reach(against)
        collision_detection(against  , 1)

    def moveleftdef(against , z):
        global velocityofdef
        velocityofdef = 20
        defender_movement_dir[z] = 2


        playground.move(against, -8, 0)
        boundry_reach(against)
        collision_detection(against  , 2)


    def moveupdef(against , z):
        global velocityofdef
        global defender_movement_dir
        velocityofdef = 20
        defender_movement_dir[z] = 3

        playground.move(against , 0 ,8)
        boundry_reach(against)
        collision_detection(against  , 3)
    

    def movedowndef(against, z):
        global velocityofdef
        global defender_dir

        defender_movement_dir[z] = 4

        playground.move(against , 0 , -8)

        boundry_reach(against)
        collision_detection(against  , 4)
    

    def moveright(event):
        global movedir
        movedir = 1
        if game_not_paused:
              playground.move(player , 10 , 0)
        boundry_reach(player)
        collision_detection(player, movedir)
        ball_collision()
        player_defender_collision(defender)
        player_defender_collision(defender1)
        player_lost()
        player_win_func()
        player_won()
        # time_calculate()

    def moveleft(event):
        global movedir
        movedir = 2
        if game_not_paused:
            playground.move(player , -10 , 0)
        boundry_reach(player)
        collision_detection(player , movedir)
        ball_collision()
        player_defender_collision(defender)
        player_defender_collision(defender1)
        player_lost()
        player_win_func()
        player_won()
        # time_calculate()
        
    def moveup(event):
        global movedir
        movedir = 3
        if game_not_paused:
            playground.move(player , 0 , -10)
        boundry_reach(player)
        collision_detection(player, movedir)
        ball_collision()
        player_defender_collision(defender)
        player_defender_collision(defender1)
        player_lost()
        player_win_func()
        player_won()
        # time_calculate()
               
    

    def movedown(event):
        global movedir
        movedir = 4
        if game_not_paused:
            playground.move(player , 0 , 10)
        boundry_reach(player)
        collision_detection(player, movedir)
        ball_collision()
        player_defender_collision(defender)
        player_defender_collision(defender1)
        player_lost()
        player_win_func()
        player_won()
        # time_calculate()
               


    def defendermoverand():


        global velocityofdef
        global defender_movement_dir
        if game_not_paused:
            if cheatend == True: velocityofdef = 0
            elif cheatend == False:
                x = random.randint(1, 4)
                if x == 1:
                    movedowndef(defender, 0)
                
                elif x == 2:
                    moveupdef(defender, 0)

                elif x == 3:
                    moveleftdef(defender, 0)

                elif x == 4:
          
                    moverightdef(defender, 0)
        else: child.update()

        playground.after(60, defendermoverand)


    def defendermoverand1():
        if game_not_paused:
            if cheatend == True: velocityofdef = 0
            elif cheatend == False:
                x = random.randint(1, 4)
                if x == 1:
                    movedowndef(defender1, 1)
                elif x == 2:
                    moveupdef(defender1, 1)
                elif x == 3:
                    moveleftdef(defender1, 1)
                elif x == 4:
                    moverightdef(defender1, 1)
                    

        else: child.update()
        playground.after(60, defendermoverand1)

    def bosskey(event):
        global game_not_paused

        bosskey1 = Toplevel(child)
        bosskey1.geometry("1920x1080")
        bossimg = PhotoImage(file = "bosskey.png")
        boss_canvas = Canvas(bosskey1, width=1920, height= 1080)
        boss_canvas.pack()

        game_not_paused = False
        bossplace = boss_canvas.create_image(0 , 0 , anchor = NW , image = bossimg)
        bosskey1.mainloop()

    score_displayer = playground.create_text(120 , 20 , text=" " ,fill = "gold" , font=('Helvetica 20 bold'))
    def score_display():
 
        score_balls = 8 - len(balls)
        scorre_balls_str = "Score: " + str(score_balls)+ "/8"
        
        playground.itemconfig(score_displayer , text = scorre_balls_str )
        child.update()
        playground.after(100 , score_display)
        
    time_displayer = playground.create_text(520 , 20 , text=" " ,fill = "gold" , font=('Helvetica 20 bold'))
    def time_display():
        playground.itemconfig(time_displayer , text = "Time spent: " + str(time_spent) + " seconds") 

        playground.after(500 , time_display)

    time_display()
    score_display()
    playground.bind_all(keyright, moveright)
    playground.bind_all(keyleft, moveleft)
    playground.bind_all(keyup, moveup)
    playground.bind_all(keydown, movedown)
    playground.bind_all("p", game_paused)
    playground.bind_all("m", cheatcode_maguire)

    playground.after(75, defendermoverand)
    playground.after(75, defendermoverand1) 
    playground.bind_all("x", bosskey)
    playground.bind_all("k" ,save_game)
    playground.bind_all("p", game_paused)



    child.mainloop()





# EMPTY 0, BORDER 1 , COIN 2

startbutton = Button(window , text ="Choose a Team and Play!", bg="gold", fg = "black",  height = 5 , width=30, command= choosingateam )

startbutton.place( x = 50 , y = 100)

leaderboardbutton = Button(window , text ="Settings", bg="gold", fg = "black",   height = 5 , width=30, command= setting_window )

leaderboardbutton.place(x = 50, y  = 200)

load_button = Button(window , text ="Load Game", bg="gold", fg = "black",  height = 5 , width=30, command= load_game )

load_button.place(x = 50 , y = 300)

leader_button = Button(window , text ="Leaderboard", bg="gold", fg = "black",   height = 5 , width=30, command= leaderboard_menu )

leader_button.place(x = 50 , y = 400)

window.mainloop()