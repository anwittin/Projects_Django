from django import forms

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id    = forms.IntegerField(widget=forms.HiddenInput)
    #paretnt_id    = forms.IntegerField(widget=froms.HiddenInput, required=False)
    content       = forms.CharField(label='', widget=forms.Textarea)