#ok banda hoy hare un vaso, un recipiente en python
import pygame, sys
import numpy as np
import math
import tkinter as tk
from tkinter import ttk
import pandas as pd
import openpyxl
# Initialize the pygame

class The_game:
    def __init__(self):
        pygame.init()
        #Create the self.screen
        self.HEIGHT, self.WIDTH = 600,600
        self.screen = pygame.display.set_mode((self.HEIGHT,self.WIDTH))
        pygame.display.set_caption("Pygame project")
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        #Create the clock
        self.clock = pygame.time.Clock()

        # variables
        self.segundero = 0

        self.cur = [0, 0]
        self.cur_vel = [0, 0]
    def loop(self):
        while True:
            tiempo = pygame.time.get_ticks()
            # LOS CONTROLES
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_w:
                        self.cur_vel[1] = -10
                    if event.key == pygame.K_a:
                        self.cur_vel[0] = -10
                    if event.key == pygame.K_x:
                        pass
                    if event.key == pygame.K_d:
                        self.cur_vel[0] = 10
                    if event.key == pygame.K_s:
                        self.cur_vel[1] = 10
                    if event.key == pygame.K_n:
                        pass
                    if event.key == pygame.K_f:
                        pass
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_w:
                        self.cur_vel[1] = 0
                    if event.key == pygame.K_e:
                        pass
                    if event.key == pygame.K_r:
                        pass
                    if event.key == pygame.K_a:
                        self.cur_vel[0] = 0
                    if event.key == pygame.K_s:
                        self.cur_vel[1] = 0
                    if event.key == pygame.K_d:
                        self.cur_vel[0] = 0
                    if event.key == pygame.K_f:
                        pass




            self.screen.fill((0,0,0))
            # A partir de aqui dibujas
            #print(segundero)
            self.vaso(self.cur[0],self.cur[1],100,100,5)
            #cursor
            self.cur[0] += self.cur_vel[0]
            self.cur[1] += self.cur_vel[1]

            # si toca el siguiente cuadrado
            l = 50
            x,y = 200,200
            self.rect(x,y,l,l)

            if self.cur[0] < 250 and self.cur[0] > 200 and self.cur[1] < 250 and self.cur[1] > 200:
                ventana = Tkinter_display()

            #Aqui termina el loop
            self.segundero = self.segundero + 1
            pygame.display.update()
            self.clock.tick(30)


        
        

    # Funciones de dibujo
    def dot(self,xi,yi,r):
        pygame.draw.circle(self.screen,(255,255,0),(xi,yi),r)
    def line(self,xi,yi,xf,yf):
        pygame.draw.line(self.screen,(255,255,255),(xi,yi),(xf,yf),1)
    def rect(self,xi,yi,w,h):
        pygame.draw.rect(self.screen,(255,255,255),(xi,yi,w,h))
    def text(self,string,xi,yi):
        textsurface = font.render(string,False,(10,100,100))
        self.screen.blit(textsurface,(xi,yi))
    def panel(self,xi,yi,string):
        w,h = 250,40
        pygame.draw.rect(self.screen,(25,25,255),(xi,yi,w,h))
        textsurface = font.render(string,False,(255,255,255))
        self.screen.blit(textsurface,(xi,yi))
    def cursor(self,xi,yi):
        ri,re = 10,12
        pygame.draw.circle(self.screen,(0,0,0),(xi,yi),re)
        pygame.draw.circle(self.screen,(255,255,255),(xi,yi),ri)
    def vaso(self,xi,yi,w,h,e):
        pygame.draw.rect(self.screen,(255,255,255),(xi,yi,w,h))
        pygame.draw.rect(self.screen,(0,0,0),(xi+e,yi,w-2*e,h-e))
class Tkinter_display:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style(self.root)
        self.root.tk.call("source","forest-light.tcl")
        self.root.tk.call("source","forest-dark.tcl")
        self.style.theme_use("forest-dark")


        frame = ttk.Frame(self.root)
        frame.pack()

        widgets_frame = ttk.Labelframe(frame, text="Insert Row")
        widgets_frame.grid(row=0,column=0, padx=20,pady=20)

        button = ttk.Button(widgets_frame, text="Insert", command=self.insert_row)
        button.grid(row=4,column=0,sticky="nsew")

        self.mode_switch = ttk.Checkbutton(widgets_frame, text="Mode", style="Switch", command=self.toggle_mode)
        self.mode_switch.grid(row=6,column=0,padx=5,pady=10,sticky="nsew")

        self.root.mainloop
    def load_data(self):
        path = r'C:\Users\Fer\AppData\Local\Programs\Python\Python310\los_codigos\tkinter\Forest-ttk-theme-master\antoine.xlsx'
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        list_values = list(sheet.values)
    ##    print(list_values)
        for col_name in list_values[0]:
            treeview.heading(col_name,text=col_name)
        for value_tuple in list_values[1:]:
            treeview.insert('',tk.END, values=value_tuple)

    def insert_row(self):
    ##    A = float(spinbox.get())
    ##    print(name,A,subscription,status)
        # Insert row into Excel sheet
        d = The_game()
        d.loop()
        # Insert row into treeview

    def toggle_mode(self):
        if self.mode_switch.instate(["selected"]):
            self.style.theme_use("forest-light")
        else:
            self.style.theme_use("forest-dark")
### AQUI EMPIEZA A CORRER LA EXPERIMENTACION

##ventana_tkinter = Tkinter_display()

juego = The_game()
juego.loop()
