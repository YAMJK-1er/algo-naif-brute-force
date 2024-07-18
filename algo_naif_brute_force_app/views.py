from django.http import HttpRequest
from .forms import UploadFilesForm
from . utils import *

# Vues pour intercepter les requetes
def algoNaifBruteForceView(request : HttpRequest) :
    uploadFilesForm = UploadFilesForm()

    if request.method == "POST" :
        uploadFilesForm = UploadFilesForm(request.POST, request.FILES)
        if uploadFilesForm.is_valid() :
            document1 = handle_uploaded_file_01(request.FILES["document1"])
            document2 = handle_uploaded_file_02(request.FILES["document2"])

    return render(request, 'index.html', {
        'form' : uploadFilesForm
    })