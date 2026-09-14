from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ["name", "birthday_date", "relation"]
        # labels = {
        #     "name": "نام و نام خانوادگی",
        #     "birthday_date": "تاریخ تولد",
        #     "relation": "نسبت",
        # }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام و نام خانوادگی",
                    "required": True,
                }
            ),
            "birthday_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "required": True,
                }
            ),
            "relation": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
