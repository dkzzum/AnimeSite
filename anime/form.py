from django import forms


class CommentariesForm(forms.Form):
    commentaries = forms.CharField(min_length=1, max_length=10000, widget=forms.Textarea())
