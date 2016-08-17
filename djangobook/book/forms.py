from django import forms


PARAMETER_CHOICES = (
    ('name', 'Name'),
    ('category', 'Category')
)


class SearchForm(forms.Form):
    query = forms.CharField(label='Search query', max_length=255)
    parameter = forms.ChoiceField(label='Search parameter', choices=PARAMETER_CHOICES)
