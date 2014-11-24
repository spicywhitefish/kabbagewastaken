from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(initial=" ", required=False)
    source = forms.ChoiceField(
        choices = (('twitter','twitter'), ('wikipedia','wikipedia'), ('both','both')), required=True
    )