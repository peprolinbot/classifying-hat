from django import forms

class ResultsIdForm(forms.Form):
    results_id = forms.CharField(label='Results ID', max_length=24, widget=forms.TextInput(
                              attrs={'class': "hp-font"}))
