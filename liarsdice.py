import random

dice_rolls = [1,2,3,4,5,6]

class Game():

	def __init__(self, d):
		self.num_players = 0
		self.dice_per_player = d
		self.history = []
		self.players = []
		self.started = False
		self.first = True
		self.count = 0

	def add_player(self, player):
		if not self.started:
			self.players.append(player)
			self.num_players += 1

	def start_round(self):
		self.started = True
		for player in self.players:
			roll = []
			for i in range(player.dice):
				roll.append(random.choice(dice_rolls))
			player.roll = roll

	def run_round(self):
		prev_call = None
		call = None
		prev_player = None
		while True:
			prev_player = player
			player = players[self.count % num_players]
			prev_call = call
			call = player.call()
			history.append(call)
			if call == -1:
				total = 0
				amount = call[0]
				num = call[1]
				for player in self.players:
					for roll in players.roll:
						if roll == 1 or roll == num:
							total += 1
				if total >= amount:
					self.players.remove(player)
				else:
					self.players.remove(prev_player)
				self.num_players -= 1
				history = []
			self.count += 1

	def run_game(self):
		while len(players) != 1:
			self.run_round()

class Player():

	def __init__(self, d):
		self.x = 1
		self.dice = d
		self.roll = []
	def call(self, game):
		return -1