import time
import sys


def loading(bar_width=40):
	# setup toolbar
	sys.stdout.write("[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line, after '['

	for i in range(bar_width):
	    time.sleep(0.1) # do real work here
	    # update the bar
	    sys.stdout.write("█")
	    sys.stdout.flush()

	sys.stdout.write("]\n") # this ends the progress bar


def create_bar(bar_width=40,bar_text=''):
	sys.stdout.write(bar_text+"[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line, after '['
	
def load(write_num=1):
	sys.stdout.write("█"*write_num)
	sys.stdout.flush()

def end_bar():
	sys.stdout.write("]\n") # this ends the progress bar

