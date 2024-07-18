from django import forms


class UploadFilesForm(forms.Form) :
    document1 = forms.FileField(label="Document 01", widget=forms.FileInput(attrs={
        'class' : "form-control"
    }))
    document2 = forms.FileField(label="Document 02", widget=forms.FileInput(attrs={
        'class' : "form-control"
    }))
    pattern_length = forms.IntegerField(required=True, min_value=3, label="Longueur de motif", widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Longueur du motif"
    }))
