from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
#from winsound import *
import os
import sqlite3



class Registration:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		# self.root["bg"] = "#7d8481"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.resizable(False, False)

		self.root.grab_set()
		self.root.focus_set()
		self.wiget_for_registration()
	
	
	def on_closing(self):
		self.text_field_family.delete(0, END)
		self.text_field_name.delete(0, END)
		self.text_field_surname.delete(0, END)
		self.text_field_post.delete(0, END)
		self.root.destroy()
	
	
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
	
	
	def show_info(self, title_, info_):
		messagebox.showinfo(title_, info_)
	
	
	def wiget_for_registration(self):
		self.chek_value = BooleanVar()
		self.get_promting = BooleanVar()
		
		label_family = Label(self.root, text="фамилия", font="Ariel 9 bold")
		label_name = Label(self.root, text="имя", font="Ariel 9 bold")
		label_surname = Label(self.root, text="отчество", font="Ariel 9 bold")
		label_password = Label(self.root, text="должность", font="Ariel 9 bold")
		
		self.text_field_name = Entry(self.root, text="name", font="Garamond 12 bold", justify=CENTER, width=20, bd=2, relief=RIDGE)
		self.text_field_surname = Entry(self.root, text="surname", font="Garamond 12 bold", justify=CENTER, width=20, bd=2, relief=RIDGE)
		self.text_field_family = Entry(self.root, text="family", font="Garamond 12 bold", justify=CENTER, width=20, bd=2, relief=RIDGE)
		self.text_field_post = Entry(self.root, text="post", font="Garamond 12 bold", justify=CENTER, width=20, bd=2, relief=RIDGE)
		
		check_btn = Checkbutton(self.root, text="добавить личную папку на главное окно", variable=self.chek_value, command=self.check_append_folder)
		# check_btn_password = Checkbutton(self.root, text="установить\n пароль", variable=self.get_promting, command=self.if_check_add_password)
		
		self.registr_button = Button(self.root, text="Подтвердить", width=20, font="Ariel 10 bold", bd=2, relief=GROOVE, command=self.get_data_registration)
		
		label_family.place(x=10, y=18)
		label_name.place(x=10, y=52)
		label_surname.place(x=10, y=84)
		label_password.place(x=10, y=120)
		
		self.text_field_family.place(x=100, y=14)
		self.text_field_name.place(x=100, y=48)
		self.text_field_surname.place(x=100, y=82)
		# check_btn_password.place(x=10, y=130)
		self.text_field_post.place(x=100, y=118)
		self.registr_button.place(x=66, y=182)
		
		
	# def if_check_add_password(self):
		# if self.get_promting.get() == True:
			# self.text_field_post.place(x=100, y=134)
			# self.registr_button.place(x=66, y=182)
			# print("True")
		# else:
			# self.text_field_post.place_forget()
			# self.registr_button.place(x=66, y=176)
			# self.text_field_post.delete(0, END)
			# print("False")
		
		
	def get_data_registration(self):
		global database
		global cursor
		self.database = sqlite3.connect("employees.db")
		self.cursor = self.database.cursor()
		self.cursor.execute(""" CREATE TABLE IF NOT EXISTS users (
								family TEXT,
								name TEXT,
								surname TEXT,
								post TEXT
								) """)
								
		self.cursor.execute("SELECT family FROM users WHERE family = '{}'".format(self.text_field_family.get()))
		
		if self.cursor.fetchone() is None:
			if self.text_field_family.get():
				if self.text_field_name.get():
					if self.text_field_surname.get():
						if self.text_field_post.get():
							self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.text_field_family.get(), self.text_field_name.get(), self.text_field_surname.get(), self.text_field_post.get()))
							self.on_closing()
							self.show_info(" ", "Регистрация завершена!  ")
							self.database.commit()
							self.database.close()
							return
						else:
							self.show_info(" ", "укажите должность")
					else:
						self.show_info(" ", "введите отчество")
				else:
					self.show_info(" ", "введите имя")
			else:
				self.show_info(" ", "введите фамилию")
		else:
			print("Запись уже существует")
			self.show_info("Ошибка  регистрации!", "Пользователь с таким логином  \n        уже существует")
			self.on_closing()
		self.database.close()
		return
			
		
	def check_append_folder(self):
		global to_pass
		if self.chek_value.get() == True: 
			self.to_pass = 1
			print("True")
			return self.to_pass
		else:
			self.to_pass = 0
			print("False")
			return self.to_pass
		

		
