from django.shortcuts import render

def game_platform(request):
    return render(request, "fourth_task/platform.html")


def game(request):
    games = {'games': ["Atomic Heart","Cyberpank 2077", "PayDay 2"]}
    return render(request, "fourth_task/games.html", context=games)


def cart(request):
    return render(request, "fourth_task/cart.html")






