import curses
import random 
import time
MESSAGE = "Hello World!"
UPDATE_RATE = 0.02
def main(win):
    set_color(win)
    print(win)


def set_color(win):
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_GREEN)
    

def print(win):
    
    flag = False 
    current = ""
    count = 0

    while not flag:
        win.clear()
        random_letter = chr(random.randint(1,128))
        if count>100:
            current += MESSAGE[len(current)]
        else:
            current += random_letter
            count += 1

        if current != MESSAGE[:len(current)]:
            win.addstr(0,1,current[:-1],curses.color_pair(2))
            win.addstr(0,len(current),current[-1:],curses.color_pair(1))
            current = current[:-1]
        else:
            win.addstr(0,1,current,curses.color_pair(2))
            count = 0
        if current == MESSAGE:
            break 
        win.refresh()
        time.sleep(UPDATE_RATE)

    # Wait for a keyinput to end the program 
    # Stops the program from ending abruptly
    win.getkey()

curses.wrapper(main)
