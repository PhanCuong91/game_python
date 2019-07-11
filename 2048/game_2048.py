import pygame
import random
import os

matrix = [[2, 0, 0, 0], [0, 4, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
white = (255, 255, 255)


def keyboard():
    res = 'empty'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                res = 'right'
                pass
            if event.key == pygame.K_LEFT:
                res = 'left'
                pass
            if event.key == pygame.K_UP:
                res = 'up'
                pass
            if event.key == pygame.K_DOWN:
                res = 'down'
                pass
    return res


def show(dis, size):
    global matrix
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != 0:
                image = pygame.image.load(os.getcwd()+'\\images\\'+str(matrix[i][j])+'.png')
                dis.blit(image, (j*size, i*size))
    return matrix


def move(direct):
    global matrix
    if direct == 'up':
        for j in range(0, 4):
            for i in range(0, 4):
                # get row that is not zero
                if matrix[i][j] != 0:
                    k = 0
                    # move until cannot move
                    while matrix[i-k-1][j] == 0 and i-k-1 >= 0:
                        temp = matrix[i-k][j]
                        matrix[i-k-1][j] = temp
                        matrix[i-k][j] = 0
                        k += 1
            pass
    elif direct == 'down':
        print('down')
        for j in range(4):
            for i in range(3, -1, -1):
                # get row that is not zero
                if matrix[i][j] != 0:
                    k = 0
                    # move until cannot move
                    while i+k+1 <= 3 and matrix[i+k+1][j] == 0:
                        temp = matrix[i+k][j]
                        matrix[i+k+1][j] = temp
                        matrix[i+k][j] = 0
                        k += 1
        pass
    elif direct == 'left':
        for i in range(0, 4):
            for j in range(0, 4):
                # get row that is not zero
                if matrix[i][j] != 0:
                    k = 0
                    # move until cannot move
                    while matrix[i][j-k-1] == 0 and j-k-1 >= 0:
                        temp = matrix[i][j-k]
                        matrix[i][j-k-1] = temp
                        matrix[i][j-k] = 0
                        k += 1
        pass
    elif direct == 'right':
        for i in range(4):
            for j in range(3, -1, -1):
                # get row that is not zero
                if matrix[i][j] != 0:
                    k = 0
                    # move until cannot move
                    while j+k+1 <= 3 and matrix[i][j+k+1] == 0:
                        temp = matrix[i][j+k]
                        matrix[i][j+k+1] = temp
                        matrix[i][j+k] = 0
                        k += 1
        pass


def merge(direct):
    global matrix
    if direct == 'up':
        for j in range(0, 4):
            for i in range(0, 3):
                # two the nearest blocks have same value
                # then delete one block and assign a new value is 2 times the previous one
                if matrix[i][j] == matrix[i+1][j]:
                    temp = matrix[i][j]
                    matrix[i][j] = temp * 2
                    matrix[i+1][j] = 0
        pass
    elif direct == 'down':
        for j in range(4):
            for i in range(3, -1, -1):
                if matrix[i][j] == matrix[i-1][j]:
                    temp = matrix[i][j]
                    matrix[i][j] = temp * 2
                    matrix[i-1][j] = 0
        pass
    elif direct == 'right':
        for i in range(0, 4):
            for j in range(0, 3):
                if matrix[i][j] == matrix[i][j+1]:
                    temp = matrix[i][j]
                    matrix[i][j] = temp * 2
                    matrix[i][j+1] = 0
        pass
    elif direct == 'left':
        for i in range(4):
            for j in range(3, -1, -1):
                if matrix[i][j] == matrix[i][j-1]:
                    temp = matrix[i][j]
                    matrix[i][j] = temp * 2
                    matrix[i][j-1] = 0
        pass


def random_new():
    global matrix
    # generate randomly 2 or 4
    ran_num = 2**(random.randint(1, 2))
    ran_i = random.randint(0, 3)
    ran_j = random.randint(0, 3)
    # create a new block if the block is not existed
    while matrix[ran_i][ran_j] != 0:
        ran_i = random.randint(0, 3)
        ran_j = random.randint(0, 3)
    # assign generated value to generated block
    matrix[ran_i][ran_j] = ran_num


def check_end_game(matrix):
    temp = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                temp = 1
                break
    if temp == 1:
        pass
    else:
        quit()


def run():
    global matrix
    size = 80
    dis_w, dis_h = 320, 320
    pygame.init()
    dis = pygame.display.set_mode((dis_w, dis_h))
    while True:
        dis.fill(white)
        direct = keyboard()
        merge(direct)
        move(direct)
        check_end_game(matrix)
        if direct != 'empty':
            random_new()
        show(dis, size)
        pygame.display.update()
    return 0


run()
