from django import forms


class  NewWorkerForm(forms.Form):
    first_name = forms.CharField(label="Your name", max_length=40)
    last_name = forms.CharField(label="Your last name", max_length=40)
    birthday = forms.DateField(required=False)