from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

			
tickets = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
post = ["Машинист КУ", "Оператор ТУ", "Слесарь"]


#________METODS___________

# for question as closed programm
def on_closing():
	if messagebox.askokcancel("Выход", "Заверщить программу?   "):
		root.destroy()		

# get text questions and answers from file.txt 
def get_questions_and_answers(file_answers, file_questions, choise_tick, choise_question):	
	try:
		with open(file_questions, "r") as file_1, open(file_answers, "r") as file_2:
		
			f_1 = file_1.readlines()
			f_2 = file_2.readlines()
			answers = {}
			tickets = {}
			questions = {}
			answers_for_ticket = {}
			number_ticket = 1
			strings = ""
			key = 0
			
			for line in f_1:
				if "$" not in line:
					key += 1
					strings = line.replace("$", "")
					questions[key] = strings
					strings = ""
				if len(questions.keys()) == 10:
					tickets[number_ticket] = questions
					questions = {}
					number_ticket += 1
					key = 0
			
			number_ticket = 1
			key = 0

			for line in f_2:
				if "$" not in line:
					strings += line.replace("$", "")
				else:
					key += 1
					answers[key] = strings
					strings = ""
					if len(answers.keys()) == 10:
						answers_for_ticket[number_ticket] = answers
					
						answers = {}
						number_ticket += 1
						key = 0
						
			result_answers = answers_for_ticket[int(choise_tick)]
			selected_ticket = tickets[int(choise_tick)]
			return selected_ticket[choise_question], result_answers[choise_question]
	except Exception:
		show_error("Ошибка!", "Отсутствуют файлы для чтения")

# show error in case no reading file.txt 		
def show_error(title, message):
	messagebox.showerror(title, message)
	root.destroy()
	
# showing info in case non checking ticket or post
def show_info(title_text, info_text):
	info = messagebox.showinfo(title_text, info_text)
	
# show window about_us	
def about_us():
	about_us_window = Toplevel(root)
	about_us_window.title("О программе")
	about_us_window.geometry("200x150+900+800")
	about_us_window.iconbitmap("img/Admin.ico")
	lbl_about_us = Label(about_us_window, text = "Copyright © 2021\n\n"
																		"Author: Mikhail Kayurov\n\n"
																		"GNU(General Public License)\n\n"
																		"Операционная система: Windows XP\n\n"
																		"Версия программы 1.0\n")
	lbl_about_us.pack(pady=10)
	
# ticket selection button previous
def previous_ticket():
	pass
	
# ticket selection button next
def next_ticket():
	pass
		
 #  get entrys and open training_window		
