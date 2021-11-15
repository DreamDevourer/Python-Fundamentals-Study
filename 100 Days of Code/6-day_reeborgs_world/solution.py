# Please refer to the json file or this link for understanding the main problem and cross compare with this solution.

def moveUp():
    turn_left()


def moveDown():
    turn_left()
    turn_left()


def moveRight():
    turn_left()
    turn_left()
    turn_left()


if at_goal() != True:
    while front_is_clear():
        move()

    turn_left()

    while at_goal() != True:
        # Basic conditions
        if right_is_clear():
            moveRight()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
