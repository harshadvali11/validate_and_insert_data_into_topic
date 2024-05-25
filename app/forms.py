from django import forms

from app.models import *
def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('started with a')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('len must be more than 5')

class TopicForm(forms.Form):
    tn=forms.CharField(validators=[validate_for_a,validate_for_len])


class WebpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    na=forms.CharField(validators=[validate_for_a],label='NAME',help_text='name should not start with a')
    url=forms.URLField()
    email=forms.EmailField()

















