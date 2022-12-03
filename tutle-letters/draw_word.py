import time
from turtle import *
import math


def circle(radius, extent=360, steps=40, direction='left'):
    dictionary = {'left': left, 'right': right}

    if extent < 360 and steps == 360:
        steps = extent

    theta = extent / steps
    step_size = 2 * radius * math.sin(math.radians(theta / 2))

    dictionary[direction](theta / 2)
    forward(step_size)

    for i in range(1, steps):
        dictionary[direction](theta)
        forward(step_size)

    dictionary[direction](theta / 2)


def draw_letter_a():
    reset()
    lt(90)
    rt(25)
    fd(100)
    rt(130)
    fd(100)
    rt(180)
    fd(50)
    lt(65)
    fd(50)


def draw_letter_b():
    reset()
    lt(90)
    rt(180)
    fd(200)
    lt(90)
    fd(150)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(20)
    lt(20)
    fd(150)
    rt(90)
    fd(130)
    rt(90)
    fd(100)
    rt(20)
    fd(25)
    rt(20)
    fd(25)
    rt(20)
    fd(25)
    rt(20)
    fd(25)
    rt(20)
    fd(23)
    rt(20)
    fd(18)
    rt(20)
    fd(20)
    rt(20)
    fd(25)
    rt(20)
    fd(100)


def draw_letter_c():
    reset()
    lt(160)
    circle(radius=60, extent=230)


def draw_letter_d():
    reset()
    lt(90)
    fd(120)
    rt(90)
    circle(radius=60, extent=180, direction='right')


def draw_letter_e():
    reset()
    bk(30)
    left(90)

    fd(60)

    right(90)
    fd(30)
    bk(30)
    left(90)

    fd(60)

    right(90)
    fd(30)


def draw_letter_f():
    reset()
    lt(90)
    fd(100)
    rt(90)

    fd(50)
    lt(180)
    fd(50)

    lt(90)
    fd(40)
    lt(90)

    fd(40)
    lt(180)
    fd(40)


def draw_letter_g():
    reset()
    lt(90)
    rt(270)
    fd(100)
    lt(90)
    fd(150)
    lt(90)
    fd(100)
    lt(90)
    fd(75)
    lt(90)
    fd(50)


def draw_letter_h():
    reset()
    lt(90)
    fd(100)
    lt(180)
    fd(200)
    lt(180)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(180)
    fd(200)


def draw_letter_i():
    reset()
    lt(90)
    fd(100)


def draw_letter_j():
    reset()
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    rt(180)
    forward(100)
    forward(100)
    lt(180)
    fd(100)
    lt(90)
    fd(200)
    rt(90)
    fd(120)
    rt(90)
    fd(50)


def draw_letter_k():
    reset()
    lt(90)
    fd(150)
    lt(180)
    fd(80)
    lt(150)
    fd(90)
    lt(180)
    fd(90)
    lt(70)
    fd(100)


def draw_letter_l():
    reset()
    lt(90)
    rt(180)
    fd(150)
    lt(90)
    fd(130)


def draw_letter_m():
    reset()
    lt(90)
    fd(150)
    rt(150)
    fd(100)
    lt(120)
    fd(100)
    rt(150)
    fd(150)


def draw_letter_n():
    reset()
    lt(90)
    fd(100)
    rt(150)
    fd(115)
    lt(148)
    fd(100)


def draw_letter_o():
    reset()
    circle(radius=50)


def draw_letter_p():
    reset()
    right(90)
    fd(130)
    bk(50)
    left(90)
    circle(40, 180)


def draw_letter_q():
    reset()
    lt(90)
    lt(180)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(200)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(180)
    fd(100)
    lt(208)
    fd(280)


def draw_letter_r():
    reset()
    lt(90)
    fd(100)
    rt(90)
    fd(70)
    rt(90)
    fd(40)
    rt(90)
    fd(70)
    lt(140)
    fd(90)


def draw_letter_s():
    reset()
    rt(30)
    circle(radius=50, direction='left', extent=195)
    circle(radius=50, direction='right', extent=195)


def draw_letter_t():
    reset()
    lt(90)
    fd(200)
    rt(90)
    fd(90)
    back(180)


def draw_letter_u():
    reset()
    lt(90)
    fd(200)
    lt(180)
    fd(200)
    lt(90)
    fd(100)
    lt(90)
    fd(200)


def draw_letter_v():
    reset()
    lt(90)
    lt(35)
    fd(100)
    bk(100)
    right(70)
    fd(100)


def draw_letter_w():
    reset()
    rt(60)
    fd(100)
    lt(90 + 30)
    fd(100)
    rt(90 + 30)
    fd(100)
    lt(90 + 30)
    fd(100)


def draw_letter_x():
    reset()
    lt(45)
    fd(100)
    bk(50)
    lt(90)
    fd(50)
    bk(100)


def draw_letter_y():
    reset()
    lt(90)
    rt(150)
    fd(100)
    lt(120)
    fd(100)
    rt(180)
    fd(100)
    lt(30)
    fd(100)


def draw_letter_z():
    reset()
    fd(100)
    rt(90 + 45)
    fd(math.sqrt(20000))
    lt(90 + 45)
    fd(100)


speed(10)
# draw_letter_a()
# draw_letter_b()
# draw_letter_c()
# draw_letter_d()
# draw_letter_e()
# draw_letter_f()
# draw_letter_g()
# draw_letter_h()
# draw_letter_i()
# draw_letter_j()
# draw_letter_k()
# draw_letter_l()
# draw_letter_m()
# draw_letter_n()
# draw_letter_o()
# draw_letter_p()
# draw_letter_q()
# draw_letter_r()
# draw_letter_s()
# draw_letter_t()
# draw_letter_u()
# draw_letter_v()
# draw_letter_w()
# draw_letter_x()
# draw_letter_y()
# draw_letter_z()
# done()
alfabet = {
    'a': draw_letter_a,
    'b': draw_letter_b,
    'c': draw_letter_c,
    'd': draw_letter_d,
    'e': draw_letter_e,
    'f': draw_letter_f,
    'g': draw_letter_g,
    'h': draw_letter_h,
    'i': draw_letter_i,
    'j': draw_letter_j,
    'k': draw_letter_k,
    'l': draw_letter_l,
    'm': draw_letter_m,
    'n': draw_letter_n,
    'o': draw_letter_o,
    'p': draw_letter_p,
    'q': draw_letter_q,
    'r': draw_letter_r,
    's': draw_letter_s,
    't': draw_letter_t,
    'u': draw_letter_u,
    'v': draw_letter_v,
    'w': draw_letter_w,
    'x': draw_letter_x,
    'y': draw_letter_y,
    'z': draw_letter_z,
}

setup(width=0.0, height=0.0)
loop = True
while loop:
    command = input('digite um nome \n ou 0 para sair do programa \n')
    if command == "0":
        loop = False
        bye()
    else:
        word = command.lower()
        for letter in word:
            if letter not in alfabet:
                print('nome invalido')
                loop = False
                break
        if not loop:
            break

        setup(width=.5, height=0.75, startx=0, starty=None)
        for letter in word:
            alfabet[letter]()
            time.sleep(0.5)
        reset()
        setup(width=0.0, height=0.0)
