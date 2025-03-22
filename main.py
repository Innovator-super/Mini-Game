import random
from tkinter import *
from winsound import *
t=Tk()
t.title('Подножки')
t.resizable(0,0)
t.wm_attributes('-topmost',1)
w=1260
h=630
p = PhotoImage(file = './Gold_brick_block(1).png')
p3 = PhotoImage(file = './1png2.png')
p2 = PhotoImage(file = './1png1.png')
p1 = PhotoImage(file = './1png.png')
p4 = PhotoImage(file = './1взрыв1.png')
po = PhotoImage(file = './стена.png')
canvas = Canvas(width = w, height = h, bd = 0, highlightthickness = 0, bg = 'grey')
canvas.pack()
canvas.create_image(0, 0, image = po, anchor = NW)
class Block():
    def __init__(self):
        self.x = random.randint(0, w - 70) // 70 * 70
        self.y = random.randint(210, h - 70) // 70 * 70
        self.id = canvas.create_image(self.x, self.y, image = p, anchor = NW)
a = []
for i in range(20):
    a.append(Block())
class Warrior():
    def __init__(self, L, R, U, x, D, x1, but, index):
        self.x1 = x
        self.y1 = h
        self.id = canvas.create_image(x,h,image=p1,anchor=SW)
        self.attacked = ''
        self.x2 = x + 40
        self.y2 = h - 140
        self.my = 0
        self.spaced = 'd'
        self.y = 0
        self.l = True
        self.health = 200
        self.x3 = x1
        self.timer = 0
        self.timer2 = 0
        self.sup = 0
        self.supered = ''
        if index == 1:
            self.id4 = canvas.create_text(x + 40, h - 140, text = f"Plaer {index}", fill = 'blue', justify = CENTER, font = "Arial 14")
            self.turn = 'r'
        else:
            self.id4 = canvas.create_text(x + 40, h - 140, text = f"Plaer {index}", fill = 'red', justify = CENTER, font = "Arial 14")
            self.turn = 'l'
        self.id2 = canvas.create_line(x1, 30,x1 + self.health, 30, fill = 'red', width = 30)
        self.id3 = canvas.create_line(x1, 50, x1, 50, fill = 'yellow', width = 15)
        canvas.bind_all(f'<KeyPress-{but}>', self.super_1)
        canvas.bind_all(f'<KeyPress-{D}>', self.attack_r)
        canvas.bind_all(f'<KeyPress-{L}>', self.turn_left)
        canvas.bind_all(f'<KeyRelease-{L}>', self.turn2_left)
        canvas.bind_all(f'<KeyPress-{R}>', self.turn_right)
        canvas.bind_all(f'<KeyRelease-{R}>', self.turn2_right)
        canvas.bind_all(f'<KeyPress-{U}>', self.space)
    def super_1(self, zpo):
        self.supered = 's'
    def attack_r(self,j):
        self.attacked = 'a'
    def space(self, j):
        if self.l == True:
            self.spaced = 'u'
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
        if self.timer2 == 0:
            if self.turn == 'r':
                canvas.delete(self.id)
                self.id = canvas.create_image(self.x1, self.y1, image = p3, anchor=SW)
                self.timer = 40
                t.update()
                if self.y1<=id2.y1 and self.x1<=id2.x1 and self.x1>=id2.x1-63 and self.y1>=id2.y1-120:
                    id2.health -= helf
                    if id2.health < 0:
                        id2.health = 0
                    canvas.coords(id2.id2, id2.x3, 30, id2.x3 + id2.health, 30)
                    if self.sup < 140:
                        self.sup += 20
                        canvas.coords(self.id3, self.x3, 50, self.x3 + self.sup, 50)
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
                    if self.sup < 140:
                        self.sup += 20
                        canvas.coords(self.id3, self.x3, 50, self.x3 + self.sup, 50)
        self.timer2 = 40
    def super(self, id2):
        canvas.coords(self.id3, self.x3, 50, self.x3, 50)
        self.sup = 0
        id2.health -= 50
        if id2.health < 0:
            id2.health = 0
        canvas.coords(id2.id2, id2.x3, 30, id2.x3 + id2.health, 30)
        supe=canvas.create_image(id2.x1 + 35, id2.y1 - 95, image = p4)
        t.update()
        canvas.delete(supe)
        t.update()
    def o(self, id2):
        self.l = False
        for i in a:
            if self.x1 + 55 > i.x and self.x1 + 30 < i.x + 70 and self.y1 == i.y:
                self.l = True
        if self.y1 == h:
            self.l = True
        if self.l == False and self.spaced == 'd':
            self.y = h
        if self.spaced == 'u':
            self.y += 1
            self.y1 -= 1
            self.y2 -= 1
            if self.y == 300:
                self.spaced = 'd'
            elif self.y1-120 <= 0:
                self.spaced = 'd'
        elif self.spaced == 'd' and self.y != 0:
            self.y -= 1
            self.y1 += 1
            self.y2 += 1
            self.l = False
            for i in a:
                if self.x1 + 55 > i.x and self.x1 + 30 < i.x + 70 and self.y1 == i.y:
                    self.l=True
            if self.y1 == h or self.l == True:
                self.y=0
        if not self.x1 < w - 120 and self.my == 10:
            self.my=0
        elif not self.x1 > 0 and self.my == -10:
            self.my = 0
        if (self.my < 0 and self.x1 > 0) or (self.my > 0 and self.x1 + 62 < w):
            self.x1 += self.my
            self.x2 += self.my
        if self.supered == 's' and self.sup == 140:
            self.super(id2)
        elif self.attacked == 'a':
            if random.randint(0, 100) < 76:
                self.attack(id2, 5)
            else:
                self.attack(id2, 10)
        self.attacked = ''
        self.supered = ''
        if self.timer == 1:
            canvas.delete(self.id)
            self.id = canvas.create_image(self.x1, self.y1, image = p1,anchor = SW)
        if self.timer > 0:
            self.timer -= 1
        if self.timer2 > 0:
            self.timer2 -= 1
        canvas.coords(self.id, self.x1, self.y1)
        canvas.coords(self.id4, self.x2, self.y2)
b1=Warrior('a', 'd', 'w', 20, 's', 0, 'q', 1)
b2=Warrior('Left', 'Right', 'Up', w - 20 - 120, 'Down', w - 200, '/', 2)
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
PlaySound('./KO.wav', SND_FILENAME)
t.mainloop()
