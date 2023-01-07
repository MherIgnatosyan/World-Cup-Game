# The aim of this game is to collect all the availble balls to win the gam ehowever you have 2 defenders to play against...
# Its World Cup Final Argentina vs Portugal ... Messi vs Ronaldo ...
# You can choose to play either as Argentina( Messi ) or Portugal (Ronaldo) ...
# The game resolution is 800X600...
# You can choose key configuration in Settings menu...
# You can see the leaders of this increadible game in Leaderboard menu...
# The hidden cheat code is "ma" it will stop the defenders from moving...
# By pressing k you can save your game...
# By pressing p you can pause your game...
#I hope you enjoy it!

import random
import tkinter as tk
from tkinter import *
from timeit import default_timer as timer
#Defining all the global variables used in the game 
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
#Creating the starting menu
window = Tk()
window.geometry("800x600")
window.title("World Cup")
window.resizable(False, False)
windows_canvas = Canvas(width=800 , height= 600 , bg = "white" )
windows_canvas.pack()
introimg = PhotoImage(file = "intropng.png")
windows_canvas.create_image(400 , 300 , image = introimg)
username_entered = ""
name_var=tk.StringVar()
#Creating the leaderboard
def leaderboard_sort():
    global leader_keys
    global leader_values
    # Redaing from the text file the leaders names and their scores
    lead_wind = open("leaderboard.txt" , "r")
    leaderb = lead_wind.read()
    leader_list = leaderb.split("\n") 
    userreg = {}
    
    for i in range(len(leader_list)):
        leadersplit = leader_list[i].split(":")
        userreg[leadersplit[0]] = int(leadersplit[1])
    #sortng player names by their values from low numbers to high
    sortedusers = dict(sorted(userreg.items(), key=lambda x:x[1]))
    leader_keys  =  list(sortedusers.keys())
    leader_values = list(sortedusers.values())
#leadeboard window
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
    first_label = Label(lead_menu , text = firstplace_text , font=('calibre',12, 'bold'),  bg="black" , fg = "gold" ) # First place label
    first_label.place(x = 400 , y = 25, anchor= 'center' )

    secondplace_text = str(leader_keys[1]) + " : " + str(leader_values[1])+ " s."
    second_label = Label(lead_menu , text = secondplace_text , font=('calibre',10, 'bold'),  bg="black" , fg = "silver" ) #Second place label
    second_label.place(x = 300, y = 80, anchor= 'center' )

    thirdplace_text = str(leader_keys[2]) + " : " + str(leader_values[2]) + " s."
    third_label = Label(lead_menu , text = thirdplace_text , font=('calibre',10, 'bold'),  bg="black" , fg = "#CD7F32" )# Third place label
    third_label.place(x = 500 , y = 90, anchor= 'center' )
    
    scrollbar = Scrollbar(lead_menu , bg= "black" ) #Creating a scrollbarr for all the players names and scores
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(lead_menu, yscrollcommand = scrollbar.set, font=('calibre',12, 'bold') , height= 300, bg = "gold" , highlightcolor = "black" , highlightthickness = 5 )
    for i in range(len(leader_keys)):
        k = i +1
        mylist.insert(END, str(k)+ ") " + str(leader_keys[i]) + " : " + str(leader_values[i])+ " s." )
    mylist.pack( side = LEFT, fill = BOTH )
    mylist.place(x = 315 , y = 300 )
    scrollbar.config( command = mylist.yview)

    lead_menu.mainloop()

# Creating Setting menu
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

    # Thi fuction will assign keys that are used for moving the player to arrows
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

    # Thi fuction will assign keys that are used for moving the player to W A S D
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
    
    wasdbutton = Button(key_window , image=wasdimg , bg = "yellow", fg= "white", command= key_wasd) # Button for choosing W A S D
    wasdbutton.place(x = 100 , y = 200)

    portugbutton = Button(key_window , image=arrowimg , bg = "yellow" , fg = "white", command= key_arrow)# Button for choosing arrows
    portugbutton.place(x = 550 , y = 200)

    key_window.mainloop()

#Submit function to get the username ented by the player
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

name_entry = tk.Entry(windows_canvas, textvariable = name_var, selectborderwidth = 4, font=('calibre',10,'normal') , bg="white") # Name entry 
  
sub_btn=tk.Button(windows_canvas,text = 'Submit', bg="gold",bd = 4, relief= GROOVE ,  command = submit) # Submmision Button

windows_canvas.create_window(650, 250, window=name_entry, height=35, width=200)
windows_canvas.create_window(650, 300 , window=sub_btn , height=50, width=200)   

