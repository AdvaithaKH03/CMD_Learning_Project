import pygame as pg
import sys
from settings import *
from laws import *

def initial_1():

    entry_prompt()

    a = input("> ")

    if a == "Property 1":
        law_1()

    if a == "Property 2":
        law_2()
 
    if a == "Property 3":
        law_3()

    if a == "Property 4":
        law_4()


            
def run():
    while True:
        initial_1()

if __name__ == '__main__':
    run()