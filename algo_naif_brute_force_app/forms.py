from django import forms


class UploadFilesForm(forms.Form) :
    document1 = forms.FileField(label="Document 01", widget=forms.FileInput(attrs={
        
    }))
    document2 = forms.FileField(label="Document 02")
    pattern_length = forms.IntegerField(required=True, min_value=3, label="Longueur de motif")
