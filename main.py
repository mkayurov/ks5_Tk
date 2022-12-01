from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import datetime
import sqlite3
import os
from tickets import Tickets
from methanol import MetanolCalculate
from notes import Notes
from calc import Calculator

class Main:
	def __init__(self, width, height, name_title):
		self.root = Tk()
		self.root.title(name_title)
		self.root['bg']="#a1a1a1"
		self.root.resizable(False, False)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		# центровка  окна
		# self.root.eval('tk::PlaceWindow . center')
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		indentation_x = int((screen_width/2) - (width/2))
		indentation_y = int((screen_height/2) - (height/2))
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		# starting methods class
		self.menu_bar()
		self.draw_widgets()
		
		
		
	def photoredactor_window(self):
		try:
			os.startfile("C:/Program Files/PhotoshopPortable/PhotoshopCS6Portable.exe")
		except Exception:
			self.show_error("Ошибка", "Программа не найдена!")
		
	
	def calc_window(self): 
		Calculator(self.btn_calc, self.root, 300, 476, 680, 290, "Калькулятор")
		# self.btn_calc.configure(state=DISABLED)
		
	
	def equipping_window(self):
		os.startfile("equipping")
	
	
	def notes_window(self): 
		Notes(self.btn_notes, self.root, 400, 600, 680, 290, "Заметки")
		self.btn_notes.configure(state=DISABLED)
	
	def methanol_window(self): 
		MetanolCalculate(self.btn_methanol, self.root, 300, 170, 680, 290, "Расчет остатка метанола")
		self.btn_methanol.configure(state=DISABLED)
		
	
	def ticket_window(self):
		Tickets(self.btn_tickets, self.root, 1100, 684, 300, 100, "Билеты для проверки знаний")
		self.btn_tickets.configure(state=DISABLED)
	
	
	def about_us(self):
		self.about_us_window = Toplevel(self.root)
		self.about_us_window.title("О программе")
		self.about_us_window.geometry("220x180+700+400")
		self.about_us_window.resizable(False, False)
		# about_us_window.iconbitmap("img/Admin.ico")
		self.about_us_window.tk.eval('tk::PlaceWindow {0} widget {0}'.format(self.about_us_window, self.root))
		self.about_us_window.grab_set()
		self.about_us_window.focus_set()
		label_about_us = Label(self.about_us_window, text = "Copyright © 2022\n\n"
																			"Author: Mikhail Kayurov\n\n"
																			"GNU(General Public License)\n\n"
																			"Операционная система: Windows XP\n\n"
																			"Версия программы 2.0\n").pack(pady=10)
		
	
	def menu_bar(self):
		self.m = Menu(self.root)         						 			   							
		self.root.config(menu=self.m)                               										
		self.fm = Menu(self.m, tearoff=0)                                          											
		self.m.add_cascade(label="Файл",menu=self.fm, state="normal")  
		self.fm.add_command(label="Новый")	
		self.fm.add_command(label="Открыть...")    							
		self.fm.add_command(label="Сохранить...")
		self.fm.add_command(label="Выход", command=self.root.quit)
	
		self.settings = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="Настройки",menu=self.settings)	
		
		self.infom = Menu(self.m, tearoff=0) 																		
		self.m.add_cascade(label="инфо",menu=self.infom)
		self.infom.add_command(label="Архив", state="disabled")
		self.infom.add_command(label="Помощь")
		self.infom.add_command(label="О программе...", command=self.about_us)
		
		
	def draw_widgets(self):
		self.frm_1 = Frame(self.root, bg="#515151", width=300, height=50)
		self.frm_2 = Frame(self.root, bg="#979797")
		self.frm_1.pack(fill='both')
		self.frm_2.pack(fill='both')	
		
		self.lbl = Label(self.frm_1, text="KC - 5", font="Elephant 17",bg="#515151", fg="white")
		self.lbl.pack(fill='both', pady=20)
		
		self.btn_tickets = Button(self.frm_2, width=40, text="Б И Л Е Т Ы", font="Impact 17", fg="#52af8b", bg="#515151", activebackground="#515151", activeforeground="#52af8b", relief=GROOVE, bd=0, command=self.ticket_window)
		self.btn_methanol = Button(self.frm_2, width=40,  text="М Е Т А Н О Л", font="Impact 17", fg="#6ac2a0", bg="#515151", activebackground="#515151", activeforeground="#6ac2a0", relief=GROOVE, bd=0, command=self.methanol_window)
		self.btn_notes = Button(self.frm_2, width=40,  text="З А М Е Т К И", font="Impact 17", fg="#7fccae", bg="#515151", activebackground="#515151", activeforeground="#7fccae", relief=GROOVE, bd=0, command=self.notes_window)
		self.btn_equipping = Button(self.frm_2, width=40,  text="О Б О Р У Д О В А Н И Е", font="Impact 17", fg="#9eddc5", bg="#515151", activebackground="#515151", activeforeground="#9eddc5",  relief=GROOVE, bd=0, command=self.equipping_window)
		self.btn_calc = Button(self.frm_2, width=40,  text="К А Л Ь К У Л Я Т О Р", font="Impact 17", fg="#bdeedb", bg="#515151", activebackground="#515151", activeforeground="#bdeedb",  relief=GROOVE, bd=0, command=self.calc_window)
		self.btn_photoshop = Button(self.frm_2, width=40,  text="Ф О Т О Р Е Д А К Т О Р", font="Impact 17", fg="#e6fef5", bg="#515151", activebackground="#515151", activeforeground="#d4fded",  relief=GROOVE, bd=0, command=self.photoredactor_window)
		
		self.btn_tickets.pack(side="top", ipady=6, fill='both', expand=True)
		self.btn_methanol.pack(side="top", ipady=6 , fill='both', expand=True) 
		self.btn_notes.pack(side="top", ipady=6 , fill='both', expand=True)
		self.btn_equipping.pack(side="top", ipady=6 , fill='both', expand=True)
		self.btn_calc.pack(side="top", ipady=6 , fill='both', expand=True)
		self.btn_photoshop.pack(side="top", ipady=6, fill='both', expand=True)
	

	def show_error(self, title_, info_):
			messagebox.showinfo(title_, info_)
			
		
	def on_closing(self):
			self.root.destroy()
		
		
		
	def run(self):
		self.root.mainloop()
		
		
if __name__ == "__main__":
	window = Main(260, 420, "Главное меню")
	window.run()
		