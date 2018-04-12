from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Player, Game
from .forms import AddPlayerForm, StartGameForm

def index(request):
	return render(request, 'index.html')

def addplayer(request):
	if request.method == 'POST':
		form = AddPlayerForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pooltracker:addplayer'), { 'form': form })
	else:
		form = AddPlayerForm();

	return render(request, 'addplayer.html', { 'form': form })

def leaderboard(request):
	players = Player.objects.order_by('-player_wins')

	return render(request, 'leaderboard.html', { 'players': players })

def startgame(request):
	if request.method == 'POST':
		form = StartGameForm(request.POST);

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pooltracker:activegames'), { 'form': form })
	else:
		form = StartGameForm()

	return render(request, 'startgame.html', { 'form': form })

def activegames(request):
	games = Game.objects.all()

	return render(request, 'activegames.html', { 'games': games })

def endgame(request):
	if request.method == 'POST':
		player = Player.objects.get(pk=request.POST['winner'])
		player.player_wins += 1
		player.save();
		Game.objects.get(pk=request.POST['game_id']).delete()

		return HttpResponseRedirect(reverse('pooltracker:activegames'))
