
from django.contrib.auth.forms import UserCreationForm
from .models import User,HuaweiTrack
from django import forms
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            # 'huawei_id': forms.CharField(max_length=100),
            'bio': forms.Textarea(attrs={'placeholder': 'Write something about yourself','rows':8}),
        }

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email',
                  'password1', 'password2']
    

class HuaweiTrackForm(forms.ModelForm):
    track = forms.ModelChoiceField(queryset=HuaweiTrack.objects.all())

    class Meta:
        model = HuaweiTrack
        fields = ['track']