def get_entrys(button):  # we're transferring if need deactive button call training_window

	def select_choise():
					
		choise = choise_questions.get()
		question, answer = get_questions_and_answers(post_ans, post_qst, get_ticket, choise)
		message_text.set(question)
		message_text_two.set(answer)
		
		#_________WIDGETS___________
		# lbl_frame_3 = LabelFrame(training_window, width=910, height=107, bg="#fbfcfd")
		lbl_frame_4= LabelFrame(training_window)
		
		#_________CONFIG ANSWER FIELD___________
		mycanvas = Canvas(lbl_frame_4, width=885, height=378)
		mycanvas.pack(side=LEFT, fill="both", expand="yes")
		
		#___________SCROOLLBAR___________
		yscrollbar = Scrollbar(lbl_frame_4, orient="vertical", command=mycanvas.yview)
		yscrollbar.pack(side=RIGHT, fill="y")
		mycanvas.configure(yscrollcommand=yscrollbar.set)
		mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))
		
		#_________FRAME FOR SCROOLLBAR___________
		myframe =Frame(mycanvas)
		mycanvas.create_window((0,0), window=myframe, anchor="nw")
		
		#__________TEXT MESSAGES IN WINDOW________
		Message(lbl_frame_3, textvariable=message_text, width=800, bg="#fbfcfd", font="Garamond 12 bold").place(x=30, y=10)
		Message(myframe, textvariable=message_text_two, width=800, font="Garamond 12 bold").pack(padx=30)
		
		#_______UNPACKING__________
		lbl_frame_4.place(x=180, y=190)

	get_ticket = ent_ticket.get()
	get_post = ent_post.get()

	if get_ticket == ""  and get_post == "":
		show_info("Внимание!", "Выберите должность и номер билета    ")
		return
	elif get_post == "" and get_ticket:
		show_info("Внимание!", "Укажите должность!    ")
		return
	elif get_ticket == "" and get_post:
		show_info("Внимание!", "Номер билета не выбран!    ")
		return
	elif get_post != "Машинист КУ":
		show_info("Sorry", "Для операторов и слесарей пока не сделал     ")
		return
	
	
	if get_post == "Машинист КУ":
		post_qst = "questions_mash.txt"
		post_ans = "answers_mash.txt"
	elif get_post == "Оператор ТУ":
		post_qst = "" # файл вопросов
		post_ans = ""	 # файл ответов
	
	choise_questions = IntVar()
	message_text = StringVar()
	message_text_two = StringVar()
	
	training_window = Toplevel(root, bg="#e0e5e6")
	training_window.title("Обучение")
	training_window.geometry('1100x600+500+200')
	training_window.resizable(False, False)
	training_window.iconbitmap("img\Tests.ico")
	
	lbl_frame_3 = LabelFrame(training_window, width=930, height=107, bg="#fbfcfd")
	
	lbl_frame_4sub = LabelFrame(training_window)
	mycanvas = Canvas(lbl_frame_4sub, width=902, height=378)
	mycanvas.pack(side=LEFT, fill="both", expand="yes")
	
	lbl_frame_3.place(x=180, y=72)
	lbl_frame_4sub.place(x=180, y=190)
	
	
	#_________WIDGETS___________
	lbl_frame_1 = LabelFrame(training_window, bg="#bec9ca")
	lbl_frame_2 = LabelFrame(training_window, bg="#93a7a6")
	lbl_ticket_number = Label(lbl_frame_2, width=10, fg="white", bg="#93a7a3", text='Билет № {}'.format (get_ticket), font="Garamond 15 bold")
	
	#________BUTTONS_________
	button_left = Button(lbl_frame_2
									, text = "<<<"
									, width=8, bg="#93a7a6"
									, activebackground="#93a7a6"
									, font="Garamond 18 bold"
									, fg="#FFFFFF", activeforeground="#dcdcdc"
									, command=lambda:show_info("Внимание!", "Если ещё раз нажмешь эту кнопку   \n           остановиться КУ-3"))
	button_right = Button(lbl_frame_2
									, text = ">>>"
									, width=8, bg="#93a7a6"
									, activebackground="#93a7a6"
									, font="Garamond 18 bold", fg="#FFFFFF"
									, activeforeground="#dcdcdc"
									, command=lambda:show_info("Внимание!", "А если нажмешь эту кнопку   \n    остановится винтовой"))
									
	button_left["border"] = "0"
	button_right["border"] = "0"
	
	lbl_frame_1.place(x=10, y=72)
	lbl_frame_2.place(x=10, y=10)
	lbl_ticket_number.pack(padx=475, pady=10)
	button_left.place(x=320, y=2)
	button_right.place(x=635, y=2)


	
	#________RADIOBUTTONS________
	for check in tickets:
		if check < 10:
			space = "вопрос № {} ".format(check)
		else:
			space = "вопрос №{}".format(check)
		Radiobutton(lbl_frame_1
								, text=space
								, font="Verdana 9 bold"
								, activebackground="#bec9ca"
								, fg="#00465B", bg="#bec9ca"
								, activeforeground="red"
								, variable=choise_questions
								, value=check
								, command=select_choise).pack(padx=20, pady=13)
	
	# _______UNPACKING__________
	# lbl_frame_1.place(x=10, y=72)
	# lbl_frame_2.place(x=10, y=10)
	# lbl_ticket_number.pack(padx=475, pady=10)
	# btn.place(x=100, y=10)
	
	# deactivate button call training_window
	def on_close():  
		button.configure(state='normal')
		training_window.destroy()
	
	# for deactivate training_window buttons
	button.configure(state='disabled')
	training_window.protocol("WM_DELETE_WINDOW", on_close)


	
#_________ROOT WINDOW_________
root = Tk()
root.title("KC-5")
root.geometry('300x300+900+600')
root["bg"] = "#e0e5e6"
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap("img/Folder.ico")


#_________MENU________________
m = Menu(root)         						 			   						#  Меню на главном окне
root.config(menu=m)                               								# окно конфигурируется с указанием меню для него
fm = Menu(m)                                          								# пункт меню с размещением на основном меню (m)
m.add_cascade(label="Файл",menu=fm, state="disabled")  	   	# каскад выпадающего меню
fm.add_command(label="Новый")            	   							# пункту располагается на основном меню (m)
fm.add_command(label="Открыть...")     	      						# список команд пункта меню
fm.add_command(label="Сохранить...")
fm.add_command(label="Выход", command=root.quit)
hm = Menu(m) 																		#второй пункт меню
m.add_cascade(label="Информация",menu=hm)
hm.add_command(label="Помощь")
hm.add_command(label="О программе...", command=about_us)

#____________WIDGETS______________
frame_1= LabelFrame(root, width=280, height=50, bg="#93a7a6")
frame_2 = LabelFrame(root, width=285, height=130, bg="#bec9ca")
frame_3 = LabelFrame(root, width=285, height=80, bg="#fbfcfd")

lbl_1 = Label(frame_1, text = 'KC - 5', font="Elephant 17",bg="#93a7a6", fg="white")
lbl_2 = Label(frame_2, text = 'должность', bg="#bec9ca")
lbl_3 = Label(frame_2, text = 'билет', bg="#bec9ca")

ent_post = ttk.Combobox(frame_2, width=12, values=post)
ent_ticket = ttk.Combobox(frame_2, width= 3, values=tickets)

btn_image = PhotoImage(file="img/btn_2.png")
btn_1= Button(frame_3, image=btn_image, bg="#fbfcfd", activebackground="#fbfcfd",  command=lambda: get_entrys(btn_1))
btn_1["border"] = "0"

#__________UNPACKING____________
frame_1.place(x=8, y=5)
frame_2.place(x=8, y=52)
frame_3.place(x=8, y=190)
lbl_1.pack(padx=101)
lbl_2.place(x=109, y=8)
ent_post.place(x=90, y=28)
lbl_3.place(x=121, y=64)
ent_ticket.place(x=117, y=84)
btn_1.place(x=65, y=8)

root.mainloop()


