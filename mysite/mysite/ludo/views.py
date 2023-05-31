from django.shortcuts import render
from ludo.models import Station, SubStation

def index(request):
    stations = Station.objects.all()
    substation = {station.name:[sub for sub in SubStation.objects.filter(parent=station)] for station in stations if SubStation.objects.filter(parent=station)}
    print(substation)
    return render(request, "ludo/index.html", context={'stations':stations})

def subindex(request, substation_id):
    station = Station.objects.get(pk=substation_id)
    stations = SubStation.objects.filter(parent=station)
    return render(request, "ludo/index.html",context={"stations":stations})
