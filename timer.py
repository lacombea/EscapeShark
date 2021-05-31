import time

class Timer:
	#initialisation : sauvegarde du début de l'heure de jeu
	def __init__(self):
		self.start = time.time()

	#calcul de la durée de la partie et conversion en format heures:minutes:secondes
	def get_time(self):
		end = time.time()
		m, s = divmod(end - self.start, 60)
		h, m = divmod(m, 60)
		time_str = "%02d:%02d:%02d" % (h, m, s)
		return time_str