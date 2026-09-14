from django.shortcuts import render, redirect, get_object_or_404
from .models import Birthday
from datetime import datetime
from .forms import BirthdayForm

from datetime import datetime


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


def home_view(request):
    form = BirthdayForm()
    all_birthday = Birthday.objects.all()

    context = {
        "all_birthday": all_birthday,
        "form": form,
    }
    return render(request, "home.html", context)


def add_birthday(request):
    if request.method == "POST":
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")


def delete_birthday(request, id):
    person = get_object_or_404(Birthday, id=id)
    person.delete()
    return redirect("home")
