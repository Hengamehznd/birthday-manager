from django.shortcuts import render, redirect
from .models import Birthday
from datetime import datetime

from datetime import datetime


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


def home_view(request):
    all_birthday = Birthday.objects.all()
    return render(request, "home.html", {"all_birthday": all_birthday})


def add_birthday(request, name, birthday):
    dc = DateConverter()
    date = dc.to_python(birthday)
    Birthday.objects.create(name=name, birthday_date=date)

    return redirect("home")
