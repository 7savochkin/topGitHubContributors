from django import forms


class RepositoryForm(forms.Form):
    """Form for validating link to GitHub's repository"""
    repository_url = forms.URLField(label="Link to repository:")
