from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        Person.objects.create(name=name, age=age)
        return redirect("/")
    return render(request, "form.html")

def contact(request):
    return HttpResponse("<h1>ติดต่อ: 68043407 นายวรพัธน์ ด้วงแก้ว</h1>")

def edit(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect("/")
    return render(request, "edit.html", {"person": person})

def delete(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        person.delete()
        return redirect("/")
    return render(request, "delete.html", {"person": person})
