import psychopy
from psychopy import visual
from psychopy import event
from psychopy import clock

# you might wish to play with fullscr, allowGUI and the 'size' options
# so you can make the window full-screen.
win = visual.Window(size=(800, 600), fullscr=False) 

# the movie:
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='flame.avi',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-1.0,
    )
# movie.stop()
# movie.setAutoDraw(True) 


# function to print some text:
def print_some_text(win, string, duration):
    text_obj_2 = visual.TextStim(win, 
    text=string, 
    pos=(0, 0))
    this_clock = clock.Clock()
    while this_clock.getTime() < duration:
        text_obj_2.draw()
        win.flip()
    win.flip()


# function to wait for a key:
def wait_for_key(win, starttext, keys):
    
        # the text:
    text_obj = visual.TextStim(win, 
        text=starttext, 
        pos=(0, 0)
    )

    event.clearEvents()
    press_clock = clock.Clock()
    correctlyPressed = False
    draw_incorr_text = False

    while not correctlyPressed:
    
        text_obj.draw()

        if draw_incorr_text is True and press_clock.getTime() < 1.0:
            incor_text_obj.draw()
        else:
            draw_incorr_text=False
        win.flip()

        evs = event.getKeys(timeStamped=press_clock)
        if len(evs) > 0:
            buttonsPressed, timesPressed = zip(*evs)
            buttonPressed=buttonsPressed[0]

            if buttonsPressed[0] in keys: # f.e. MRI keys
                correctlyPressed = True # here we break the main loop!
            else:
                incor_text_obj = visual.TextStim(win,
                text="wrong button: %s" % (buttonPressed),
                pos=(0, -0.5))

                draw_incorr_text = True
                press_clock.reset()
                
    win.flip()


# function to play the movie:
def play_movie(win, movie):
    timer=clock.Clock()

    movie.seek(0) # go back to 0 seconds
    movie.play() # I think we need to say play...
    while timer.getTime() < movie.duration:
        movie.draw()
        win.flip()
        # the movie already has setAutoDraw() to True, so 
        # we don't have to draw it...
        

        

# Now the flow of the experiment is like so:
wait_for_key(win, 'Press <ENTER> to start', ['5', 'return'])
play_movie(win, movie)
print_some_text(win, 'it''s done', 2.0)


# we can close the window like so:
win.close()
# this will also give some psychopy outputs.