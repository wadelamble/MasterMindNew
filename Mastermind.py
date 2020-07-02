# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:53:16 2019

@author: MilesL25
"""
import time
from random import seed
from random import randint
import pygame

carryOn = True

pygame.init()
clock = pygame.time.Clock()
purple = (102, 0, 102)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 117, 26)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 210, 0)
blue = (0, 0, 255)
brown = (102, 41, 0)
size = (600, 693)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MasterMind Board")
screen.fill((200, 200, 200))

seconds = round(time.time())

black_pegs = 0
white_pegs = 0
guesses = 0
guess = []
code = []

seed(seconds)
colors = ["red", "orange", "yellow", "green", "blue", "white"]
pos_codes = []
sub_code = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                sub_code = [colors[i], colors[j], colors[k], colors[l]]
                pos_codes.append(sub_code)


def remove_codes(pos_codes, guess, black_pegs, white_pegs):
    new_pos_codes = []
    for pos_code in pos_codes:
        p_black_pegs, p_white_pegs = c_grade(black_pegs, white_pegs, guess, pos_code)
        if p_black_pegs == black_pegs and p_white_pegs == white_pegs:
            new_pos_codes.append(pos_code)
    pos_codes = new_pos_codes
    return pos_codes


def c_code(code):
    # making the randomly generated code
    # FIX
    for i in range(4):
        value = randint(1, 6)
        if value == 1:
            code.append("white")
        elif value == 2:
            code.append("yellow")
        elif value == 3:
            code.append("orange")
        elif value == 4:
            code.append("red")
        elif value == 5:
            code.append("blue")
        elif value == 6:
            code.append("green")
    return code


def h_code(code):
    count = 0
    code = ["black", "black", "black", "black"]
    carryOn = True
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = event.pos
                x = coords[0]
                y = coords[1]
                for i in range(6):
                    offset = 82
                    offset2 = 106
                    if ((offset + i*63) < y < (offset2 + i*63)) and (538 < x < 562):
                        code[count] = colors[i]
                        d_code(code)
                        pygame.display.update()
                        count = count + 1
                if (500 < x < 600) and (630 < y < 693):
                    carryOn = False
    return code


def h_guess(guess):
    guess = ["black", "black", "black", "black"]
    carryOn = True
    count = 0
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = event.pos
                x = coords[0]
                y = coords[1]
                for i in range(6):
                    offset = 82
                    offset2 = 106
                    if ((offset + i * 63) < y < (offset2 + i * 63)) and (538 < x < 562):
                        guess[count] = colors[i]
                        d_guess(guess, guesses)
                        pygame.display.update()
                        count = count + 1
                if (500 < x < 600) and (630 < y < 693):
                    carryOn = False
    return guess


def c_grade(black_pegs, white_pegs, guess, code):
    # grading the guess
    black_pegs = 0
    white_pegs = 0
    guess_2 = []
    code_2 = []
    for i in range(4):
        if code[i] == guess[i]:
            black_pegs = black_pegs + 1
        else:
            guess_2.append(guess[i])
            code_2.append(code[i])

    while len(guess_2) != 0:
        if guess_2[0] in code_2:
            white_pegs = white_pegs + 1
            code_2.remove(guess_2[0])
        guess_2.pop(0)
    return black_pegs, white_pegs


def h_grade(black_pegs, white_pegs):
    black_pegs = 0
    white_pegs = 0
    carryOn = True
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = event.pos
                x = coords[0]
                y = coords[1]
                if (588 < y < 608) and (540 < x < 560):
                    black_pegs = black_pegs + 1
                    d_grade(black_pegs, white_pegs, guesses)
                    pygame.display.update()
                if (525 < y < 545) and (540 < x < 560):
                    white_pegs = white_pegs + 1
                    d_grade(black_pegs, white_pegs, guesses)
                    pygame.display.update()
                if (500 < x < 600) and (630 < y < 693):
                    carryOn = False



    return black_pegs, white_pegs


def c_guess(guess, black_pegs, white_pegs, guesses, pos_codes):
    if guesses == 0:
        guess = ["yellow", "green", "blue", "white"]
    else:
        pos_codes = remove_codes(pos_codes, guess, black_pegs, white_pegs)
        length = len(pos_codes)
        guess = pos_codes[length - 1]

    return guess, pos_codes


def d_code(code):
    x_offset = 80
    y_offset = 31
    for i in range(1, 5):
        if code[i-1] == 'red':
            pygame.draw.circle(screen, red, (x_offset*i, y_offset), 12)
        if code[i-1] == 'orange':
            pygame.draw.circle(screen, orange, (x_offset*i, y_offset), 12)
        if code[i-1] == 'yellow':
            pygame.draw.circle(screen, yellow, (x_offset*i, y_offset), 12)
        if code[i-1] == 'green':
            pygame.draw.circle(screen, green, (x_offset*i, y_offset),12)
        if code[i-1] == 'blue':
            pygame.draw.circle(screen, blue, (x_offset*i, y_offset), 12)
        if code[i-1] == 'white':
            pygame.draw.circle(screen, white, (x_offset*i, y_offset), 12)


def d_guess(guess, guesses):
    x_offset = 80
    y_offset = 94
    for i in range(1, 5):
        x = x_offset*i
        y = y_offset + guesses*63
        r = 12
        if guess[i - 1] == 'red':
            pygame.draw.circle(screen, red, (x, y), r)
        if guess[i - 1] == 'yellow':
            pygame.draw.circle(screen, yellow, (x, y), r)
        if guess[i - 1] == 'orange':
            pygame.draw.circle(screen, orange, (x, y), r)
        if guess[i - 1] == 'white':
            pygame.draw.circle(screen, white, (x, y), r)
        if guess[i - 1] == 'blue':
            pygame.draw.circle(screen, blue, (x, y), r)
        if guess[i - 1] == 'green':
            pygame.draw.circle(screen, green, (x, y), r)


def d_grade(black_pegs, white_pegs, guesses):
    x_offset = 400
    y_offset = 94
    r = 5
    for i in range(1, black_pegs+1):
        x = x_offset + i*20
        y = y_offset + guesses*63
        pygame.draw.circle(screen, red, (x, y), r)
    for i in range((black_pegs+1), (white_pegs + black_pegs + 1)):
        x = x_offset + i*20
        y = y_offset + guesses*63
        pygame.draw.circle(screen, white, (x, y), r)


def d_board():
    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, brown, [0, 0, 500, 693])
    pygame.draw.line(screen, black, (400, 0), (400, 693))
    pygame.draw.rect(screen, (50, 20, 0), [0, 0, 400, 63])
    pygame.draw.line(screen, black, (500, 441), (600, 441))
    pygame.draw.line(screen, black, (500, 630), (600, 630))
    pygame.draw.line(screen, black, (500, 63), (600, 63))
    pygame.draw.line(screen, black, (500, 504), (600, 504))
    pygame.draw.rect(screen, green, [500, 630, 100, 63])
    pygame.draw.rect(screen, (20, 20, 20), [500, 0, 100, 63])
    pygame.draw.rect(screen, (20, 20, 20), [500, 441, 100, 63])
    for i in range(1, 11):
        x = 0
        y = 63*i
        x2 = 500
        y2 = 63*i
        pygame.draw.line(screen, black, (x, y), (x2, y2))
    for i in range(0, 11):
        for j in range(1, 5):
            x = 80*j
            y = 31 + i*63
            r = 12
            x2 = 400 + 20*j
            y2 = y
            r2 = 5
            pygame.draw.circle(screen, black, (x, y), r)
            pygame.draw.circle(screen, black, (x2, y2), r2)
    for i in range(0, 6):
        x_offset = 550
        y_offset = 94
        y = 63 # lazy
        if i == 0:
            pygame.draw.circle(screen, red, (x_offset, y_offset + y*i), 15)
        if i == 1:
            pygame.draw.circle(screen, orange, (x_offset, y_offset + y*i), 15)
        if i == 2:
            pygame.draw.circle(screen, yellow, (x_offset, y_offset + y*i), 15)
        if i == 3:
            pygame.draw.circle(screen, green, (x_offset, y_offset + y*i), 15)
        if i == 4:
            pygame.draw.circle(screen, blue, (x_offset, y_offset + y*i), 15)
        if i == 5:
            pygame.draw.circle(screen, white, (x_offset, y_offset + y*i), 15)

    pygame.draw.circle(screen, white, (550, 535), 10)
    pygame.draw.circle(screen, red, (550, 598), 10)

    write("COLORS", white, 30, [508, 20])
    write("GRADES", white, 30, [508, 461])
    write("ENTER", blue, 30, [515, 650])
    pygame.draw.rect(screen, brown, [401, 0, 99, 63])


def display():
    carryOn = True
    pygame.display.update()
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = event.pos
                x = coords[0]
                y = coords[1]
                if (500 < x < 600) and (630 < y < 693):
                    carryOn = False


def write(msg, color, text_size, text_loc):
    font = pygame.font.SysFont(None, text_size)
    text = font.render(msg, True, color)
    screen.blit(text, text_loc)


def start_screen():
    screen.fill(white)
    msg = "MASTERMIND"
    write(msg, blue, 100, [60, 100])
    msg = "Click B if you want to be the code-breaker..."
    write(msg, purple, 30, [65, 220])
    msg = "...or M if you want to be the code-maker."
    write(msg, purple, 30, [70, 290])
    msg = "Click anywhere for more information."
    write(msg, purple, 30, [85, 360])


def info_screen():
    screen.fill(white)
    write("Welcome to Mastermind!", blue, 15, [50, 50])
    write("As a codebreaker, your goal is to guess the four-digit combination of colors created by the computer.", blue, 15, [50, 70])
    write("Click the icons on the side to guess, and the computer will respond with red or white, in no specific order", blue, 15, [50, 90])
    write("red is used for a piece of the right color in the right place", blue, 15, [50, 110])
    write("white is used for the right color in the wrong place", blue, 15, [50, 130])
    write("Using this information, make your next guess.", blue, 15, [50, 150])
    write("Continue until you correctly guess the computers 4-digit combination.", blue, 15, [50, 170])
    write("As a codemaker, you fulfill the opposite role.", blue, 15, [50, 190])
    write("Create a four-digit combination of colors, and the computer will guess at your combination.", blue, 15, [50, 210])
    write("Signify how close they are by using the smaller red and white icons. Make sure to label their guesses correctly!", blue, 15, [50, 230])
    write("4- Legendary!!!", red, 20, [100, 260])
    write("5- Awesome!!", orange, 20, [100, 285])
    write("6- Good work!", yellow, 20, [100, 310])
    write("7- Okay.", green, 20, [100, 335])
    write("8- Developing :/", blue, 20, [100, 360])
    write("9- YOU SUCK :(", purple, 20, [100, 385])
    write("Good luck! Right click to exit.", black, 30, [50, 430])



def lose_screen():
    screen.fill(white)
    write("You lose.", red, 125, [100, 70])
    write("You trash.", red, 125, [80, 220])
    write("Go outside.", red, 125, [40, 380])


def win_screen(winner):
    if winner:
        screen.fill(white)
        write("Yay! You won.", green, 100, [70, 300])
    else:
        screen.fill(white)
        write("The computer won!", green, 100, [50, 300])


start_screen()
pygame.display.update()
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                main = 'HC'
                carryOn = False
            if event.key == pygame.K_b:
                main = 'CC'
                carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                info_screen()
                pygame.display.update()
            if event.button == 3:
                start_screen()
                pygame.display.update()

d_board()
pygame.display.update()
if main == 'HC':
    while black_pegs < 4:
        if guesses == 0:
            code = h_code(code)
            # d_code(code)
            # pygame.display.update()
        guess, pos_codes = c_guess(guess, black_pegs, white_pegs, guesses, pos_codes)
        d_guess(guess, guesses)
        pygame.display.update()
        black_pegs, white_pegs = h_grade(black_pegs, white_pegs)
        # d_grade(black_pegs, white_pegs, guesses)
        # pygame.display.update()

        guesses = guesses + 1
    winner = False
    win_screen(winner)
elif main == 'CC':
    while black_pegs < 4:
        if guesses == 10:
            lose_screen()
            pygame.display.update()
        if guesses == 0:
            code = c_code(code)
        guess = h_guess(guess)
        # d_guess(guess, guesses)
        # pygame.display.update()
        black_pegs, white_pegs = c_grade(black_pegs, white_pegs, guess, code)
        d_grade(black_pegs, white_pegs, guesses)
        pygame.display.update()

        guesses = guesses + 1
    winner = True
    win_screen(winner)

pygame.quit()



