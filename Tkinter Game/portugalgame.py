#Screen resolution is 2560x1600(Macbook M1 Air) which is a scaled version of 1440x900
#main game window is 1280x720
#the only cheat code: avoid
#pausing is with p
#boss key is x
#I have drawn the images of the character and the logo for the game myself using canva(www.canva.com)
#us left and right arrow key to move
from tkinter import *
from random import randint
from sys import exit
import os
#the variable that makes block come faster
hard = 5
#all obstacles
objects = []
#movement velocity
vel = 20
#game status
status = True
#score of the user
score = 0
#choosing character color
def choose_character(color):
    global img_path
    if color == "green":
        img_path = "Images/theguy.png"
    elif color == "purple":
        img_path = "Images/theguy2.png"
    else:
        img_path = "Images/theguy3.png"
    return img_path
#saving the game
def save_game():
    save_file = open("save.txt", "w")
    text = user["username"] + ":"+str(user["score"])#writing username and score to file
    save_file.write(text+"\n")
    save_file.close()
    save_file = open("save.txt", "a+")
    for i in objects:
        each_coords = my_canvas.coords(i)
        save_file.write(str(each_coords)+",")#appending coords of each obstacle
    save_file.write(str(my_canvas.coords(theguy))+",")
    save_file.write(str(hard)+",")
    if 'img_path' in globals():
        save_file.write(img_path)
    else: 
        save_file.write("Images/theguy.png")
    save_file.close()
#getting leaderboard file username and score
def get_leader():
    file = open("leaderboard.txt", "r")
    content = file.read().split("\n")
    file.close()
    return content
#saving user and score to a leaderboard file
def saving_leaderboard():

    lead_file = open("leaderboard.txt", "a+")
    text = user["username"] + ":"+str(user["score"])
    lead_file.write(text+"\n")
    lead_file.close()
#user dictionary create
def user_create():
    if user_entry.get():
        global user
        global username
        username = user_entry.get() #creating the user name based on the entry value
        user_entry.delete(0, END)
        user = {
        "username" : username,
        "score" : score
        }
        App()
        return user
#boss_key
def boss_key(event):
    global status
    if status == True:
        status = False
        global boss
        #creating the nwe window to show image
        boss = Toplevel(window)
        window.withdraw()
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight() - 500
        x = (ws/2) - (1280/2)
        y = (hs/2) - (720/2)
        boss.geometry('%dx%d+%d+%d' % (1280, 720, x, y))
        boss.configure(background="black")
        boss.title("Work stuff")
        boss_img = PhotoImage(file="Images/boss.png")
        boss_canvas = Canvas(boss, width = 1280, height = 720)
        boss_canvas.pack()
        for_boss = boss_canvas.create_image(0, 0, anchor=NW, image=boss_img)
        boss.bind("<x>", boss_key)
        boss.mainloop()
    else:
        status = True
        boss.destroy()
        window.deiconify()
        move_obstacles()
    return status
#cheat check
def cheat_code():
    global hard
    code = cheat_entry.get()
    print(code)
    if code == "avoid":
        hard = 0
        cheat_entry.delete(0, END)
        return hard
