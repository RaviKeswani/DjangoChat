from django import forms

class StudentFormUpload(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    father_name=forms.CharField(max_length=100)
    dob=forms.DateField()
    gender=forms.ChoiceField(choices=(('Female','Female'),('Male','Male')))
    email=forms.EmailField(max_length=100)
    city=forms.CharField(max_length=100)
    picture=forms.ImageField()