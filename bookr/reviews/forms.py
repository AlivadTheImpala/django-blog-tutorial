from django import forms
from .models import Publisher


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("contributor", "Contributor")
                                  ))


class PublisherForm(forms.ModelForm):
    # this inputs for this form are coming from the Publisher model.
    class Meta:
        model = Publisher
        fields = "__all__"
