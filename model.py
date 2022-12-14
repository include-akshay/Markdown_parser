from tkinter import * 
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from __init__ import *
import os
from new_md_to_html import new_reg


class Model():

    def __init__(self, controller=None):
        self.controller=controller
        
        dir = os.path.dirname(os.path.abspath(__file__))
        self.path = r"{0}\database_SL\\".format(dir)
        self.path=self.path.replace("\\","\\\\")

    def fetchDirectory(self):
        dir_list=os.listdir(self.path)

        list_of_articles=[]
        for x in dir_list:
            if x.endswith(".md"):
                list_of_articles.append(x[:-3])
        return list_of_articles
    
    def fetch_text(self,file_name):

        text_file=open(file_name,'r' )
        stuff=text_file.read()
        text_file.close()
        return stuff
    
    def generate_html(self,file_path):
        i=len(file_path)-1
        while file_path[i]!="\\":
            i=i-1
        file_name = file_path[i+1:-3]
        print("\n"+file_name)
        stuff = self.fetch_text(file_path)
        return new_reg(stuff,file_name)