#pause menu
def pause_game(event):
    global status
    if status == True:
        status = False
        global pause
        global cheat_entry
        pause = Toplevel(window)
        pause.title("Pause Menu")
        ws = window.winfo_width() + 150
        hs = window.winfo_height()
        xx = (ws/2) - (500/2)
        yy = (hs/2) - (500/2)
        pause.geometry('%dx%d+%d+%d' % (500, 500, xx, yy))
        pause.config(bg="black", pady=40)
        pause.focus_set()
        pause.bind("<p>", pause_game)

        pause_frame = Frame(pause, bg ="black")
        pause_frame.pack()

        cheat_entry = Entry(pause_frame,)
        cheat_entry.grid(row=0, column=1, padx=10, ipady = 5 )
        enter_button = Button(pause_frame, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="Enter Code", command=lambda: cheat_code(), font=('Aerial', 22), activebackground = "yellow")
        enter_button.grid(row=0, column=0)
        continue_button = Button(pause_frame, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="Continue", command=lambda: pause_game(event), font=('Aerial', 22), activebackground = "yellow")
        continue_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2, ipadx=30)
        save_button = Button(pause_frame, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="Save", command=lambda: save_game(), font=('Aerial', 22), activebackground = "yellow")
        save_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2, ipadx=30)
        quit_button = Button(pause_frame, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='red', text="Quit", command=lambda: window.destroy(), font=('Aerial', 22), activebackground = "yellow")
        quit_button.grid(row=3, column=0, pady=10, padx=10, columnspan=2, ipadx=30)

        pause.mainloop()
    else:
        status = True
        pause.destroy()
        add_score()
        move_obstacles()
    return status
#showing score on Screen
def show_score():
    global score
    global user
    score_text = "Score: " + str(user["score"])
    score_label = Label(window, text=score_text, font=('Aerial', 22), fg = "yellow", bg ="#363636")
    score_label.place(x=2, y=10)
    username_text = str(user["username"])
    username_label = Label(window, text=username_text, font=('Aerial', 22), fg = "yellow", bg ="#363636")
    username_label.place(x=2, y=40)
    window.update()
#add score every second survived
def add_score():
    global score
    score = int(user["score"])
    if status == True:
        score += 1
        user["score"] = score #updating user score to be able to save
        show_score()
        window.after(2500, add_score)
    return score
#increase the hard to make obstacles move faster
def make_hard():
    global hard
    if hard != 25: #adding obstacle speed until 25
        hard += 1
        window.after(3000, make_hard)
        return hard
    else: return
#popup when lost
def modal_lost():
    global lost
    global score
    global user
    user["score"] = str(score)
    saving_leaderboard()
    content = get_leader()
    lost = Toplevel(window)
    lost.title("Game over")
    ws = window.winfo_width() + 150
    hs = window.winfo_height()
    xx = (ws/2) - (500/2)
    yy = (hs/2) - (500/2)
    lost.geometry('%dx%d+%d+%d' % (500, 500, xx, yy))
    lost.config(bg="black")
    lost.focus_set()
    lost_text = "You lost " + user["username"]+", do You want to Restart or Quit? \n \n" + "Your score : " + user["score"]
    #Create a Label Text
    label = Label(lost, text=lost_text,
    font=('Aerial', 22), bg='black', fg = "yellow")
    label.pack()
     # Add a Frame
    frame = Frame(lost, bd = 0)
    frame.pack(pady=10)
    # Add Button for making selection
    button1 = Button(frame, cursor="hand2", bd = 0, highlightbackground='yellow', fg='green', text="Resart", command=lambda: restart(), font=('Aerial', 22), activebackground = "#9e8c03")
    button1.grid(row=0, column=1)
    button2 = Button(frame, bd = 0, cursor="hand2", highlightbackground='yellow', fg='red', text="Quit", command=lambda: window.destroy(), font=('Aerial', 22), activebackground = "#9e8c03")
    button2.grid(row=0, column=2)

    scrollbar = Scrollbar(lost)
    scrollbar.pack(side=RIGHT, fill=Y)

    scores_leader = Listbox(lost, yscrollcommand=scrollbar.set, bg="black", font=('Aerial', 22), fg="Yellow", bd=2, highlightbackground = "Yellow", highlightcolor= "Yellow", highlightthickness=2)
    for i in content:
        scores_leader.insert(END, i)
        scores_leader.pack(fill=BOTH, padx=10, pady=7)

    scrollbar.config(command=scores_leader.yview)

    lost.mainloop()
#function to Restart
def restart():
    #rerunning the file
    os.execl(sys.executable, sys.executable, *sys.argv)
