from Tkinter import *
from PIL import ImageTk, Image

# Will load the Main Menu, and we'll start adding buttons, menu's, pictures, explanations etc.
class Main():

	_version="v0.0.1"
	_window_icon = "favicon_icon.ico"
	_menu_graph = "graph.png"
	_contact_no = "(03) 9592 8986"
	_window_width = 600
	_window_height = 600
	
	root=Tk()
	root.resizable(False, False)
	root.title("Reporting App %s" % _version)
	root.iconbitmap(_window_icon)

	main_menu = Frame(root)
	main_menu.grid(row=0)
	
	welcome = Label(main_menu, text="Welcome to Reporting App %s" % _version, font='Helvetica 16 bold')
	contact = Label(main_menu, text="If you have any questions, issues, or feedback, please call Support on %s" % _contact_no, font="Helvetica 11")
	welcome.pack(side=TOP)
	contact.pack(side=TOP)
	button_frame = Frame(main_menu)
	button_frame.pack(side=TOP)
	
	exit = Button(button_frame, command=quit, text="Exit", width=12)
	exit.pack(side=RIGHT, padx=25, pady=5)
	new = Button(button_frame, text="Create", width=12)
	new.pack(side=LEFT, padx=25, pady=5)

	load = Label(main_menu, text="Double click a report from below to load it again", font="Helvetica 11 bold")
	load.pack(side=TOP)

	listbox = Listbox(main_menu)
	listbox.pack(side=TOP)
	listbox.insert(END, "a list entry")
	
	graph = Image.open(_menu_graph)
	graph = graph.resize((550, 300), Image.ANTIALIAS)
	graph = ImageTk.PhotoImage(graph)
	
	panel = Label(main_menu, image=graph)
	panel.pack(side=BOTTOM)
	
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	
	root.geometry("%dx%d+%d+%d" % (_window_width,_window_height,(screen_width/2) - (_window_width/2),(screen_height/2) - (_window_height/2)))

