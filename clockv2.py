import pygame
import math
import datetime
import time

pygame.init()

win = pygame.display.set_mode((600, 600))
bunny = pygame.image.load(r'''.\icons\bunny.png''')
paw = pygame.image.load(r'''.\icons\paw.png''')
paw_firma = pygame.image.load(r'''.\icons\paw_firma.png''')
stars2 = pygame.image.load(r'''.\icons\stars2.png''')

pygame.display.set_caption('Bunny Clock!')

horas = [(300, 150), (375, 175), (425, 225),
              (450, 300), (425, 375), (375, 425),
              (300, 450), (225, 425), (175, 375),
              (150, 300), (175, 225), (225, 175)]
minutos = []


width = 5
lenght = 300
radius = 5
vel = 1
indice_paw = 0




angle = (300, 150)
indice_horas = 0
indice_minutos = 0
indice_segundos = 0
x = 300
y = 150
s = 1



def minutes1(x, y):

    if x < 375 and y < 175:
        return x + 15, y + 5, 1
    elif x < 425 and y < 225:
        return x + 10, y + 10, 1
    elif x < 450 and y < 300: ##
        return x + 5, y + 15, 1
    elif x > 425 and y < 375:
        return x - 5, y + 15, 1
    elif x > 375 and y < 425:
        return x - 10, y + 10, 1
    elif x > 300 and y < 450:
        return x - 15, y + 5, 1

    elif x == 300 and y == 450:
        return 285, 445, 2


def minutes2(x, y):

    if x > 225 and y > 425:
        return x - 15, y - 5, 2
    elif x > 175 and y > 375:
        return x - 10, y - 10, 2
    elif x > 150 and y > 300:
        return x - 5, y - 15, 2 ###
    elif x < 175 and y > 225:
        return x + 5, y - 15, 2
    elif x < 225 and y > 175:
        return x + 10, y - 10, 2
    elif x < 300 and y > 150:
        return x + 15, y - 5, 2
    elif x == 300 and y == 150:
        return 315, 155, 0
    

while True:      
    minutos.append((x, y))
    if s == 1:
        x, y, s = minutes1(x, y)
    elif s == 2:
        x, y, s = minutes2(x, y)
    else:
        break


minuto = 1
run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    ev = pygame.event.get()

    
    now = datetime.datetime.now()
    hora = now.hour if now.hour < 12 else now.hour - 12
    if now.hour < 20 and now.hour > 6:
        bg = (253, 166, 168)
        lindo_rosa = (253, 146, 168)
        segundero = (253, 146, 168)
    else:
        bg = (63, 74, 136)
        lindo_rosa = (27, 36, 110)
        segundero = (63, 74, 136)


    win.fill(bg)
    pygame.draw.circle(win, (255, 255, 255), (300, 300), 200)

#-----SEGUNDOS------------------------------------------------------------
    pygame.draw.line(win, (lindo_rosa), (300, 300), (minutos[now.second]), 2)
#-----MINUTOS----------------------------------------------------------
    pygame.draw.line(win, (0, 0, 0), (300, 300), (minutos[now.minute]), 3)
    pygame.draw.circle(win, (0, 0, 0), (minutos[now.minute]), 5)

#----INDICE MINUTOS/SEGUNDOS---------------------------------------------------------


    if indice_minutos < 60:
        indice_minutos += 1
    else:
        indice_minutos = 0


#-----HORAS---------------------------------------------------------------

    pygame.draw.line(win, (0, 0, 0), (300, 300), (horas[hora]), width)
    pygame.draw.circle(win, (0, 0, 0), (horas[hora]), 6)

    if indice_horas < 11:
        indice_horas += 1
    else:
        indice_horas = 0



#------------------------------------------------------------------------

    
    win.blit(bunny,(275, 275))

    win.blit(stars2,(440, 440))
    if now.second % 5 == 0:
        win.blit(paw, (330, 360))
        win.blit(paw, (220, 220))
        win.blit(paw_firma, (250, 260))

#--NUMEROS--------------------------------------------------------------
    myfont = pygame.font.SysFont("arial", 18)
    title = pygame.font.SysFont("monospace", 25)
    firma = pygame.font.SysFont("monospace", 10)
    other = pygame.font.SysFont("monospace", 15)

    label1 = myfont.render("1", 1, (lindo_rosa))
    label2 = myfont.render("2", 1, (lindo_rosa))
    label3 = myfont.render("3", 1, (lindo_rosa))
    label4 = myfont.render("4", 1, (lindo_rosa))
    label5 = myfont.render("5", 1, (lindo_rosa))
    label6 = myfont.render("6", 1, (lindo_rosa))
    label7 = myfont.render("7", 1, (lindo_rosa))
    label8 = myfont.render("8", 1, (lindo_rosa))
    label9 = myfont.render("9", 1, (lindo_rosa))
    label10 = myfont.render("10", 1, (lindo_rosa))
    label11 = myfont.render("11", 1, (lindo_rosa))
    label0 = myfont.render("00", 1, (lindo_rosa))
    labelf = title.render("Feliz nueva hora!", 3, (0, 0, 0))
    firma_saki = firma.render("by 606, 2019.", 1, (0, 0, 0))
    message = other.render("Even good things can come out of bad times.", 1, (0, 0, 0))



    
    win.blit(label0, (295, 115))
    win.blit(label1, (390, 145))
    win.blit(label2, (445, 205))
    win.blit(label3, (470, 290))
    win.blit(label4, (445, 380))
    win.blit(label5, (385, 440))
    win.blit(label6, (295, 465))
    win.blit(label7, (205, 440))
    win.blit(label8, (145, 375))
    win.blit(label9, (120, 290))
    win.blit(label10, (140, 210))
    win.blit(label11, (200, 145))
    if now.minute == 0:
        win.blit(labelf, (180, 45))
        win.blit(bunny, (80, 25))
        win.blit(bunny, (470, 25))

    win.blit(paw_firma, (480, 568))
    win.blit(firma_saki, (500, 570))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_7]:
        win.blit(message, (50, 525))
        win.blit(paw_firma, (30, 525))
        print('cheer up')

#---------------------------------------------------------------------------
    
    pygame.display.flip()


    
    
    #for x in posiciones
    #pygame.draw.line(win, (0, 0, 0), (300, 300), (a(reloj_a, reloj_b)), width)
    pygame.display.update()
    

pygame.quit()

