from random import *
import tkinter as tk
from PIL import Image , ImageTk

game_list = ['rock' , 'paper', 'scissor']
winlabel=''
ulabel=''
clabel=''
upoint=0
cpoint=0


def winnerChoice(user):
    global winlabel , ulabel , clabel , upoint , cpoint
    cc = randint(0,2)
    computer = game_list[cc]
    if user==computer:
        winlabel.config(text='Draw' , fg='black')
    elif (
        (user=='rock' and computer=='scissor') or
        (user=='scissor' and computer=='paper') or
        (user=='paper' and computer=='rock')
          ):
        upoint+=1
        winlabel.config(text='Win',fg='green')
    else:
        cpoint+=1
        winlabel.config(text='Lose',fg='red')
        
    ulabel.config(text=f'user :\n{user}\n{upoint}')
    clabel.config(text=f'Computer :\n{computer}\n{cpoint}')



root = tk.Tk()
root.geometry('1000x400')
title = tk.Label(root , text='Game' , font=('bold',30))
title.place(x=440 , y=0)

rock_img = Image.open('images\\rock.jpg')
rock_img = rock_img.resize([100,100])
rock_img = ImageTk.PhotoImage(rock_img)
rock_btn = tk.Button(root , image=rock_img , command=lambda:winnerChoice('rock'))
rock_btn.place(x=200 , y=100)

paper_img = Image.open('images\\paper.png')
paper_img = paper_img.resize([100,100])
paper_img = ImageTk.PhotoImage(paper_img)
paper_btn = tk.Button(root , image=paper_img, command=lambda:winnerChoice('paper'))
paper_btn.place(x=440 , y=100)

scissor_img = Image.open('images\\scissor.png')
scissor_img = scissor_img.resize([100,100])
scissor_img = ImageTk.PhotoImage(scissor_img)
scissor_btn = tk.Button(root , image=scissor_img, command=lambda:winnerChoice('scissor'))
scissor_btn.place(x=670 , y=100)

winlabel = tk.Label(text='' , font=('bold',22))
winlabel.place(x=450,y=300)

ulabel = tk.Label(text=f'user\n{upoint}' , font=('bold',22))
ulabel.place(x=110,y=250)

clabel = tk.Label(text=f'computer\n{cpoint}' , font=('bold',22))
clabel.place(x=790,y=250)

root.mainloop()





