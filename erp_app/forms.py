from django import forms

class ExpenseForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea(
    attrs={'rows':10, 'cols':30}))
    date_paid = forms.DateField()
    amount_paid = forms.DecimalField()
