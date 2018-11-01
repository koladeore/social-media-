# get user model returns user model that crrently active in this project
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

# *args means for however many arguments you take in, it will catch them all,xame as **kwargs but is key word argument like a dict
#  kwargs They are used when you are not sure of the number of keyword arguments that will be passed in the function.
 # put in labels in form in that templates 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
