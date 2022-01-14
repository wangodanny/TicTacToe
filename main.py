from turtle import *
from State import *
from is_win import *

def line(a, b, x, y):
    up()
    goto(a,b)
    down()
    goto(x, y)

def draw_grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    line(x,y, x+133, y+133)
    line(x,y+133, x+133, y)

def drawo(x, y):
    up()
    goto(x +67,y+5)
    down()
    circle(62)

def floor(value):
    retun ((value+200)//133) * 133 -200

state = State()

def tap(x,y):
    Screen().onscreenclick(None)
    x = floor(x)
    y = floor(y)
    player = state.player
    grid = state.grid;
    item - state.get_grid_item(x,y)

    if (grid[item[0]][item[1]] is not None):
        print ("Square already taken")
        return

    grid[item[0]][item[1]] = player

    if (player == state.players[0]):
        drawx(x,y)
    else:
        drawo(x,y)
    update()

    if (is_win(grid, item[0], item[1])):
        print("Player " + str(player) + " wins")
        restart()

    state.player = state.switch_player(player)
    Screen.onscreenclick(tap)

def restart():
    Screen.restart()
    hideturtle()
    state.reset()
    draw_grid()
    update()
    Screen().onscreenclick(tap)
    done()

Screen().setup(420,420,370,0)
hideturtle()
Screen.tracer(0,0)
draw_grid()
update()
Screen().onscreenclick(tap)
done()
