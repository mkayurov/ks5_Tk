from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
#from winsound import *
import os
import sqlite3
import time


class Child:
	def __init__(self, button, parent, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel(parent)
		self.btn = button
		self.parent_window = parent
		self.root["bg"] = "#e0e5e6"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
	
		self.root.grab_set()
		self.root.focus_set()
		self.widgets_child()
		self.menu_bar()
		self.pressed_button = None
		
	def menu_bar(self):
		""" func for draw menubar - Функция для отрисовки и функционала меню бара """
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
		self.fm.add_command(label="Выход", command=self.on_closing)
		
		self.hm = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Должность",menu=self.hm)
		self.hm.add_radiobutton(label="Машинист", state="normal", value="машинист", variable=self.checked_post, command=self.check_button_post)
		self.hm.add_radiobutton(label="Оператор", state="normal", value="оператор", variable=self.checked_post, command=self.check_button_post)
		self.hm.add_radiobutton(label="Слесарь", state="normal", value="слесарь", variable=self.checked_post, command=self.check_button_post)

		
	def widgets_child(self):
		""" func for castom widgets on window - Функция для отрисовки виджетов """
		self.select_questions = IntVar()
		self.color_button = "#7d8481"
		self.active_color = "#393939"
		# frames 
		self.frm_child_1 = Frame(self.root, width=1086, height=61, bg="#93a7a6", relief=GROOVE, bd=2)
		self.frm_child_2 = Frame(self.root, width=180, height=598, bg="#7d8481", relief=GROOVE, bd=2)
		self.frm_child_3 = Frame(self.root, width=900, height=100, bg="#f3f7fb", relief=GROOVE, bd=2)
		self.lbl_child_1 = Label(self.frm_child_1, font="Broadway 13", bg="#93a7a6", fg="#2f2f2f")
		# unpacking frames
		self.frm_child_1.place(x=8, y=8)
		self.frm_child_2.place(x=8, y=75)
		self.frm_child_3.place(x=194, y=75)
		self.lbl_child_1.place(x=36, y=14)
		
		# question radiobuttons
		self.rbt_question_1 = Radiobutton(self.frm_child_2, text="вопрос № 1 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=1, command=self.check_radiobutton)
		self.rbt_question_2 = Radiobutton(self.frm_child_2, text="вопрос № 2 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=2, command=self.check_radiobutton)
		self.rbt_question_3 = Radiobutton(self.frm_child_2, text="вопрос № 3 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=3, command=self.check_radiobutton)
		self.rbt_question_4 = Radiobutton(self.frm_child_2, text="вопрос № 4 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=4, command=self.check_radiobutton)
		self.rbt_question_5 = Radiobutton(self.frm_child_2, text="вопрос № 5 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=5, command=self.check_radiobutton)
		self.rbt_question_6 = Radiobutton(self.frm_child_2, text="вопрос № 6 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=6, command=self.check_radiobutton)
		self.rbt_question_7 = Radiobutton(self.frm_child_2, text="вопрос № 7 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=7, command=self.check_radiobutton)
		self.rbt_question_8 = Radiobutton(self.frm_child_2, text="вопрос № 8 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=8, command=self.check_radiobutton)
		self.rbt_question_9 = Radiobutton(self.frm_child_2, text="вопрос № 9 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
																		selectcolor="#7d8481", variable=self.select_questions, value=9, command=self.check_radiobutton)
		self.rbt_question_10 = Radiobutton(self.frm_child_2, text="вопрос № 10 ", font="Verdana 9 bold", fg="#f7f7f7", bg="#7d8481", activeforeground="#7d8481", 
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
												
		self.btn_print = Button(self.frm_child_1, text="редактировать", width=16, font="Verdana 9 bold", relief=GROOVE, bg=self.color_button, activebackground=self.active_color, fg="white", command=self.editing_tickets)
		# ScrolledText widget
		self.scrolled_text = ScrolledText(self.root, width=105, height=25, font="Garamond 12 bold", fg="black", relief=GROOVE, wrap=WORD, padx=20, pady=20)
		self.text_question = Text(self.frm_child_3, width=102, height=3, bg="#f3f7fb", font="Garamond 12 bold",  fg="black", padx=10, pady=10, wrap=WORD, bd=0)

		
	def on_closing(self):
		""" func for closed window - Функция для закрытия окна """	
		self.btn.configure(state=NORMAL) # вернет нормальное состояние кнопке btn_open_child в классе Main
		self.root.destroy()
		
		
	def print_on_paper(self): 
		""" func for print ticket - Функция для печати """
		try:
			qst, ans = self.read_database(self.ticket, self.number_question)
			print_file = "Вопрос номер " + qst + "\n" + ans
			os.startfile("print_file.txt", "print")
		except Exception:
			self.show_message_info("ОШИБКА !", "Печатать то нечего !!!", 800, 450)

	
	def show_message_info(self, sound, title_, text_, indentation_x, indentation_y):
		""" func for window messages - Функция для окна сообщений """
		#PlaySound(sound, SND_ASYNC) # play sound
		win = Toplevel()
		win.overrideredirect(False) # delete button manager window 
		win.title(title_)  
		win.geometry("+{}+{}".format(indentation_x, indentation_y))
		win.resizable(False, False)
		win.grab_set()
		win.focus_set()
		
		Label(win, text=text_, font="Garamond 12 bold", fg="black", justify=CENTER, bd=2).pack(padx=10, pady=10)
		Button(win, text="OK", font="Garamond 17 bold", fg="black", width=5, relief=GROOVE, command=lambda:win.destroy()).pack(pady=10)	
		
		
	def show_error(self, title_, info_): 
		""" func for window messages to errors - Функция для окна сообщений об ошибках """
		messagebox.showinfo(title_, info_)
	
		
	def draw_buttons(self): 
		""" func for draw buttons check tickets - Функция для отрисовки кнопок выбора билетов """
		h = 184
		v = 16
		for i in self.buttons_ticket:
			i.place(x=h, y=v)
			h += 74
		self.btn_print.place(x=924, y=16)
		self.btn_print.configure(state=DISABLED)
	
	
	def draw_radiobuttons(self): 
		""" func for draw radiobuttons check questions - Функция для отрисовки кнопок выбора вопросов """
		space_heigth =30
		for i in self.radiobuttons_question:
			i.place(x=28, y=space_heigth)
			space_heigth += 54
	

	def check_button_ticket(self, btn):  
			""" func for choise ticket and geting his number - Функция для выбора билета и получении его номера """
			self.pressed_button = btn
			self.reset_fields_and_buttons()
			self.ticket = btn.cget("text")
			
			for i in self.buttons_ticket:
				if i == btn:
					i.configure(bg="#494949")
					i.configure(state=DISABLED)
				else:
					i.configure(bg="#7d8481")
					i.configure(state=NORMAL)
		
		
	def check_radiobutton(self): 
		""" function output text answer and questions on display view - Функция для вывода текста ответа и вопроса в соответствующие поля """
		self.number_question = self.select_questions.get()
		try:
			self.table, self.question_get, self.answer_get = self.read_database(self.ticket, self.number_question)
			self.btn_print.configure(state=NORMAL)
		except Exception:
			self.show_message_info("ding.wav", "Внимание !", "     Выберите билет!     ", 800, 450)
			self.number_question = self.select_questions.set(0)

		# view answer in scrolled text field 	
		self.scrolled_text.configure(state=NORMAL)
		self.scrolled_text.delete("1.0", "end")
		self.scrolled_text.insert("1.0", self.answer_get)
		self.scrolled_text.place(x=194, y=180)
		self.scrolled_text.configure(state=DISABLED)
		# view question in text field 												
		self.text_question.configure(state=NORMAL)
		self.text_question.delete("1.0", "end")
		self.text_question.insert("1.0", self.question_get)
		self.text_question.place(x=20, y=14)	
		self.text_question.configure(state=DISABLED)
			
			
	def reset_fields_and_buttons(self): 
		""" func for clean text fields and reset pressed buttons - Функция для очистки текстовых полей и сброс нажатых кнопок """
		self.number_question = self.select_questions.set(0)
		self.scrolled_text.configure(state=NORMAL)
		self.text_question.configure(state=NORMAL)
		self.scrolled_text.delete("1.0", "end")
		self.text_question.delete("1.0", "end")
		self.scrolled_text.configure(state=DISABLED)
		self.text_question.configure(state=DISABLED)
		self.question_get = ""
		self.answer_get = ""
		self.ticket = None

		for i in self.buttons_ticket:
			i.configure(bg="#7d8481")
			i.configure(state=NORMAL)
			
		self.draw_buttons()
	
	
	def check_button_post(self): 
		""" func checks which position is selected by the user - Функция для выбора должности и соответствующих ей билетов """
		self.reset_fields_and_buttons()
		self.draw_buttons()
		self.check_post = self.checked_post.get()
		self.draw_radiobuttons()
		self.post_data = ""
		
		if self.check_post == "машинист":
			self.lbl_child_1.config(text="Машинист")
			self.post_data = "mash.db"
		if self.check_post == "оператор":
			self.lbl_child_1.config(text="Оператор")
			self.post_data = "oper.db"
		if self.check_post == "слесарь":
			self.lbl_child_1.config(text="Слесарь")
			self.post_data = "slesar.db"


	def deactivate_buttons(self):
		""" func for deactivate buttons and radiobuttons at editing - функция для деактивации кнопок и радиокнопок при редактировании """
		for i in self.buttons_ticket:
			if i == self.pressed_button:
				i.configure(bg="#494949")
				i.configure(state=DISABLED)
			else:
				i.configure(bg="#7d8481")
				i.configure(state=DISABLED)
				
		for i in self.radiobuttons_question:
			if i == self.number_question:
				i.configure(bg="red")
				# i.configure(state=DISABLED)
			else:
				i.configure(bg="#7d8481")
				i.configure(state=DISABLED)
				
		self.frm_child_3.configure(bg="#d6f4c6")
		self.text_question.configure(bg="#d6f4c6")
		self.scrolled_text.configure(bg="#d6f4c6")
	
	
	def activate_buttons(self):
		""" func for activate buttons and radiobuttons after editing - функция для активации кнопок и радиокнопок после редактирования """
		for i in self.buttons_ticket:
			if i == self.pressed_button:
				i.configure(bg="#494949")
				i.configure(state=DISABLED)
			else:
				i.configure(bg="#7d8481")
				i.configure(state=NORMAL)	
					
		for i in self.radiobuttons_question:
			if i == self.number_question:
				print(i)
			else:
				i.configure(state=NORMAL)
		self.frm_child_3.configure(bg="#f3f7fb")
		self.text_question.configure(bg="#f3f7fb")
		self.scrolled_text.configure(bg="white")
		
		
	def read_database(self, ticket_choise, question): 
		""" func for reading questions and answers in database - Функция для чтения вопросов и ответов из базы данных и вывод текста в соответствующие поля """
		array_tickets = []
		num = 1
		for i in range(10):
			array_tickets += ["ticket_" + str(num)]
			num += 1
		
		database = sqlite3.connect(self.post_data)
		cursor = database.cursor()
		cursor.execute("SELECT * FROM {} WHERE number = {}".format(array_tickets[int(ticket_choise)-1], question)) # выбор таблицы и строки по номеру 
		output = cursor.fetchone()
		cursor.close()
		database.close()
		return array_tickets[int(ticket_choise)-1], output[1], output[2]		


	def editing_tickets(self):
		""" func for editing text questions and answers and save changes in database - Функция для редактирования текста вопросов и ответов и сохранения изменений в базе данных """
		edit_question = self.text_question.get("1.0", "end")
		edit_answer = self.scrolled_text.get("1.0", "end")
		self.scrolled_text.configure(state=NORMAL)
		self.text_question.configure(state=NORMAL)
		self.deactivate_buttons()
		
		if self.btn_print["text"] == "редактировать":
			self.btn_print.configure(text = "сохранить")
		else:
			self.btn_print.configure(text = "редактировать")
			self.update_database(self.table, edit_question, edit_answer, self.number_question)
			self.scrolled_text.configure(state=DISABLED)
			self.text_question.configure(state=DISABLED)
			PlaySound("ding.wav", SND_ASYNC)
			# self.show_message_info("ding.wav","Сохранение", "изменения успешно внесены ", 800, 450)
			self.activate_buttons()
			
		
	def update_database(self, tic, qst, ans, num): 
		""" func for update data after enter changes in tickets - функция для обновления базы данных после внесения изменений в билеты 
			передать в эту функцию возвращенные параметры из read_database 
		"""
		try:
			database = sqlite3.connect(self.post_data)
			cursor = database.cursor()
			print("Соединение с базой данных SQLite успешно установлено !")
			cursor.execute("""UPDATE  '{}' SET question='{}', answer='{}' WHERE number ='{}' """.format(tic, qst, ans, num)) # апостроф !
			database.commit()
			print("Запись успешно обновлена !")
			cursor.close()
		except sqlite3.Error as error:
			print("Ошибка при работе с базой данных SQLite", error)
		finally:
			if database:
				database.close()
				print("Соединение с базой данных SQLite закрыто !")

		

