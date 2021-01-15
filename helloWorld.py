import curses
import random 
import time
def main(win):
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_GREEN)
    ANS = "Hello World"
    flag = False 
    current = ""
    count = 0
    while not flag:
        win.clear()
        random_letter = chr(random.randint(1,128))
        if count>50:
            current += ANS[len(current)]
        else:
            current += random_letter
            count += 1

        if current != ANS[:len(current)]:
            win.addstr(0,0,current[:-1],curses.color_pair(2))
            win.addstr(0,len(current)-1,current[-1:],curses.color_pair(1))
            current = current[:-1]
        else:
            win.addstr(0,0,current,curses.color_pair(2))
            count = 0
        if current == ANS:
            break 
        win.refresh()
        # win.getkey()
        time.sleep(0.1)
    win.getkey()

curses.wrapper(main)

# main()
