from django.shortcuts import render
from django.http import JsonResponse
import random
from .models import *
import datetime
import json

# Create your views here.
global day
day = len(DailyPlayer.objects.all())

def index(request):
    get_daily_player()
    day = len(DailyPlayer.objects.all())
    return render(request, 'guessr/index.html', {
        "curDay": day
    })

def get_daily_player():
    today = datetime.date.today()
    
    player = None
    
    daily_player = DailyPlayer.objects.filter(date=today).first()
    
    num_players = len(Player.objects.all())

    if not daily_player:
        player_id = random.randint(1, num_players)
        
        try:
            player = Player.objects.get(pk=player_id)
            daily_player = DailyPlayer(date=today, player=player)
            daily_player.save()
        except Player.DoesNotExist:
            player = Player.objects.get(pk=player_id)
    else:
        player = daily_player.player
    
    return player

def oldday(day):
    p1 = DailyPlayer.objects.get(pk=day)
    return p1

def guesser(request, days):
    todays = oldday(days) 
    p1 = todays.player
    day = len(DailyPlayer.objects.all())
    pstat = Player.objects.get(name=p1)
    stats = PlayerStats.objects.get(player=pstat)
    
    return render(request, "guessr/guesser.html", {
        "todays": todays,
        "day": days,
        "curDay": day,
        'player': pstat,
        'stats': stats
    })

def search(request, player):
    if request.method != 'POST':
        try:
            p1 = Player.objects.filter(name__iexact=player)
            if p1:
                playa = Player.objects.get(name__iexact=player)
                p2 = playa.stat.all()
                resp = list(p1.values())
                p3 = list(p2.values())
                data = {
                    'player': resp,
                    'stats': p3
                }
                return JsonResponse(data, safe=False, status=200)
            else: 
                return JsonResponse({'error': 'Player does not exist.'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Bruh'}, status=400)
        
def get_team(request, id):
    try:
        team = Team.objects.filter(pk=id)
        teams = list(team.values())
        return JsonResponse(teams, safe=False, status=200)
    except KeyError:
        return JsonResponse({'error': 'yea man'}, status=400)
    
def autofill(request, player):
    players = Player.objects.filter(name__icontains=player).values()
    data = {
        'player': list(players),
    }
    return JsonResponse(data, safe=False, status=200)


get_daily_player()