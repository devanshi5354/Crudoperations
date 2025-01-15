from django import forms

class EmployeeForm(forms.Form):
    # Define the fields for the form
    emp_id = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Employee ID'}))
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Employee Name'}))
    age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Enter Employee Age'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Employee Email'}))

