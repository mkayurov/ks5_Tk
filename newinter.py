from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from winsound import *
import os
import sqlite3

post_question = ""
post_answer = ""
check_post = None


class Child:


	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		self.root["bg"] = "#e0e5e6"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.root.grab_set()
		self.root.focus_set()
		self.widgets_child()
		self.menu_bar()
		
		self.select_questions = IntVar()
		self.question = StringVar()
		self.answer= StringVar()
		self.number_question = IntVar()
		self.answer_get = None
		self.question_get = None
		
	def window_update(self):
		self.root.update()
		
	def menu_bar(self):
		# func for draw menubar 
		global checked_post
		self.checked_post = StringVar()
		
		self.m = Menu(self.root)         						 			   							
		self.root.config(menu=self.m) 
		
		self.fm = Menu(self.m, tearoff=0)		
		self.m.add_cascade(label="Файл",menu=self.fm, state="normal")  
		self.fm.add_command(label="Новый", state="disabled")
		self.fm.add_separator()		
		self.fm.add_command(label="Открыть...", state="disabled")    							
		self.fm.add_command(label="Сохранить...", state="disabled")
		self.fm.add_command(label="Печать", state="normal", command=self.print_on_paper)
		self.fm.add_command(label="Выход", command=self.root.quit)
		
		self.hm = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Должность",menu=self.hm)
		self.hm.add_radiobutton(label="Машинист", state="normal", value="машинист", variable=self.checked_post, command=self.check_button_post)
		self.hm.add_radiobutton(label="Оператор", state="normal", value="оператор", variable=self.checked_post, command=self.check_button_post)
		self.hm.add_radiobutton(label="Слесарь", state="normal", value="слесарь", variable=self.checked_post, command=self.check_button_post)
		
		self.ticket_menu = Menu(self.m, tearoff=0)
		self.ticket_menu.add_command(label="билет 1", command=self.open_ticket_editing)
		self.ticket_menu.add_command(label="билет 2")
		self.ticket_menu.add_command(label="билет 3")
		self.ticket_menu.add_command(label="билет 4")
		self.ticket_menu.add_command(label="билет 5")
		self.ticket_menu.add_command(label="билет 6")
		self.ticket_menu.add_command(label="билет 7")
		self.ticket_menu.add_command(label="билет 8")
		self.ticket_menu.add_command(label="билет 9")
		self.ticket_menu.add_command(label="билет 10")
		
		self.hm = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Редактирование",menu=self.hm)
		self.hm.add_cascade(label="Билеты", menu=self.ticket_menu)    							
		self.hm.add_command(label="Настройки")

		
	def widgets_child(self):
		# func for castom widgets on window
		self.color_button = "#7d8481"
		self.active_color = "#393939"
		# frames 
		self.frm_child_1 = Frame(self.root, width=1086, height=61, bg="#93a7a6", relief=GROOVE, bd=2)
		self.frm_child_1.place(x=8, y=8)
		self.frm_child_2 = Frame(self.root, width=180, height=598, bg="#7d8481", relief=GROOVE, bd=2)
		self.frm_child_2.place(x=8, y=75)
		self.frm_child_3 = Frame(self.root, width=900, height=100, bg="#f3f7fb", relief=GROOVE, bd=2)
		self.frm_child_3.place(x=194, y=75)
		self.lbl_child_1 = Label(self.frm_child_1, font="Broadway 13", bg="#93a7a6", fg="#2f2f2f")
		self.lbl_child_1.place(x=28, y=14)
		
		# question radiobuttons
		self.rbt_question_1 = Radiobutton(self.frm_child_2, text="вопрос № 1 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=1, command=self.check_radiobutton)
		self.rbt_question_2 = Radiobutton(self.frm_child_2, text="вопрос № 2 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=2, command=self.check_radiobutton)
		self.rbt_question_3 = Radiobutton(self.frm_child_2, text="вопрос № 3 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=3, command=self.check_radiobutton)
		self.rbt_question_4 = Radiobutton(self.frm_child_2, text="вопрос № 4 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=4, command=self.check_radiobutton)
		self.rbt_question_5 = Radiobutton(self.frm_child_2, text="вопрос № 5 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=5, command=self.check_radiobutton)
		self.rbt_question_6 = Radiobutton(self.frm_child_2, text="вопрос № 6 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=6, command=self.check_radiobutton)
		self.rbt_question_7 = Radiobutton(self.frm_child_2, text="вопрос № 7 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=7, command=self.check_radiobutton)
		self.rbt_question_8 = Radiobutton(self.frm_child_2, text="вопрос № 8 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=8, command=self.check_radiobutton)
		self.rbt_question_9 = Radiobutton(self.frm_child_2, text="вопрос № 9 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=9, command=self.check_radiobutton)
		self.rbt_question_10 = Radiobutton(self.frm_child_2, text="вопрос № 10 ", font="Verdana 9 bold", activebackground="#7d8481", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=10, command=self.check_radiobutton)
		self.radiobuttons_question = [self.rbt_question_1, self.rbt_question_2, self.rbt_question_3,
																self.rbt_question_4, self.rbt_question_5, self.rbt_question_6, 
																self.rbt_question_7, self.rbt_question_8, self.rbt_question_9, self.rbt_question_10]																										
		
		# ticket button
		self.btn_ticket_1 = Button(self.frm_child_1, text="1", width=5, relief=GROOVE, font="Broadway 10", bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_1))
		self.btn_ticket_2 = Button(self.frm_child_1, text="2", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_2))
		self.btn_ticket_3 = Button(self.frm_child_1, text="3", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_3))
		self.btn_ticket_4 = Button(self.frm_child_1, text="4", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_4))
		self.btn_ticket_5 = Button(self.frm_child_1, text="5", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_5))
		self.btn_ticket_6 = Button(self.frm_child_1, text="6", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_6))
		self.btn_ticket_7 = Button(self.frm_child_1, text="7", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_7))
		self.btn_ticket_8 = Button(self.frm_child_1, text="8", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_8))
		self.btn_ticket_9 = Button(self.frm_child_1, text="9", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_9))
		self.btn_ticket_10 = Button(self.frm_child_1, text="10", width=5, relief=GROOVE, font="Broadway 10",bg=self.color_button, activebackground=self.active_color, fg="white", command=lambda:self.check_button_ticket(self.btn_ticket_10))
		self.buttons_ticket = [self.btn_ticket_1, self.btn_ticket_2, self.btn_ticket_3, 
										self.btn_ticket_4, self.btn_ticket_5, self.btn_ticket_6,
										self.btn_ticket_7, self.btn_ticket_8, self.btn_ticket_9, self.btn_ticket_10]
		self.btn_print = Button(self.frm_child_1, text="печать", width=8, font="Broadway 10", relief=GROOVE, bg=self.color_button, activebackground=self.active_color, fg="white", command=self.print_on_paper)
	
		
	def on_closing(self):
		self.root.destroy()
		
		
	def print_on_paper(self):
		# func for print ticket 
		if self.question_text.get() and self.answer_text.get():
			print_file = "Вопрос номер " + self.question_text.get() + "\n" + self.answer_text.get()
			f = open("print_file.txt", "w")
			f.write(print_file)
			os.startfile("print_file.txt", "print")
			f.close()
			# print("Вопрос номер", self.question_text.get() + "\n" + self.answer_text.get())
			# print(print_file)
		else:
			# self.show_error("ОШИБКА !", "Печатать то нечего !!!" )
			self.show_message_info("ОШИБКА !", "Печатать то нечего !!!", 800, 450)

	
	def show_message_info(self, title_, text_, indentation_x, indentation_y):
		PlaySound("button.wav", SND_ASYNC) # play sound
		win = Toplevel()
		win.overrideredirect(False)		# delete button manager window 
		win.title(title_)  
		win.geometry("+{}+{}".format(indentation_x, indentation_y))
		win.resizable(False, False)
		win.grab_set()
		win.focus_set()
		
		Label(win, text=text_, font="Garamond 12 bold", fg="black", justify=CENTER, bd=2).pack(padx=10, pady=10)
		Button(win, text="OK", font="Garamond 17 bold", fg="black", width=5, activebackground="#393939", relief=GROOVE, command=lambda: win.destroy()).pack(pady=10)
		
		
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
	
	
	def reset_fields_and_buttons(self):
		# func for cleaning text fields and check button
	
		for i in self.buttons_ticket:
			i.configure(bg="#7d8481")
			i.configure(state=NORMAL)
		self.draw_buttons()
		self.draw_radiobuttons()	
		
		
	def draw_buttons(self):
		# func for draw buttons check tickets
		h = 220
		v = 16
		for i in self.buttons_ticket:
			i.place(x=h, y=v)
			h += 74
		self.btn_print.place(x=960, y=16)
		
	
	def check_button_ticket(self, btn):
		self.reset_fields_and_buttons()
		self.check_post = self.checked_post.get()
		self.ticket = btn.cget("text")
	
		for i in self.buttons_ticket:
			if i == btn:
				i.configure(bg="#494949")
				i.configure(state=DISABLED)
			else:
				i.configure(bg="#7d8481")
				i.configure(state=NORMAL)
				
	
	def draw_radiobuttons(self): 
		# func for draw radiobuttons check questions
		self.select_questions = IntVar()
		space_heigth =30
		# tickets = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		for i in self.radiobuttons_question:
			i.place(x=28, y=space_heigth)
			space_heigth += 54
		
		
		# for i in tickets:
			# space = "вопрос № {} ".format(i)
			# _Radiobutton = Radiobutton(self.frm_child_2
									# , text=space
									# , font="Verdana 9 bold"
									# , activebackground="#7d8481"
									# , fg="#f7f7f7"
									# , bg="#7d8481"
									# , activeforeground="#7d8481"
									# , selectcolor="#7d8481"
									# , variable=self.select_questions
									# , value=i
									# , command=self.check_radiobutton).place(x=28, y=space_heigth)
			# space_heigth += 54
	
		
	def deactivate_buttons(self):
		for i in self.buttons_ticket:
			i.configure(bg="#494949")
			i.configure(state=DISABLED)
		
		
	def check_radiobutton(self):
		# function output text answer and questions on display view
		self.number_question = self.select_questions.get()

		try:
			self.question_get, self.answer_get = self.read_database(self.ticket, self.number_question)
		except Exception:
			self.show_message_info("Внимание !", "     Выберите билет!     ", 800, 450)
			
		# view answer in scrolled text field 	
		self.scrolled_text = ScrolledText(self.root, width=105, height=25, font="Garamond 12 bold", fg="black", relief=GROOVE, wrap=WORD, padx=20, pady=20)
		self.scrolled_text.insert("1.0", self.answer_get)
		self.scrolled_text.place(x=194, y=180)
		self.scrolled_text.configure(state=DISABLED)
														
		self.text_question = Text(self.frm_child_3, width=102, height=3, bg="#f3f7fb", font="Garamond 12 bold",  fg="black", padx=10, pady=10, wrap=WORD, bd=0)
		self.text_question.insert("1.0", self.question_get)
		self.text_question.place(x=20, y=14)	
		self.text_question.configure(state=DISABLED)
			
	
	def open_ticket_editing(self):
		self.scrolled_text.configure(state=NORMAL)
		self.text_question.configure(state=NORMAL)
		self.scrolled_text.delete("1.0", "end")
		self.text_question.delete("1.0", END)
	
	def check_button_post(self):
		# func checks which position is selected by the user
		#global post_question, post_answer
		self.reset_fields_and_buttons()
		self.check_post = self.checked_post.get()
		
		print(self.check_post)
		if self.check_post == "машинист":
			self.lbl_child_1.config(text="Машинист")
			self.draw_buttons()
			self.post_answer = "answers_mash.txt"
			self.post_question = "questions_mash.txt"
			self.draw_radiobuttons()
		if self.check_post == "оператор":
			self.lbl_child_1.config(text="Оператор")
			self.draw_buttons()
			self.post_answer = "answers_oper.txt"
			self.post_question = "questions_oper.txt"
			self.draw_radiobuttons()
		if self.check_post == "слесарь":
			self.lbl_child_1.config(text="Слесарь")
			self.draw_buttons()
			self.post_answer = "answers_slesar.txt"
			self.post_question = "questions_slesar.txt"
			self.draw_radiobuttons()
		
		
	def read_database(self, ticket_choise, question): 
		# func for reading from database
		global ticket
		array_tickets = []
		num = 1
		for i in range(10):
			array_tickets += ["ticket_" + str(num)]
			num += 1
		
		database = sqlite3.connect("tickets.db")
		cursor = database.cursor()
		cursor.execute("SELECT {} FROM {} WHERE number = {}".format(array_tickets[int(ticket_choise)-1], question)) # выбор таблицы и строки по номеру 
		output = cursor.fetchone()
		database.close()
		return output[1], output[2]
	

		
	

