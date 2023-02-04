from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method=='POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("First name",form.cleaned_data['firstName'])
            print("First name",form.cleaned_data['lastName'])
            print("First name",form.cleaned_data['email'])
            
    
    return render (request,'regitsration.html',{'form':form})