# Creating wndow to choose the team player want o play
def choosingateam():
    global key_down
    global username_entered
    global cheatend
    global game_not_paused

    parent = Toplevel(window)
    parent.title("Choosing a Team")
    parent.geometry("800x600")
    parent.resizable(False, False)
    introimg = PhotoImage(file = "intropng.png")
    bglabel = Label(parent , image= introimg)
    bglabel.place(x = 0 , y = 0, relheight=1, relwidth=1)
    cheatend = False
    game_not_paused = True
    def portugal_game():
        gamescreen("messiface.png", "ronaldoface.png" , 550 , 150, 50 , 300 , 500 , 500 ,"ronaldolose.png" , "ronaldowin.png" , username_entered,  key_up , key_down , key_right , key_left ,  ball_number = [9, 12, 14, 22, 24, 26, 37, 40], starting_time = 0 ) 
        parent.quit()
    def argentina_game():
        gamescreen("ronaldoface.png", "messiface.png" , 550 , 150 , 50 , 300 , 500 , 500, "messilose.png", "messiwin.png" , username_entered ,  key_up , key_down , key_right , key_left ,  ball_number = [9, 12, 14, 22, 24, 26, 37, 40], starting_time = 0 )  
        parent.quit()


    if username_entered != "": # Checking if username is entered
        if key_down != " ": # Checking if key configuration is entered
            argimg = PhotoImage(file = "argimg.png")
            portimg = PhotoImage(file = "portugimg.png")
            #Button for choosing to play for Argentina
            argbutton = Button(parent , image=argimg , fg= "white", command= argentina_game )
            argbutton.place(x = 100 , y = 200)
            #Button for choosing to play for Argentina
            portugbutton = Button(parent , image=portimg , fg = "white", command= portugal_game)
            portugbutton.place(x = 550 , y = 200)
        else:               
            #Erros messege for user to choose key configuration
            error_text = "Please Choose Key Configuration"
            error_label = Label(parent , text = error_text , font=('calibre',15, 'bold'),  bg="yellow" , fg = "red" )
            error_label.place(relx=0.5 , rely=0.5 , anchor= 'center' )
    else:
        # Error messege for the user to enter a username
        error_text = "Please Enter A Username"
        error_label = Label(parent , text = error_text , font=('calibre',15, 'bold'),  bg="yellow" , fg = "red" )
        error_label.place(relx=0.5 , rely=0.5 , anchor= 'center' )
    parent.mainloop()
# funtion for loading previosly saved game
def load_game():
    global cheatend
    global game_not_paused
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
    cheatend = False
    game_not_paused = True

    gamescreen(saved_list[0], saved_list[1],playercordsx,playercordsy ,defendercordsx , defendercordsy,defender1cordsx,defender1cordsy,saved_list[8],saved_list[9],saved_list[10],saved_list[11], saved_list[12],saved_list[13], saved_list[14], list_of_balls , int(saved_list[-1]))

