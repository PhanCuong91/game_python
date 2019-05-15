import pygame
import random
import time

dis_w = 400
dis_h = 300
pixel_w, pixel_h = 10, 10
pos = [[200, 150], [190, 150]]


def run():
    prey_x, prey_y = int(random.randint(0, dis_w) / pixel_w) * pixel_w, int(
        random.randint(0, dis_h) / pixel_h) * pixel_h
    pygame.init()
    dis = pygame.display.set_mode((dis_w, dis_h))
    clock = pygame.time.Clock()
    direction = 'R'
    length = 2
    # run game by a loop
    while True:
        dis.fill((255, 255, 255))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'D':
                    direction = 'U'
                elif event.key == pygame.K_DOWN and direction != 'U':
                    direction = 'D'
                elif event.key == pygame.K_LEFT and direction != 'R':
                    direction = 'L'
                elif event.key == pygame.K_RIGHT and direction != 'L':
                    direction = 'R'
        # snake hits the prey
        if pos[0][0] == prey_x and pos[0][1] == prey_y:
            # set new prey
            prey_x, prey_y = int(random.randint(0, dis_w)/pixel_w) * pixel_w, int(random.randint(0, dis_h)/pixel_h) * pixel_h
            # add one rectangle to snake 's body
            if direction == "U":
                pos.append([pos[len(pos) - 1][0], pos[len(pos) - 1][1] - pixel_h])
            elif direction == "D":
                pos.append([pos[len(pos) - 1][0], pos[len(pos) - 1][1] + pixel_h])
            elif direction == 'L':
                pos.append([pos[len(pos) - 1][0] + pixel_w, pos[len(pos) - 1][1]])
            elif direction == 'R':
                pos.append([pos[len(pos) - 1][0] - pixel_w, pos[len(pos) - 1][1]])
            # increase length to 1
            length += 1
        # draw prey
        pygame.draw.rect(dis, (0, 0, 255), (prey_x, prey_y, pixel_w, pixel_h))
        # move snake
        snake(pos, length, direction, dis)
        # update display
        pygame.display.update()
        # speed of game
        time.sleep(0.2)
        # clock.tick(20)


def snake(pos, length, direction, dis):
        # in case, the head is not out of display and hit its body, then run game
        if 0 < pos[0][0] < dis_w and 0 < pos[0][1] < dis_h and not pos[0] in pos[1:length - 1]:
            # save the position of the head
            temp_x = pos[0][0]
            temp_y = pos[0][1]
            # respective action with direction for the head of snake
            if direction == "U":
                pos[0][1] -= pixel_h
            elif direction == "D":
                pos[0][1] += pixel_h
            elif direction == 'L':
                pos[0][0] -= pixel_w
            elif direction == 'R':
                pos[0][0] += pixel_w
            # draw the head
            pygame.draw.rect(dis, (255, 0, 0), (pos[0][0], pos[0][1], pixel_w, pixel_h))
            # update the position of body
            # (the previous point is moved to the current point)
            for i in range(length - 1, 0, -1):
                if i == 1:
                    pos[i][0] = temp_x
                    pos[i][1] = temp_y
                else:
                    pos[i][0] = pos[i - 1][0]
                    pos[i][1] = pos[i - 1][1]
                # draw the body of snake
                pygame.draw.rect(dis, (0, 255, 0), (pos[i][0], pos[i][1], pixel_w, pixel_h))
        # otherwise, end game
        else:
            pygame.quit()
            quit()


run()
