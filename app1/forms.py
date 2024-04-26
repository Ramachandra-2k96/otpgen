from django import forms
class inputform(forms.Form):
	quantity=forms.IntegerField(label='Enter the Quantity:',min_value=1,max_value=100000)
	size = forms.IntegerField(label="Enter size:",min_value=1,max_value=30)
