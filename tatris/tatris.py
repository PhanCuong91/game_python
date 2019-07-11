import pygame
import time
import random

dis_w, dis_h = 200, 400
square_size = 10
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
step_d = 1 * square_size
step_l_r = 1 * square_size
save_pos = []
min_col = []
gap_pos = []
t = 0.2
change = False
# S-shape, Z-shape, T-shape, L-shape, Line-shape, MirroredL-shape, and a Square-shape
name_shape = ['s-shape', 's-shape_r_1', 's-shape_r_2', 's-shape_r_3',
              'z-shape', 'z-shape_r_1', 'z-shape_r_2', 'z-shape_r_3',
              't-shape', 't-shape_r_1', 't-shape_r_2', 't-shape_r_3',
              'line-shape', 'line-shape_r_1', 'line-shape_r_2', 'line-shape_r_3',
              'l-shape', 'l-shape_r_1', 'l-shape_r_2', 'l-shape_r_3',
              'mir-l-shape', 'mir-l-shape_r_1', 'mir-l-shape_r_2', 'mir-l-shape_r_3',
              'square-shape', 'square-shape', 'square-shape', 'square-shape']
shape_dic = {'s-shape': [[0, 0], [1, 1], [0, 1], [1, 2]],
             's-shape_r_1': [[1, 0], [2, 0], [1, 1], [0, 1]],
             's-shape_r_2': [[0, 0], [1, 1], [0, 1], [1, 2]],
             's-shape_r_3': [[0, 2], [2, 1], [1, 1], [1, 2]],
             'z-shape': [[0, 1], [1, 1], [1, 0], [0, 2]],
             'z-shape_r_1': [[0, 0], [2, 1], [1, 0], [1, 1]],
             'z-shape_r_2': [[0, 1], [1, 1], [1, 0], [0, 2]],
             'z-shape_r_3': [[0, 0], [2, 1], [1, 0], [1, 1]],
             't-shape': [[0, 1], [2, 1], [1, 0], [1, 1]],
             't-shape_r_1': [[1, 0], [2, 1], [1, 1], [1, 2]],
             't-shape_r_2': [[0, 1], [2, 1], [1, 1], [1, 2]],
             't-shape_r_3': [[0, 1], [1, 1], [1, 0], [1, 2]],
             'l-shape': [[0, 0], [1, 2], [0, 1], [0, 2]],
             'l-shape_r_1': [[0, 2], [2, 2], [1, 2], [0, 3]],
             'l-shape_r_2': [[0, 2], [1, 2], [1, 3], [1, 4]],
             'l-shape_r_3': [[0, 2], [2, 2], [2, 1], [1, 2]],
             'line-shape': [[0, 0], [0, 1], [0, 2], [0, 3]],
             'line-shape_r_1': [[0, 3], [3, 3], [2, 3], [1, 3]],
             'line-shape_r_2': [[0, 0], [0, 1], [0, 2], [0, 3]],
             'line-shape_r_3': [[0, 3], [3, 3], [2, 3], [1, 3]],
             'mir-l-shape': [[0, 2], [1, 1], [1, 0], [1, 2]],
             'mir-l-shape_r_1': [[0, 1], [2, 2], [1, 2], [0, 2]],
             'mir-l-shape_r_2': [[0, 3], [1, 2], [0, 2], [0, 4]],
             'mir-l-shape_r_3': [[0, 2], [2, 2], [1, 2], [2, 3]],
             'square-shape': [[0, 0], [1, 0], [0, 1], [1, 1]]}

def save_finished_shape(shape_pos, saved_pos):
    for i in range(len(shape_pos)):
        saved_pos.append(shape_pos[i])
    return saved_pos


def initial_saved_pos(saved_pos):
    for i in range(0, dis_w, square_size):
        saved_pos.append([i, dis_h])
    return saved_pos


# take second element for sort
def takeSecond(elem):
    return elem[1]


def delete_row(saved_pos):
    """
    :param saved_pos:
    :return:
    """
    global gap_pos
    saved_pos.sort(key=takeSecond)
    count = 0
    del_temp = []
    row = []
    for i in range(len(saved_pos)-1):
        # check each column in same row is  filled
        if save_pos[i][1] == save_pos[i+1][1] and (save_pos[i][1] != dis_h or save_pos[i+1][1] != dis_h):
            count += 1
            # if row is fulfill, save all position of the row and
            if count == int(dis_w/square_size - 1):
                temp = save_pos[i][1]
                row.append(temp)
                for j in range(int(dis_w/square_size)):
                    del_temp.append([j*square_size, temp])
                count = 0
        else:
            count = 0
    # delete row
    for i in range(len(del_temp)):
        print('remove:', del_temp[i])
        print('row: ', row)
        saved_pos.remove(del_temp[i])
    # increase position of other above rows
    for i in range(len(row)):
        for j in range(len(saved_pos)):
            if saved_pos[j][1] < row[i]:
                saved_pos[j][1] = saved_pos[j][1] + square_size
    return saved_pos


def shape_pos_convert(shape):
    """
    the function shall convert position of pixel to position of square (pixel * square_size).
    then use the new position to draw shape
    :param shape: position of pixel
    :return: position of square
    """
    shape_pos = []
    for i in range(len(shape)):
        shape_pos.append([shape[i][0]*square_size, shape[i][1]*square_size])
    return shape_pos


