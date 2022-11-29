from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import os
from child_window import Child 
from documents import Graphics, Journal, Templates, Registration, Equipping, MetanolCalculate, Editing
import sqlite3


class Main:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Tk()
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		
		self.wigets_main()
		self.menu_bar()
		
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
		
	def on_closing(self):
		self.root.destroy()
		
		
	def menu_bar(self):
		self.m = Menu(self.root)         						 			   							
		self.root.config(menu=self.m)                               										
		self.fm = Menu(self.m, tearoff=0)                                          											
		self.m.add_cascade(label="Файл",menu=self.fm, state="normal")  
		self.fm.add_command(label="Новый")
		# self.fm.add_separator()		
		self.fm.add_command(label="Открыть...")    							
		self.fm.add_command(label="Сохранить...")
		self.fm.add_command(label="Выход", command=self.root.quit)
		
		self.infom = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Информация",menu=self.infom)
		self.infom.add_command(label="Архив", state="disabled")
		self.infom.add_command(label="Работникам", command=self.read_database, state="disabled")
		self.infom.add_command(label="Помощь")
		self.infom.add_command(label="О программе...", command=self.about_us)
		
		self.hm = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Настройки",menu=self.hm)
		
		
	def about_us(self):
		about_us_window = Toplevel(self.root)
		about_us_window.title("О программе")
		about_us_window.geometry("220x180+700+400")
		about_us_window.resizable(False, False)
		about_us_window.iconbitmap("img/Admin.ico")
		about_us_window.grab_set()
		about_us_window.focus_set()
		label_about_us = Label(about_us_window, text = "Copyright © 2021\n\n"
																			"Author: Mikhail Kayurov\n\n"
																			"GNU(General Public License)\n\n"
																			"Операционная система: Windows XP\n\n"
																			"Версия программы 1.3.3\n").pack(pady=10)
		
													
	# func to draw widgets in view main window
	def wigets_main(self):
		self.frm_main_1 = LabelFrame(self.root, width=600, height=50, bg="#7d8481", bd=2)
		self.frm_main_2 = Frame(self.root, width=600, height=450, bg="#93a7a6", relief=GROOVE, bd=2)
		self.frm_main_3 = LabelFrame(self.frm_main_2, width=200, height=250, text=" Общие документы ", font="Elephant 8",bg="#93a7a6", fg="black")
		self.frm_main_4 = LabelFrame(self.frm_main_2, width=521, height=94, font="Elephant 8",bg="#93a7a6", fg="black")
		self.frm_main_5 = LabelFrame(self.frm_main_2, width=300, height=250, text=" Работникам ", font="Elephant 8",bg="#93a7a6", fg="black")
		
		self.frm_main_1.pack()
		self.frm_main_2.pack()
		self.frm_main_3.place(x=10, y=6)
		self.frm_main_4.place(x=10, y=266)
		self.frm_main_5.place(x=230, y=6)
		
		# Labels
		self.label_1 = Label(self.frm_main_1, text="KC - 5", font="Elephant 17",bg="#7d8481", fg="white")
		self.label_1.place(x=230, y=6)
		# Buttons
		self.btn_open_child = Button(self.frm_main_2, width=25, fg="white", font="Elephant 10 bold", text="Билеты для проверки знаний", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.open_child_window)
		btn_registration = Button(self.frm_main_2, width=25, fg="white", font="Elephant 10 bold", text="Добавить в БД", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.registration)
		btn_entry = Button(self.frm_main_2, width=25, fg="white", font="Elephant 10 bold", text="Вход", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.entrys)
		btn_graphics = Button(self.frm_main_3, width=15, text="Графики", fg="white", font="Elephant 10 bold", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.open_graphics_window)
		btn_journal = Button(self.frm_main_3, width=15, text="Журналы", fg="white", font="Elephant 10 bold", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.open_journal_window)
		btn_templates = Button(self.frm_main_3, width=15, text="Шаблоны", fg="white", font="Elephant 10 bold", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.open_templates_window)
		btn_equipping = Button(self.frm_main_3, width=15, text="Оборудование", fg="white", font="Elephant 10 bold", activeforeground="white", bg="#7d8481", relief=GROOVE, command=self.open_equipping_window)
		btn_metanol_vol = Button(self.frm_main_4, width=22, text="Объём метанола", fg="white", activebackground="#7d8481", bg="#7d8481", relief=GROOVE, command=self.open_metanol_window)
		btn_metanol_journal = Button(self.frm_main_4, width=22, text="Журнал метанола.", fg="white", activebackground="#7d8481", bg="#7d8481", relief=GROOVE, command=self.open_journal_metanol)
		
		self.btn_open_child.place(x=250, y=42)
		btn_registration.place(x=250, y=95)
		btn_registration.configure(state=DISABLED)
		btn_entry.place(x=250, y=147)
		btn_graphics.place(x=18, y=20)
		btn_journal.place(x=18, y=73)
		btn_templates.place(x=18, y=126)
		btn_equipping.place(x=18, y=177)
		btn_metanol_vol.place(x=18, y=10)
		btn_metanol_journal.place(x=18, y=50)
		btn_metanol_journal.configure(state=NORMAL)
		
		
	
	
	def entrys(self): pass
	
	
	def adding_to_database(self):
		pass
		# self.database = sqlite3.connect("employees.db")
		# self.cursor = self.database.cursor()
		# self.cursor.execute("ALTER TABLE users ADD COLUMN 'post' 'TEXT' ")
		# self.database.commit()
		# self.database.close()
	
	# Function for delete user from database
	def delete_user(self):
		self.database = sqlite3.connect("employees.db")
		self.cursor = self.database.cursor()
		ask = input("Какой акаунт удалить? ")
		for i in self.cursor.execute("SELECT family FROM users"):
			if i[0] == ask:
				self.cursor.execute("DELETE FROM users WHERE family = '{}'".format(ask))
				self.database.commit()
				print("акаунт" + i[0] + " удален")
				
			print(i[0])
			self.database.close()
			return
			
	# function for reading list database
	def read_database(self):
		global employees
		employees = []
		self.database = sqlite3.connect("employees.db")
		self.cursor = self.database.cursor()
		for i in self.cursor.execute("SELECT * FROM users"):
			# employees.append("{} {} {}".format(i[0], i[1], i[2]))
			print(i[0], i[1], i[2], i[3])
		self.database.close()
		
	# func for open child window
	def open_child_window(self):
		Child(self.btn_open_child, self.root, 1100, 684, 300, 100, "Child window")
		self.btn_open_child.configure(state=DISABLED)

		
	def open_graphics_window(self):
		year_now = datetime.datetime.now()
		Graphics(300, 240, 640, 240, "Графики на {} год".format(year_now.year))
	
	
	def open_journal_window(self):
		try:
			os.startfile("C:\Documents and Settings\MashinistKU\Рабочий стол\журналы кс 5")
		except Exception:
			self.show_error("Ошибка !", "Файл отсутствует или поврежден")
		# Journal(300, 240, 640, 220, "Справки и акты")
	
	
	def open_templates_window(self):
		try:
			os.startfile("F:\машинистКС5\Каюров\python\ks_5\Templ")
		except Exception:
			self.show_error("Ошибка !", "Файл отсутствует или поврежден")
	
	
	def open_equipping_window(self):
		Equipping(400, 120, 680, 290, "Оборудование")
		# os.startfile("F:\python\Templ")
		
		
	def registration(self):
		Registration(300, 240, 700, 250, "Регистрация")
	
	
	def open_metanol_window(self):
		MetanolCalculate(300, 170, 680, 290, "Расчет остатка метанола")
		
		
	def open_journal_metanol(self): pass

		
	def open_ticket_editing(self): 
		Editing(600, 400, 600, 200, "Редактировать билеты")

	
	
		
	def run(self):
		self.root.mainloop()
		
		
if __name__ == "__main__":
	window = Main(545, 425, 400, 200, "Main window")
	window.run()
		