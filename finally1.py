from email.mime import image
from tkinter import * 
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from __init__ import *
import os
from PIL import ImageTk, Image
from md_to_html import reg

class Finally(tk.Tk):


    def __init__(self): 
        super().__init__()
        self.title("MY WIKI")
        self.geometry("1460x820")
        #self.wm_iconbitmap("1.ico")

        
        self.edit_this_var=""
        self.edit=False
        self.opened=False
        

        self.initializeFrames()
        self.initialize_top_frame()
        self.initialize_left_frame()
        self.initialize_middle_frame()
        self.initialize_right_frame()
        
        self.initialize_menu()



        self.mainloop()
    
  


    '''function use to save files, there are two cases encountered here, i) when a file was opened in the middle frame and also the edit 
       command was activated, in this case the selected file will just be overwritten with what is newly edited.
       ii) when a new file is being created.
    '''
    def save_file_as(self):   
        if self.edit==True and self.opened==True:

            self.edit=False
            
           
            with open(self.edit_this_var, 'r+') as f:
                
                
                f.seek(0) 
                f.truncate() 
                
                f.write(self.text_area.get('1.0', tk.END))
                f.close()
            
            self.text_area.delete(1.0, END)
            
        else:
            try:
                path = filedialog.asksaveasfile(filetypes = (("MD File", "*.md"),("All files", "*.*"))).name

            
            except:
                return   
            
            with open(path, 'w') as f:
                f.write(self.text_area.get('1.0', tk.END))
            
            # for updating the list of articles on left frame
            path="E:\SL_Project_mywiki\COP702_1\database_SL"
            dir_list=os.listdir(path)

            list_of_articles="𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝚁𝚃𝙸𝙲𝙻𝙴𝚂 <br> <br>"
            for x in dir_list:
                if x.endswith(".md"):
                    list_of_articles= list_of_articles + f"<a href='{path}\{x}'> {x[:-3]} </a><br>"

            self.left_label.set_html(list_of_articles)

            
    
        
    #function is binded with the event when the textbox for creating artciles is modified, basically for live rendering
    def inputEditorChange(self,event):
        self.text_area.edit_modified(0)
        markdownText = self.text_area.get("1.0", "end")
        html = reg(markdownText)
        self.Label_renderer.set_html(html)

    # function to display the contents of opened file in the editable textbox when edit button was pressed.
    def edit_file(self):
        self.edit=True
       
        if self.opened==True:
            to_read=open(self.edit_this_var,'r' )
            stuff=to_read.read()
            self.text_area.delete(1.0, END)
            self.text_area.insert(1.0,stuff)
            to_read.close()


    # frames ###############################################################################################################

    def initializeFrames(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=26)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=18)
        self.columnconfigure(2,weight=6)
        

        self.top_frame=LabelFrame(self, bg="light blue", width="1")
        self.top_frame.grid(row=0, column=0, columnspan=3,sticky = W, pady = 20)

        self.left_frame=LabelFrame(self)
        self.left_frame.grid(row=1, column=0, rowspan=2,sticky = W, pady = 2)

        self.middle_frame=LabelFrame(self)
        self.middle_frame.grid(row=1, column=1, rowspan=2, pady = 2)

        self.right_frame=LabelFrame(self)
        self.right_frame.grid(row=1,column=2,sticky = E, pady = 2)

        self.right_frame.rowconfigure(0, weight=4)
        self.right_frame.rowconfigure(1, weight=1)


    # frames end ###########################################################################################################

    # menubar ##############################################################################################################

    def initialize_menu(self):
        mainmenu=Menu(self)
        mainmenu.add_command(label=" SAVE ", command=self.save_file_as)
        mainmenu.add_command(label=" EDIT ", command=self.edit_file)


        self.config(menu=mainmenu)
       
    #######################################################################################################################


    # initializing top frame################################################################################################

    def initialize_top_frame(self):
        # img = Image.open("1.png")
        # resize_img = img.resize((60 ,55))
        # img = ImageTk.PhotoImage(resize_img)
        # image_label=Label(self.top_frame,image=img, padx=1000)
        # image_label.grid(row=0, column=1,sticky = W, pady = 2)
        # self.image_label=img
        heading=Label(self.top_frame, text="OUR-PEDIA", font="Algerian 34 bold", bg="lightblue")
        heading.grid(row=0, column=2,sticky = W, pady = 10, padx=600)

    ########################################################################################################################


    # populating right frame #############################################################################################

    def initialize_right_frame(self):
        self.text_area=scrolledtext.ScrolledText(self.right_frame,  wrap=tk.WORD ,bg="gray", fg="white", font="arial 15", insertofftime=5, 
                                            insertontime=15, width="50")
        self.text_area.grid(row=0, column=0,sticky = W, pady = 2)
        self.text_area.bind("<<Modified>>", self.inputEditorChange)

        self.Label_renderer=HTMLScrolledText(self.right_frame, html="<p>Type Above to  <b>CREATE NEW</b></p>", background="lightblue", width="68")
        self.Label_renderer.grid(row=1, column=0, pady = 2)


    #######################################################################################################################


    # populating middle frame #############################################################################################

    def initialize_middle_frame(self):

        # img1 = ImageTk.PhotoImage(Image.open("light.jpg"))
        self.Read_renderer=HTMLScrolledText(self.middle_frame, html="Here the selected article will appear",container=self, 
                                     background="lightpink", fg="white",state="disabled", width="70", height="44")
        self.Read_renderer.grid(sticky = W, pady = 2)

     #######################################################################################################################


    # Populating left frame.###############################################################################################

    def initialize_left_frame(self):

        self.left_label=HTMLScrolledText(self.left_frame, container=self, width="30", height="44")

        path="/home/anurag/work/Markdown_parser"
        dir_list=os.listdir(path)

        list_of_articles="𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝚁𝚃𝙸𝙲𝙻𝙴𝚂 <br> <br>"
        for x in dir_list:
            if x.endswith(".md"):
                list_of_articles= list_of_articles + f"<a href='{path}\{x}'> {x[:-3]} </a><br>"

        self.left_label.set_html(list_of_articles)
        self.left_label.configure(state='disabled')
        self.left_label.grid(sticky = W, pady = 2)

    ######################################################################################################################

Finally()