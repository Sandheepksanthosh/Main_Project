from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,VehicleDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def addcategory(req):
    return render(req, "Addcategory.html")


def savecategory(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        img = req.FILES['image']
        obj = CategoryDb(CategoryName=cn, CategoryImage=img)
        obj.save()
        messages.success(req, "Category Added")
        return redirect(addcategory)


def displaycategory(req):
    data = CategoryDb.objects.all()
    return render(req, "Displaycategory.html", {'data': data})


def editcategory(req, editid):
    data = CategoryDb.objects.get(id=editid)
    return render(req, "Editcategory.html", {'data': data})


def updatecategory(req, updateid):
    if req.method == "POST":
        cn = req.POST.get('cname')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=updateid).CategoryImage

        CategoryDb.objects.filter(id=updateid).update(CategoryName=cn, CategoryImage=file)
        messages.success(req, "Category Updated")
        return redirect(displaycategory)


def deletecategory(req, deleid):
    data = CategoryDb.objects.filter(id=deleid)
    data.delete()
    return redirect(displaycategory)

def addvehicles(req):
    category = CategoryDb.objects.all()
    return render(req, "Addvehicles.html", {'category': category})


def savevehicle(req):
    vn = req.POST.get('vname')
    bn = req.POST.get('bname')
    ec = req.POST.get('engcap')
    ml = req.POST.get('mile')
    fc = req.POST.get('fucap')
    mp =r+ req.POST.get('mpower')
    vt = req.POST.get('vtype')
    pr = req.POST.get('price')
    img = req.FILES['image']
    obj = VehicleDb(VehicleName=vn, BrandName=bn, Enginecapacity=ec, Mileage=ml, Fuelcapacity=fc, Maxpower=mp, VehicleType=vt, VehiclePrice=pr, VehicleImage=img)
    obj.save()
    return redirect(addvehicles)


def displayvehicles(req):
    data = VehicleDb.objects.all()
    return render(req, "Displayvehicles.html", {'data': data})


def editvehicle(req, editid):
    data = VehicleDb.objects.get(id=editid)
    return render(req, "Editvehicles.html", {'data': data})


def updatevehicle(req, updateid):
    if req.method == "POST":
        vn = req.POST.get('vname')
        bn = req.POST.get('bname')
        vt = req.POST.get('vtype')
        vp = req.POST.get('price')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = VehicleDb.objects.get(id=updateid).VehicleImage

        VehicleDb.objects.filter(id=updateid).update(VehicleName=vn, BrandName=bn, VehicleType=vt, VehiclePrice=vp, VehicleImage=file)
        return redirect(displayvehicles)


def deletevehicle(req, deleid):
    data = VehicleDb.objects.filter(id=deleid)
    data.delete()
    return redirect(displayvehicles)