#function for configuring the window
def configure_window(w, h):
    #main window configuration basing on screen width and length
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight() - 500
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(background="black")
    return window
#move theguy (our character)
def move_guy(event):
    global status
    global vel
    position = my_canvas.coords(theguy)
    #making sure that our character doesn't go over the edges
    if event.keysym == 'Left' and position[0] > 0 and status == True:
        x = -vel
        my_canvas.move(theguy, x, 0)
    elif event.keysym == 'Right' and position[0]+guy_width < canvas_width and status == True:
        x = vel
        my_canvas.move(theguy, x, 0)
#moving obstacles
def move_obstacles():
    y = 0
    for i in objects:
        coords = my_canvas.coords(i)
        if coords[1] >= 720:
            y = randint(-1300, -730)
            if coords[0] <= 1120 and coords[0] % 160 == 0:
                x = 80
            else:
                x = -80
            my_canvas.move(i, x, y)
        else:
            y = hard
            my_canvas.move(i, 0, y)
    if status == True:
        window.after(30, move_obstacles)
        #using the status boolean in case of pause and boss key
#creating obstacles
def create_objects():

        global count
        x1 = 0
        y1 = 0
        spawn = 0
        width = 40
        height = 40
        for i in range(8):
            #divided the screen on 8 equal sections of 160 
            obj_square = my_canvas.create_rectangle(x1+spawn, y1, x1+spawn + width, y1 + height, outline="yellow", fill="yellow")
            objects.append(obj_square)
            spawn+=160
            decision = randint(0,3)
            if decision == 0:
                y1 = 0
            else: y1 -= randint(20, 120)
        window.after(30, move_obstacles)
        #if count < 1:
        #    window.after(400, create_objects)
        #count +=1
        return objects
#checking for collision
def check_collision():
    global status
    guycords = my_canvas.coords(theguy)
    for i in objects:
        cords = my_canvas.coords(i)
        if guycords[0] - cords[0] <= 40 and guycords[0] - cords[0] >= -80 and guycords[1] - cords[1] <= 40 and guycords[1] - cords[1] >= -80:
            status = False
            modal_lost()
            return
    window.after(25, check_collision)
#game app
def App():
    global window
    global theguy
    global my_canvas
    global guy_width
    global guy_height
    global canvas_width
    global canvas_height
    menu.destroy()
    window = Tk()
    window_width = 1280
    window_height = 720
    configure_window(window_width, window_height)
    window.title("Avoid Them")
    canvas_width = 1280
    canvas_height = 720
    my_canvas = Canvas(window, width = canvas_width, height = canvas_height, bg = 'black')
    my_canvas.pack()
    if 'img_path' in globals():
        theguyimg = PhotoImage(file=img_path)
    else:
        theguyimg = PhotoImage(file="Images/theguy.png")
    guy_width = 80
    guy_height = 80
    theguy = my_canvas.create_image(600,640, anchor=NW, image=theguyimg)

    create_objects()
    show_score()
    window.after(25, check_collision)
    window.after(2500, make_hard)
    window.after(2500, add_score)
    window.bind("<Left>", move_guy)
    window.bind("<Right>", move_guy)
    window.bind("<p>", pause_game)
    window.bind("<x>", boss_key)


    window.mainloop()
