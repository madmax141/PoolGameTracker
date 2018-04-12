import datetime

from django.db import models
from django.utils import timezone

class Player(models.Model):
	player_name = models.CharField(max_length=200)
	player_wins = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.player_name

class Game(models.Model):
	player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_one')
	player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_two')

	def __str__(self):
		return str(self.player_one) + ' VS ' + str(self.player_two)