def draw_shape(shape_pos, dis):
    """
    the function shall draw required shape
    :param shape_pos: position of shape
    :param dis: display that contains the shape
    :return: None
    """
    for i in range(len(shape_pos)):
        pygame.draw.rect(dis, red, (shape_pos[i][0], shape_pos[i][1], square_size, square_size), 2)


def rotate_shape(name):
    """
    rotate the shape
    ex: rotate s-shape to s-shape_r_1
    :param name: name of current shape
    :return: name of rotated shape
    """
    div = int(name_shape.index(name) / 4)
    buff = name_shape.index(name) % 4
    if buff == 3:
        # print(name_shape[div * 4])
        return name_shape[div * 4]
    else:
        # print(name_shape[div * 4 + buff + 1])
        return name_shape[div * 4 + buff + 1]


def update_total(total, move_d, move_l, move_r):
    """
    the function shall calculate total move of one shape from beginning
    then the result use for function move_after_rotate()
    :param total: (array int) previous total
    :param move_d: (int)
    :param move_l: (int)
    :param move_r: (int)
    :return: current total
    """
    total[0] += move_d
    total[1] += move_r - move_l
    return total


def move(shape_pos, move_d, move_l, move_r):
    """
    the function shall update new position for the shape
    :param shape_pos: previous position
    :param move_d: move down value in this time
    :param move_l: move left value in this time
    :param move_r: move right value in this time
    :return: current position of shape
    """
    global min_col
    global save_pos
    global change
    for i in range(len(shape_pos)):
        # the next position is blocked by existed shape
        # Since that, cannot move forward and create a new shape
        if shape_pos[i][1] == dis_h or [shape_pos[i][0], shape_pos[i][1]+move_d] in save_pos:
            move_d = 0
            change = True
        # the current x position is 0 or next position is blocked by existed shape
        # Since that, cannot move to left
        if shape_pos[i][0] == 0 or [shape_pos[i][0]-square_size, shape_pos[i][1]] in save_pos:
            move_l = 0
        # the current x position is dis_w - square_size or next position is blocked by existed shape
        # Since that, cannot move to right
        if shape_pos[i][0] == (dis_w - square_size) or [shape_pos[i][0]+square_size, shape_pos[i][1]] in save_pos:
            move_r = 0
    for i in range(len(shape_pos)):
        shape_pos[i][0] += move_r-move_l
        shape_pos[i][1] += move_d
    return shape_pos


def move_after_rotate(shape_pos, total_d, total_l):
    """
    :param shape_pos:
    :param total_d:
    :param total_l:
    :return:
    """
    for i in range(len(shape_pos)):
        shape_pos[i][0] += total_l
        shape_pos[i][1] += total_d
    return shape_pos


def run():
    global save_pos
    global change
    global t
    start = 1
    pygame.init()
    shape_name = 'line-shape'
    dis = pygame.display.set_mode((dis_w, dis_h))
    total = [0, 0]
    shape_pos = 0
    save_pos = initial_saved_pos(save_pos)
    move_l = 0
    move_r = 0
    while True:
        # current move of shape
        # shape always move down
        move_d = 1 * square_size
        # move left or right when pressing respective button
        dis.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    t = 0.05
                elif event.key == pygame.K_LEFT:
                    move_l = step_l_r

                elif event.key == pygame.K_RIGHT:
                    move_r = step_l_r

                elif event.key == pygame.K_UP:
                    # create temp variable and check those are suitable.
                    temp_shape = rotate_shape(shape_name)
                    # print(shape_name)
                    temp_shape_pos = shape_pos_convert(shape_dic[temp_shape])
                    temp = move_after_rotate(temp_shape_pos, total[0], total[1])
                    bol = True
                    for i in range(len(temp)):
                        # if not, do not rotating shape
                        if temp[i][0] < 0 or temp[i][0] > dis_w-square_size:
                            bol = False
                    if bol:
                        shape_pos = temp
                        shape_name = temp_shape
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    t = 0.2
                if event.key == pygame.K_LEFT:
                    t = 0.2
                    move_l = 0
                if event.key == pygame.K_RIGHT:
                    t = 0.2
                    move_r = 0
        if start == 1:
            shape_pos = shape_pos_convert(shape_dic[shape_name])
            start = 0
        else:
            move(shape_pos, move_d, move_l, move_r)
            total = update_total(total, move_d, move_l, move_r)
            if change:
                save_pos = (save_finished_shape(shape_pos, save_pos))
                print('save pos', save_pos)
                print('\n')
                save_pos = delete_row(save_pos)
                print('save pos after', save_pos)
                # create a random shape
                ran = random.randint(0, 27)
                shape_name = name_shape[ran]
                shape_pos = shape_pos_convert(shape_dic[shape_name])
                for j in range(len(shape_pos)):
                    shape_pos[j][0] += int(dis_w/2)
                # clear total after change to next shape
                total = [0, int(dis_w/2)]
                change = False
        draw_shape(shape_pos, dis)
        draw_shape(save_pos, dis)
        pygame.display.update()
        time.sleep(t)


run()