# Main Game Function
def gamescreen(defendername , playername , playerxcords , playerycords , defenderxcord , defenderycord , defender1xcord, defender1ycord, loser_image_cr , winner_image_cr , username_enter, keyup, keydown , keyright , keyleft, ball_number = [9, 12, 14, 22, 24, 26, 37, 40], starting_time = 0  ):
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
    global game_not_paused
    global cheatend
    #creatng game window
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
    # Creating a matrix grid to place teh flags and balls
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
    # Saving teh game by saving teh possition of the player , defenders , score ,  key config. , username and time 
    def save_game(event):
        global player_x_cord
        global player_y_cord
        global game_not_paused
        global time_spent

        game_not_paused  = False
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

    #Saving the name and time to text file
    def saving_leaderboard():

        lead_file = open("leaderboard.txt", "a+")
        text = "\n" + user["username"] + ":" + str(user["score"]) 
        lead_file.write(text)
        lead_file.close()
    #Pausing teh game 
    def game_paused(event):

        global game_not_paused
        global player_x_cord
        global player_y_cord
        game_not_paused = not game_not_paused
        print(game_not_paused)
        
        child.update()
    #Initializing starting time
    time_spent = starting_time
    # Counting time by adding one to the time every second
    def time_played():
        global time_spent
        if game_not_paused == True:
            time_spent += 1
        playground.after(1000 , time_played)
    playground.after(1000, time_played)
    #Cheatcode stops defenders from moving making it easier for player to collect the balls
    def cheatcode_maguire(event):
        global cheatend
        cheatend = not cheatend
        if cheatend:
            playground.itemconfig( defender , image = maguire)
            playground.itemconfig( defender1 , image = maguire)
        else:
            playground.itemconfig( defender , image = Ramos)
            playground.itemconfig( defender1 , image = Ramos)
    #Creating teh map of the game
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
    # Initializing the position of teh balls
    balls = ball_number
    for i in range(len(balls)):
        playground.itemconfig(balls[i], image = ballImg)

    # Collision detection with player an dteh balls
    def ball_collision():
        global balls_collected
        playerboundry = playground.bbox(player)
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
    #collision detection beetween the player  , defenderes and flags
    def collision_detection(obj , direction):
        global movedir
        for i in range(len(flags)):
            flag_boudry = playground.bbox(flags[i])
            flagleft = flag_boudry[0]
            flagright = flag_boudry[2]
            flagtop = flag_boudry[1]
            flagbottom = flag_boudry[3]

            playerboundry = playground.bbox(obj)

            if  flagleft< playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 1: 
                playground.move(obj ,-10,0)

            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 2: 
                playground.move(obj, 10 , 0)

            elif flagleft < playerboundry[0] < flagright and flagtop < playerboundry[3]< flagbottom and direction == 4:
                playground.move(obj, 0 , -10)

            elif flagleft < playerboundry[2] < flagright and flagtop < playerboundry[1]< flagbottom and direction == 3:
                playground.move(obj, 0 , 10)
    # Player win function when all teh balls are collected
    def player_win_func():

        global player_win
        global time_spent
        global user
        global time_spent
        if len(balls)==0:

            user["score"] = time_spent
            saving_leaderboard()
            player_win = True
    # Checking the collison with the borders of the map
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
    # Checkin g the collision beetween teh player and defenders
    def player_defender_collision(defender_name):
        global player_lose
 
        defenderpos_boudry = playground.bbox(defender_name)
        defenderposleft = defenderpos_boudry[0]
        defenderposright = defenderpos_boudry[2]
        defenderpostop = defenderpos_boudry[1]
        defenderposbottom = defenderpos_boudry[3]
        playerboundry = playground.bbox(player)

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
    # If player touches defender this function works
    def player_lost():
        global username_entered
        global player_lose
        global player_win
        global game_not_paused
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
            username_entered = ""
            player_lose = False
            game_not_paused = True
            loserpage.mainloop()
    #Player win window
    def player_won():
        global time_spent
        global username_entered
        global player_win
        global game_not_paused
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
            username_entered = ""
            player_win = False
            game_not_paused = True
            loserpage.mainloop()
    #defender movement
    def moverightdef(against , z):
        global velocityofdef
        global defender_movement_dir
        velocityofdef = 20
        defender_movement_dir[z] = 1
        playground.move(against,7 , 0)
        boundry_reach(against)
        collision_detection(against  , 1)

    def moveleftdef(against , z):
        global velocityofdef
        velocityofdef = 20
        defender_movement_dir[z] = 2
        playground.move(against, -7, 0)
        boundry_reach(against)
        collision_detection(against  , 2)

    def moveupdef(against , z):
        global velocityofdef
        global defender_movement_dir
        velocityofdef = 20
        defender_movement_dir[z] = 3
        playground.move(against , 0 ,7)
        boundry_reach(against)
        collision_detection(against  , 3)

    def movedowndef(against, z):
        global velocityofdef
        global defender_dir
        defender_movement_dir[z] = 4
        playground.move(against , 0 , -7)
        boundry_reach(against)
        collision_detection(against  , 4)
    #player movement
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

    #defenders random movement
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
    #boss key function
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

    #displaying the score 
    score_displayer = playground.create_text(120 , 20 , text=" " ,fill = "gold" , font=('Helvetica 20 bold'))
    def score_display():
 
        score_balls = 8 - len(balls)
        scorre_balls_str = "Score: " + str(score_balls)+ "/8"
        
        playground.itemconfig(score_displayer , text = scorre_balls_str )
        child.update()
        playground.after(100 , score_display)
    #displaying the time 
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
    playground.bind_all("ma", cheatcode_maguire)

    playground.after(75, defendermoverand)
    playground.after(75, defendermoverand1) 
    playground.bind_all("x", bosskey)
    playground.bind_all("k" ,save_game)
    playground.bind_all("p", game_paused)

    child.mainloop()


startbutton = Button(window , text ="Choose a Team and Play!", bg="gold", fg = "black",bd = 4, relief= GROOVE ,  height = 5 , width=30, command= choosingateam )

startbutton.place( x = 50 , y = 100)

leaderboardbutton = Button(window , text ="Settings", bg="gold", fg = "black",bd = 4, relief= GROOVE ,   height = 5 , width=30, command= setting_window )

leaderboardbutton.place(x = 50, y  = 200)

load_button = Button(window , text ="Load Game", bg="gold", fg = "black",bd = 4, relief= GROOVE ,  height = 5 , width=30, command= load_game )

load_button.place(x = 50 , y = 300)

leader_button = Button(window , text ="Leaderboard", bg="gold", fg = "black", bd = 4, relief= GROOVE ,  height = 5 , width=30, command= leaderboard_menu )

leader_button.place(x = 50 , y = 400)

window.mainloop()