#game app when loading a saved game
def load_game():
    global user
    global window
    global theguy
    global my_canvas
    global guy_width
    global guy_height
    global canvas_width
    global canvas_height
    menu.destroy()
    window = Tk()
    window_width = 1280
    window_height = 720
    configure_window(window_width, window_height)
    window.title("Avoid Them")
    canvas_width = 1280
    canvas_height = 720
    my_canvas = Canvas(window, width = canvas_width, height = canvas_height, bg = 'black')
    my_canvas.pack()
    guy_width = 80
    guy_height = 80

    load_file = open("save.txt", "r")
    load_line = load_file.readline()
    username = load_line.split(":")[0]
    score = int(load_line.split(":")[1])
    user = {
    "username" : username,
    "score" : score
    }
    load_content = load_file.read().replace("[",'').replace("]",'').replace("\n",'').split(",")
    print(load_content)
    for i in range(0, len(load_content)-4,4):
        x1 = float(load_content[i])
        y1 = float(load_content[i+1])
        x2 = float(load_content[i+2])
        y2 = float(load_content[i+3])
        obj_square = my_canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", fill="yellow")
        objects.append(obj_square)
    guy_x = float(load_content[32])
    guy_y = float(load_content[33])
    hard = int(load_content[34])
    img_path = str(load_content[35])
    theguyimg = PhotoImage(file=img_path)
    theguy = my_canvas.create_image(guy_x, guy_y, anchor=NW, image=theguyimg)

    load_file.close()
    os.remove("save.txt")
    window.after(30, move_obstacles)
    show_score()
    window.after(25, check_collision)
    window.after(2500, make_hard)
    window.after(2500, add_score)
    window.bind("<Left>", move_guy)
    window.bind("<Right>", move_guy)
    window.bind("<p>", pause_game)
    window.bind("<x>", boss_key)


    window.mainloop()
#Main menu
def main_menu():
    global menu
    global user_entry
    menu = Tk()
    menu_width = 500
    menu_height = 700
    ws = menu.winfo_screenwidth()
    hs = menu.winfo_screenheight()-100
    x = (ws/2) - (menu_width/2)
    y = (hs/2) - (menu_height/2)
    menu.geometry('%dx%d+%d+%d' % (menu_width, menu_height, x, y))
    menu.title("Avoid them")
    menu.configure(background="black")
    menu.focus_set()
    menu_canvas = Canvas(menu, width = menu_width, height = menu_height, bg ="black")
    menu_canvas.pack()
    game_logo = PhotoImage(file="Images/gameLogo.png")
    logo_image = menu_canvas.create_image(50,50, anchor=NW, image=game_logo)

    user_enter_label = Label(menu_canvas, bg = 'black', bd = 0, fg='white', text="Enter Username: ", font=('Aerial', 30), activebackground = "yellow", height=1)
    user_enter_label.place(x=20, y=260)
    user_entry = Entry(menu_canvas, font=('Aerial', 30), bd=0, width=10)
    user_entry.place(x=290, y=260)
    start_button = Button(menu_canvas, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="START GAME", command=lambda: user_create(), font=('Aerial', 30), activebackground = "yellow", height=1)
    start_button.place(x=20, y=350)
    quit_b = Button(menu_canvas, bd = 0, cursor="hand2", highlightbackground='yellow', fg='red', text="Quit", command=lambda: menu.destroy(), font=('Aerial', 30), activebackground = "#9e8c03")
    quit_b.place(x=20, y=440)

    choosing_character_button1 = Button(menu_canvas, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="Select Green", command=lambda: choose_character("green"), font=('Aerial', 30), activebackground = "yellow", height=1)
    choosing_character_button1.place(x=290, y=350)
    choosing_character_button2 = Button(menu_canvas, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='Purple', text="Select Purple", command=lambda: choose_character("purple"), font=('Aerial', 30), activebackground = "yellow", height=1)
    choosing_character_button2.place(x=290, y=440)
    choosing_character_button3 = Button(menu_canvas, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='#db187d', text="Select Pink", command=lambda: choose_character("pink"), font=('Aerial', 30), activebackground = "yellow", height=1)
    choosing_character_button3.place(x=290, y=530)
    if os.path.isfile('save.txt') == True:
        load_button = Button(menu_canvas, bg = 'yellow', bd = 0, cursor="hand2", highlightbackground='yellow', fg='green', text="LOAD GAME", command=lambda: load_game(), font=('Aerial', 30), activebackground = "yellow", height=1)
        load_button.place(x=20, y=530)

    menu.mainloop()
main_menu()