import time

#from app import *

class Timer:
	def __init__(self):
		self.start = time.time()

	def get_time(self):
		end = time.time()
		m, s = divmod(end - self.start, 60)
		h, m = divmod(m, 60)
		time_str = "%02d:%02d:%02d" % (h, m, s)
		return time_str