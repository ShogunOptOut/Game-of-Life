import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((800, 800))
FPS = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 100)


#variables
field = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
field2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


# Werte setzen (Koordinaten: [Zeile][Spalte])
field[2][3] = 1
field[2][5] = 1
field[3][4] = 1
field[3][5] = 1
field[4][4] = 1

# field2 als echte Kopie erzeugen
field2 = [row.copy() for row in field]

def randomGenerate():
    for i in range(len(field)):
        for x in range(len(field[0])):
            field[i][x] = random.randint(0,1)

randomGenerate()

def drawField():
    for i in range(len(field)):
        for x in range(len(field[0])):
            if field[i][x] == 0:
                pygame.draw.rect(screen, (0,255,0), (80 * i, 80 * x, 80, 80))
            else:
                pygame.draw.rect(screen, (0,0,255), (80 * i, 80 * x, 80, 80))

def nextGeneration():
    for i in range(len(field)):
        for x in range(len(field[0])):
            
            # cells = 0
            # if i < 9 and i > 0 and x < 9 and x > 0:
            cells = countCells (i, x)
        
            if field[i][x] == 0:
                if cells == 3:
                    field2[i][x] = 1
            else:
                if cells < 2:
                    field2[i][x] = 0
                if cells == 2 or cells == 3:
                    field[i][x] = 1
                if cells > 3:
                    field2[i][x] = 0
                    
                    
    for i in range(len(field)):
        for x in range(len(field[0])):
            field[i][x] = field2[i][x]

def countCells(i, x):
    counter = 0
    if field[(i - 1 + 10) % 10][(x + 10 - 1) % 10] == 1:
        counter += 1
    if field[(i - 1 + 10) % 10][(x + 10) % 10] == 1:
        counter += 1
    if field[(i - 1 + 10) % 10][(x + 1 + 10) % 10] == 1:
        counter += 1
    if field[(i + 10) % 10][(x - 1 + 10) % 10] == 1:
        counter += 1
    if field[(i + 10) % 10][(x + 1 + 10) % 10] == 1:
        counter += 1
    if field[(i + 1 + 10) % 10][(x - 1 + 10) % 10] == 1:
        counter += 1
    if field[(i + 1 + 10) % 10][(x + 10) % 10] == 1:
        counter += 1
    if field[(i + 1 + 10) % 10][(x + 1 + 10) % 10] == 1:
        counter += 1
        
    return counter

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            nextGeneration()
            
    #drawField
    drawField()

    pygame.display.update()
    FPS.tick(120)
                
                
