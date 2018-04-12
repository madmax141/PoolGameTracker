from django import forms
from .models import Player, Game

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_name']

    def clean_player_name(self):
        player_name = self.cleaned_data['player_name']

        if Player.objects.filter(player_name=player_name).exists():
            raise forms.ValidationError("Player with that name already exists")

        return player_name

class StartGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['player_one', 'player_two']

    def clean(self):
        form_data = self.cleaned_data

        if form_data['player_one'] == form_data['player_two']:
            raise forms.ValidationError("Players need to be unique")

        return form_data