class Equipping:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		self.root["bg"] = "#b8c4bf"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)

		self.root.grab_set()
		self.root.focus_set()
		self.draw_widgets_equipping()
		# os.startfile("F:/машинистКС5/Машинисты КС-5/Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
	def draw_widgets_equipping(self):
		self.frame = LabelFrame(self.root, text=" Компрессоры ", width=386, height=100, bg="#b8c4bf")
		self.frame.pack(pady=5)
		
		btn_bks_8 = Button(self.frame, text="БКС-8", width=20, fg="white", font="Ariel 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda:self.open_compressor(btn_bks_8))
		btn_bks_8.place(x=12, y=10)
		btn_bks_35 = Button(self.frame, text="БКС-35", width=20, fg="white", font="Ariel 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda:self.open_compressor(btn_bks_35))
		btn_bks_35.place(x=12, y=44)
		btn_mku_1000 = Button(self.frame, text="МКУ-1000", width=20, fg="white", font="Ariel 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE,  command=lambda:self.open_compressor(btn_mku_1000))
		btn_mku_1000.place(x=200, y=10)
		btn_mku_3000 = Button(self.frame, text="МКУ-3000", width=20, fg="white", font="Ariel 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE,  command=lambda:self.open_compressor(btn_mku_3000))
		btn_mku_3000.place(x=200, y=44)
		
		
	def open_compressor(self, btn):
		try:
			if btn.cget("text") == "БКС-8":
				os.startfile("F:/машинистКС5/Машинисты КС-5/Каюров/python/ks_5/Equipping/БКС8 РЭ.pdf")
			elif btn.cget("text") == "БКС-35":
				os.startfile("F:/машинистКС5/Машинисты КС-5/Каюров/python/ks_5/Equipping/Паспорт на компрессор кожва СНС92.doc")
			elif btn.cget("text") == "МКУ-1000":
				os.startfile("F:/машинистКС5/fdf")
			else:
				os.startfile("F:/машинистКС5/fdfd")
		except Exception:
			self.show_error("Ошибка !", "Файл отсутствует или поврежден")
			return
	
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
	
	
# _________________________class for reflection graphic ___________________________________
class Graphics:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		# self.root["bg"] = "#a0a0a4"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)

		self.root.grab_set()
		self.root.focus_set()
		self.wiget_for_graphics()
		# os.startfile("F:/машинистКС5/Машинисты КС-5/Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
		
		
	def wiget_for_graphics(self):
		self.frame_1 = Frame(self.root, width=300, height=250, bg="#b8c4bf")
		self.frame_1.pack()
		
		btn_mash= Button(self.frame_1, width=30, text="Машинисты", fg="white", font="Elephant 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda: self.open_mash_graphic(btn_mash))
		btn_mash.pack(padx=10, pady=15)
		btn_oper = Button(self.frame_1, width=30, text="Операторы", fg="white", font="Elephant 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda: self.open_mash_graphic(btn_oper))
		btn_oper.pack(padx=10, pady=15)
		btn_slesar = Button(self.frame_1, width=30, text="Слесаря", fg="white", font="Elephant 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda: self.open_mash_graphic(btn_slesar))
		btn_slesar.pack(padx=10, pady=15)
		btn_master = Button(self.frame_1, width=30, text="Мастера", fg="white", font="Elephant 10 bold", activebackground="#7d8481", activeforeground="white", bg="#7d8481", relief=GROOVE, command=lambda: self.open_mash_graphic(btn_master))
		btn_master.pack(padx=10, pady=15)
	
	
	def open_mash_graphic(self, btn):
		btn_name = btn.cget("text")
		if btn_name == "Машинисты":
			try:
				os.startfile("F:/машинистКС5/Машинисты КС-5/Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
			except Exception:
				self.show_error("Ошибка !", "Файл отсутствует или поврежден")
		elif btn_name == "Операторы":
			try:
				os.startfile("F:/машинистКС5/Машинисты КС- /Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
			except Exception:
				self.show_error("Ошибка !", "Файл отсутствует или поврежден")
		elif btn_name == "Слесаря":
			try:
				os.startfile("F:/машинистКС5/Машинисты КС- /Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
			except Exception:
				self.show_error("Ошибка !", "Файл отсутствует или поврежден")
		elif btn_name == "Мастера":
			try:
				os.startfile("F:/машинистКС5/Машинисты КС /Каюров/график_сменности_машинисты_КС5_2022 (2).xlsx")
			except Exception:
				self.show_error("Ошибка !", "Файл отсутствует или поврежден")
				
	
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)

	
class Journal:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		# self.root["bg"] = "#a0a0a4"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)

		self.root.grab_set()
		self.root.focus_set()
		self.widget_for_certificates()
		
	
	def widget_for_journal(self):
		self.frame_1 = Frame(self.root, width=300, height=250, bg="#b8c4bf")
		self.frame_1.pack()
		
		btn_act = Button(self.frame_1, width=30, text="Акты", bg="#7d8481").pack(padx=0, pady=0)

		
class Templates:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		# self.root["bg"] = "#a0a0a4"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.resizable(False, False)

		self.root.grab_set()
		self.root.focus_set()
		self.widget_for_templates()
	
	
	def widget_for_templates(self):
		self.frame_1 = Frame(self.root, width=400, height=300, bg="#b8c4bf", relief=GROOVE)
		self.frame_1.pack()
		
		
class MetanolCalculate:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		self.root["bg"] = "#b8c4bf"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.resizable(False, False)
		
		self.num_char1 = StringVar()
		self.num_char2 = StringVar()
		self.num_char1.trace("w", self.check_field1)
		self.num_char2.trace("w", self.check_field2)
		
		self.root.grab_set()
		self.root.focus_set()
		self.draw_widgets_metanol()
		
		
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
		
		
		
	def show_info(self, title_, info_):
		messagebox.showinfo(title_, info_)
		
		
	def on_closing(self):
		self.root.destroy()
  
		
	def read_data(self, lev1, lev2):
		self.db = sqlite3.connect("methanol.db")
		self.cursor = self.db.cursor()
		for i in self.cursor.execute(''' SELECT * FROM capacity '''):
			if int(lev1) == i[0]:
				vol1 = i[1]
				per1 = i[2]
				vol1 = vol1.replace(",", ".")
				per1 = per1.replace(",", ".")
				print(type(vol1), type(per1))
				print("остаток равен " + vol1 + "\n емкость заполнен на " + per1 + "%")
				print("Данные успешно считаны!")
				break
			else:
				continue
		for i in self.cursor.execute(''' SELECT * FROM capacity '''):
			if int(lev2) == i[0]:
				vol2 = i[1]
				per2 = i[2]
				vol2 = vol2.replace(",", ".")
				per2 = per2.replace(",", ".")
				print("остаток равен " + vol2 + "\n емкость заполнен на " + per2 + "%")
				print("Данные успешно считаны!")
				break
			else:
				continue
		self.db.close()
		sum = float(vol1) + float(vol2)
		return round(float(vol1), 1), per1, round(float(vol2), 1), per2, round(sum, 1)

		
	def draw_widgets_metanol(self):
		self.lbl_1 = Label(self.root, text="E-1", font="Ariel 10", bg="#b8c4bf")
		self.lbl_1.place(x=75, y=20)
		self.lbl_2 = Label(self.root, text="E-2", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_2.place(x=75, y=60)
		self.lbl_3 = Label(self.root, text="мм", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_3.place(x=195, y=20)
		self.lbl_4 = Label(self.root, text="мм", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_4.place(x=195, y=60)
		self.text_field_volume1 = Entry(self.root, textvariable=self.num_char1, font="Garamond 12 bold", justify=CENTER, width=10, bd=2, relief=RIDGE)
		self.text_field_volume1.place(x=105, y=20)
		self.text_field_volume2 = Entry(self.root, textvariable=self.num_char2, font="Garamond 12 bold", justify=CENTER, width=10, bd=2, relief=RIDGE)
		self.text_field_volume2.place(x=105, y=60)
		self.btn_met_calculate = Button(self.root, text="Расчитать", width=20, 
													fg="white", font="Ariel 10 bold", activebackground="#7d8481", 
													activeforeground="white", bg="#7d8481", relief=GROOVE,  
													command=lambda:self.get_volume(self.btn_met_calculate))
		self.btn_met_calculate.place(x=70, y=110)
		
	
	
	def check_field1(self, *args):
		"""проверка в реальном времени 
			символы вводимые пользователем
		"""
		char = self.num_char1.get()
		if char.isdigit():
			if len(char) == 4:
				if int(char) <= 2400:
					print("Заебись!")
					return 
					# self.text_field_volume1.config(state="readonly")
				else:
					self.show_info("Ошибка!", "максимальный уровень емкости 2400 мм.")
					return
			else:
				self.text_field_volume1.delete("4", "end")	
		else:
			self.text_field_volume1.delete("0", "end")
			# self.show_error("Ошибка!", "недопустимый символ")
			return
	
	
	def check_field2(self, *args):
		"""проверка в реальном времени 
			символы вводимые пользователем
		"""
		char = self.num_char2.get()
		if char.isdigit():
			if len(char) == 4:
				if int(char) <= 2400:
					print("Заебись!")
					# self.text_field_volume2.config(state="readonly")
					return
				else:
					self.show_info("Ошибка!", "максимальный уровень емкости 2400 мм.")
					return
			else:
				self.text_field_volume2.delete("4", "end")	
		else:
			self.text_field_volume2.delete("0", "end")
			# self.show_error("Ошибка!", "недопустимый символ")
			return 
		
		
	def to_make_round(self, number):
		if int(number[-1]) >= 5:
			number = number[:-1]
			number = int(number)
			number += 1
			number = str(number)
			number += "0"
			
			print("bing")
		else:
			number = number[:-1]
			number += "0"
			# print(number)
			print("Not")
		return number
			
			
	def get_volume(self, btn):
		print(self.num_char1.get())
		btn_title = btn.cget("text")
		text_vol1 = self.text_field_volume1.get()
		text_vol2 = self.text_field_volume2.get()
	
		if text_vol1 != "" and text_vol2 != "":
			text_vol1 = self.to_make_round(text_vol1)
			text_vol2 = self.to_make_round(text_vol2)
			volume1, persance1, volume2, persance2, sum_pers = self.read_data(text_vol1, text_vol2)
			self.show_info("Расчет выполнен", "Е-1:\t{} м3\n\t{} %\n\nЕ-2:\t{} м3\n\t{} %\n\nобщий объём:  {} м3          \n".format(volume1, 
																														persance1,
																														volume2, 
																														persance2, 
																														round(sum_pers, 1)))
			self.root.destroy()
		else:
			self.show_info("Ошибка!", "заполни оба поля")
			return


class Editing:
	def __init__(self, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel()
		self.root["bg"] = "#b8c4bf"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.resizable(False, False)
		self.root.grab_set()
		self.root.focus_set()
		
		self.draw_widgets_editing()
		
	
		
	def on_closing(self):
		self.root.destroy()
		
	def draw_widgets_editing(self):
		question = "Вопрос номер один"
		self.lbl_question = Label(self.root, text=question, font="Garamond 12 bold",  fg="black")
		self.text_field = ScrolledText(self.root, wrap=WORD)
		self.text_field.insert("1.0", "Some text" * 200)
		self.text_field.configure(state=NORMAL)
		self.text_field.pack()
		
		
		
		