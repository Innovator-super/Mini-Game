import random
from tkinter import *
from winsound import *
from time import sleep
from parames import *


t=Tk()
t.title('Подножки')
t.resizable(0,0)
t.wm_attributes('-topmost',1)

p = PhotoImage(file = f'./{image_}/Gold_brick_block(1).png')
p3 = PhotoImage(file = f'./{image_}/1png2.png')
p2 = PhotoImage(file = f'./{image_}/1png1.png')
p1 = PhotoImage(file = f'./{image_}/1png.png')
p4 = PhotoImage(file = f'./{image_}/1взрыв1.png')
po = PhotoImage(file = f'./{image_}/стена.png')

canvas = Canvas(width = w, height = h, bd = 0, highlightthickness = 0, bg = 'grey')
canvas.pack()
canvas.create_image(0, 0, image = po, anchor = NW)


class Block():
    def __init__(self, x, y):
        self.x = x * size_blocks
        self.y = y * size_blocks
        self.id = canvas.create_image(self.x, self.y, image = p, anchor = NW)
def create_block():
    global blocks
    while True:
        i = random.randint(0, w // size_blocks - 1)
        j = random.randint(0, h // size_blocks - 1)
        if blocks[i][j] == 0:
            blocks[i][j] = Block(i, j)
            break
blocks = [[False for j in range(h // size_blocks + 1)] for i in range(w // size_blocks + 1)]
for i in range(15):
    create_block()


class Warrior():
    def __init__(self, L, R, U, x, D, x1, but, index):
        self.x1 = x
        self.y1 = h
        self.id = canvas.create_image(x, h, image = p1, anchor = SW)
        self.attacked = False
        self.text_x = x + character_size_x
        self.text_y = h - character_size_y
        self.my = 0
        self.jump = False
        self.y = 0
        self.a = 0
        self.g = 2 ** (-7)
        self.fall = 0
        self.landing = True
        self.health = character_health
        self.x3 = x1
        self.timer = 0
        self.timer_attack = 0
        self.ulta = 0
        self.supered = False


        if index == 1:
            self.id4 = canvas.create_text(self.text_x, self.text_y, text = f"Plaer {index}", fill = 'blue', justify = CENTER, font = "Arial 14")
            self.turn = 'r'
        else:
            self.id4 = canvas.create_text(self.text_x, self.text_y, text = f"Plaer {index}", fill = 'red', justify = CENTER, font = "Arial 14")
            self.turn = 'l'
        self.id2 = canvas.create_line(x1, 30, x1 + self.health, 30, fill = 'red', width = 30)
        self.id3 = canvas.create_line(x1, 50, x1, 50, fill = 'yellow', width = 15)


        canvas.bind_all(f'<KeyPress-{but}>', self.super_1)
        canvas.bind_all(f'<KeyPress-{D}>', self.attack_r)
        canvas.bind_all(f'<KeyPress-{L}>', self.turn_left)
        canvas.bind_all(f'<KeyRelease-{L}>', self.turn2_left)
        canvas.bind_all(f'<KeyPress-{R}>', self.turn_right)
        canvas.bind_all(f'<KeyRelease-{R}>', self.turn2_right)
        canvas.bind_all(f'<KeyPress-{U}>', self.space)


    def super_1(self, zpo):
        self.supered = True


    def attack_r(self,j):
        self.attacked = True


    def space(self, j):
        if self.landing == True:
            self.jump = True
            self.fall = 2
            self.landing = False


    def turn_left(self, j):
        self.my = -1
        self.turn = 'l'


    def turn_right(self, j):
        self.my = 1
        self.turn = 'r'


    def turn2_right(self, j):
        self.my = 0


    def turn2_left(self, j):
        self.my = 0


    def attack(self, id2, helf):
        if self.timer_attack == 0:
            if self.turn == 'r':
                canvas.delete(self.id)
                self.id = canvas.create_image(self.x1, self.y1, image = p3, anchor=SW)
                self.timer = 40
                t.update()
                if self.y1 <= id2.y1 and self.x1 <= id2.x1 and self.x1 >= id2.x1-63 and self.y1 >= id2.y1 - 120:
                    id2.health -= helf
                    if id2.health < 0:
                        id2.health = 0
                    canvas.coords(id2.id2, id2.x3, 30, id2.x3 + id2.health, 30)
                    if self.ulta < ulta:
                        self.ulta += 20
                        canvas.coords(self.id3, self.x3, 50, self.x3 + self.ulta, 50)
            else:
                canvas.delete(self.id)
                self.id = canvas.create_image(self.x1, self.y1,image = p2, anchor = SW)
                self.timer = 40
                t.update()
                if self.y1 <= id2.y1 and self.x1 >= id2.x1 and self.x1 <= id2.x1 + 63 and self.y1 >= id2.y1 - 120:
                    id2.health -= helf
                    if id2.health < 0:
                        id2.health = 0
                    canvas.coords(id2.id2, id2.x3, 30, id2.x3 + id2.health, 30)
                    if self.ulta < 140:
                        self.ulta += 20
                        canvas.coords(self.id3, self.x3, 50, self.x3 + self.ulta, 50)
        self.timer_attack = 40


    def super(self, id2):
        canvas.coords(self.id3, self.x3, 50, self.x3, 50)
        self.ulta = 0
        id2.health -= 50
        if id2.health < 0:
            id2.health = 0
        canvas.coords(id2.id2, id2.x3, 30, id2.x3 + id2.health, 30)
        supe = canvas.create_image(id2.x1 + 35, id2.y1 - 95, image = p4)
        sleep(0.25)
        t.update()
        canvas.delete(supe)
        sleep(0.75)
        t.update()


    def o(self, id2):
        x1 = self.x1 // size_blocks
        y1 = int(self.y1) // size_blocks
        x2 = min(x1 + 1, w // size_blocks)
        y2 = min(y1 + 1, h // size_blocks)
        if self.y1 - 120 <= 0:
            self.fall = 0
        if self.fall <= 0:
            self.landing = False
            for i in [blocks[x1][y1], blocks[x2][y1], blocks[x1][y2], blocks[x2][y2]]:
                if i == False:
                    continue
                if self.x1 + 55 > i.x and self.x1 - 40 < i.x and self.y1 <= i.y and self.y1 > i.y - 3:
                    self.landing = True
                    break
        if self.y1 >= h and self.fall <= 0:
            self.landing = True
        if self.landing:
            self.jump = False
        else:
            self.jump = True
        if self.jump:
            self.fall -= self.g
            self.y1 -= self.fall
            self.text_y -= self.fall
            
        if (self.my < 0 and self.x1 > 0) or (self.my > 0 and self.x1 + 62 < w):
            self.x1 += self.my
            self.text_x += self.my
        if self.supered and self.ulta == 140:
            self.super(id2)
        elif self.attacked:
            if random.randint(0, 100) < 76:
                self.attack(id2, 5)
            else:
                self.attack(id2, 10)
        self.attacked = False
        self.supered = False
        if self.timer == 1:
            canvas.delete(self.id)
            self.id = canvas.create_image(self.x1, self.y1, image = p1,anchor = SW)
        if self.timer > 0:
            self.timer -= 1
        if self.timer_attack > 0:
            self.timer_attack -= 1
        canvas.coords(self.id, self.x1, self.y1)
        canvas.coords(self.id4, self.text_x, self.text_y)
b1=Warrior('a', 'd', 'w', 20, 's', 0, 'q', 1)
b2=Warrior('Left', 'Right', 'Up', w - 20 - 120, 'Down', w - 200, 'm', 2)
while True:
    b1.o(b2)
    b2.o(b1)
    if b2.health <= 0 and b1.health <= 0:
        canvas.create_text(w // 2, h // 2, text = 'Ничья', font = 'Arial 40', fill = 'green')
        break
    elif b2.health <= 0:
        canvas.create_text(w // 2, h // 2, text = 'Игрок слева выйграл', font = 'Arial 40',fill = 'green')
        break
    elif b1.health <= 0:
        canvas.create_text(w // 2,h // 2,text = 'Игрок справа выйграл', font = 'Arial 40', fill = 'green')
        break
    t.update()
PlaySound(f'./{sound}/KO.wav', SND_FILENAME)
t.mainloop()
