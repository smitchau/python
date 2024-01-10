from tkinter import *
from random import choice

root = Tk()
root.geometry("550x550")
root.title("My Game")
root.resizable(False, False)

heading = Label(root, text="Stone Paper Scissors", font=("arial 25 bold"), bg='black', fg='white')
heading.place(x=110, y=50)

user_scores = [0]
computer_scores = [0]

def game(user_take):
    print("user :",user_take)
    computer_choice = choice(['ROCK','PAPER','SCISSIOR'])
    print("computer :",computer_choice)
    if user_take == computer_choice:
        result = "It's a tie!"
        print(result,"\n")

    elif ((user_take == 'ROCK' and computer_choice == 'SCISSOR')
        or(user_take == 'PAPER' and computer_choice == 'ROCK')
        or(user_take == 'SCISSOR' and computer_choice == 'PAPER')):
        result = "USER WIN !"
        user_scores[0] += 1
        print(result,"\n")

    else:
        result = "COMPUTER WIN !"
        computer_scores[0] += 1
        print(result,"\n")

    update_scores()
    #label_result["text"] = (f"\n{result}\nUser Choice {user_take}, computer choice {computer_choice}")

def update_scores():
    #label_User["text"] = f"User: {user_scores[0]}"
    #label_computer["text"] = f"Computer: {computer_scores[0]}"
    pass

rock = Button(root, text="ROCK", font=("arial 20 bold"), bg='dark blue', fg='white', command=lambda: game("ROCK"))
rock.place(x=40, y=150)

paper = Button(root, text="PAPER", font=("arial 20 bold"), bg='dark blue', fg='white', command=lambda: game("PAPER"))
paper.place(x=190, y=150)

scissor = Button(root, text="SCISSOR", font=("arial 20 bold"), bg='dark blue', fg='white', command=lambda: game("SCISSOR"))
scissor.place(x=350, y=150)

user_label = Label(root, text="User", font=("arial 25 bold"), bg='black', fg='white')
user_label.place(x=60, y=250)

user_choice_label = Label(root, text= '', font=("arial 25 bold"), fg='purple')
user_choice_label.place(x=200, y=250)

computer_label = Label(root, text="Computer", font=("arial 25 bold"), bg='black', fg='white')
computer_label.place(x=60, y=350)

computer_choice_label = Label(root, text= '' , font=("arial 25 bold"), fg='purple')
computer_choice_label.place(x=250, y=350)

root.mainloop()
