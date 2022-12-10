from django import forms 


class StartForm(forms.Form):
    input = forms.CharField(max_length=1000, label='Enter Here')
    
class p1Form(forms.Form):
    btn = forms.CharField()
    
class p1_1Form(forms.Form):
    btn = forms.CharField()
    
class p1_2Form(forms.Form):
    btn = forms.CharField()
    
class p2Form(forms.Form):
    budget = forms.IntegerField(min_value=1)