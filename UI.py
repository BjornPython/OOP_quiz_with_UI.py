from tkinter import *
from brain import QuizBrain

background = "#343434"
flash_card_font = "Ariel"


class QuizInterface:

    def __init__(self, q_brain: QuizBrain):
        self.brain = q_brain
        self.background = "#343434"
        self.flash_card_font = "Ariel"

        self.window = Tk()
        self.window.title("RANDOM QUIZ GAME")
        self.window.geometry("600x400")
        self.window.config(padx=50, pady=50, bg=self.background)

        self.canvas = Canvas(width=500, height=250,
                             background=self.background,
                             highlightthickness=0)

        self.front = PhotoImage(file="front.png")
        self.back = PhotoImage(file="back.png")
        self.card_background = self.canvas.create_image(250, 125, image=self.front)
        self.can_lang = self.canvas.create_text(250, 50, text="QUESTION", font=(flash_card_font, 16, "italic"))
        self.can_word = self.canvas.create_text(250, 130, text=self.brain.QandA[0]["question"],
                                                font=(flash_card_font, 16, "bold"))
        self.canvas.place(x=5, y=5)
        self.x_image = PhotoImage(file="x_mark.png")
        self.x_button = Button(image=self.x_image,
                               background=self.brain.background,
                               height=30,
                               width=30,
                               command=self.false_ans
                               )
        self.x_button.place(x=100, y=280)

        self.check_image = PhotoImage(file="check_mark.png")
        self.check_button = Button(image=self.check_image,
                                   background=self.brain.background,
                                   height=30,
                                   width=30,
                                   command=self.true_ans
                                   )
        self.check_button.place(x=380, y=280)

        self.score_label = Label(text=f"SCORE: {self.brain.score}",
                                 bg=self.brain.background, fg="white",
                                 font=("Ariel", 12, "bold"))
        self.score_label.place(x=50, y=-30)

        self.check_ans_label = Label(bg=self.brain.background, fg="white",
                                     font=("Ariel", 12, "bold"))
        self.check_ans_label.place(x=220, y=290)
        self.window.mainloop()

    def false_ans(self):
        right = self.brain.check_ans(False)
        if right == "list index out of range":
            self.canvas.itemconfig(self.can_word, text="YOU HAVE FINISHED\nALL QUESTIONS!")
            self.check_ans_label.config(text="")
        elif right:
            new_question = self.brain.new_ques()
            self.edit_text(new_question, right)
        else:
            new_question = self.brain.new_ques()
            self.edit_text(new_question, right)

    def true_ans(self):
        right = self.brain.check_ans(True)
        if right == "list index out of range":
            self.canvas.itemconfig(self.can_word, text="YOU HAVE FINISHED\nALL QUESTIONS!")
            self.check_ans_label.config(text="")
        elif right:
            new_question = self.brain.new_ques()
            self.edit_text(new_question, right)
        else:
            new_question = self.brain.new_ques()
            self.edit_text(new_question, right)

    def edit_text(self, new_ques, correct):
        if correct:
            self.canvas.itemconfig(self.can_word, text=new_ques)
            self.check_ans_label.config(text="CORRECT!")
            self.score_label.config(text=f"SCORE: {self.brain.score}")
        else:
            self.canvas.itemconfig(self.can_word, text=new_ques)
            self.check_ans_label.config(text="WRONG!")
