from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,VehicleDb
from Frontend.models import Makeatripdb

# Create your views here.
def homepage(req):
    bikes = VehicleDb.objects.all()
    return render(req, "Home.html", {'bikes': bikes})


def aboutuspage(req):
    return render(req, "AboutUs.html")


def bikespage(req):
    bikes = VehicleDb.objects.all()
    return render(req, "Bikes.html", {'bikes': bikes})


def servicespage(req):
    return render(req, "Services.html")


def bikesingle(req, proid):
    data = VehicleDb.objects.get(id=proid)
    return render(req, "BikeSingle.html", {'data': data})


def savetrip(req):
    if req.method == "POST":
        pl = req.POST.get('pulocation')
        pd = req.POST.get('dplocation')
        pdt = req.POST.get('pcdate')
        dfd = req.POST.get('dpdate')
        dfd = req.POST.get('dpdate')
        pt = req.POST.get('putime')
        obj = Makeatripdb(pickup_location=pl, dropoff_location=pd, picup_date=pdt, dropoff_date=dfd, pickup_time=pt)
        obj.save()
        return redirect(bikespage)

