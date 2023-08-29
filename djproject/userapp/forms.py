from django.forms import ModelForm


from .models import UserDetails 


class UserForm(ModelForm):
    clas Meta:
       model=UserDetails
