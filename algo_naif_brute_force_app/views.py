from django.http import HttpRequest
from django.shortcuts import render
from .forms import UploadFilesForm
from .utils import *

# Vues pour intercepter les requetes
def algoNaifBruteForceView(request : HttpRequest) :
    uploadFilesForm = UploadFilesForm()

    if request.method == "POST" :
        uploadFilesForm = UploadFilesForm(request.POST, request.FILES)
        if uploadFilesForm.is_valid() :
            document1 = handle_uploaded_file_01(request.FILES["document1"])
            document2 = handle_uploaded_file_02(request.FILES["document2"])

            common_patterns = find_common_patterns(doc1=document1, doc2=document2, pattern_length=int(request.POST.get('pattern_length')));
            words_sim = word_similarity(doc1=document1, doc2=document2)
            sentences_sim = sentence_similarity(doc1=document1, doc2=document2)

            img_path = plot_similarity_statistics(words_sim, sentences_sim, len(common_patterns))

            print(img_path)
            return render(request, 'index.html', {
                'words_sim' : words_sim, 
                'sentences_sim' : sentences_sim,
                'graphiques' : 'similarity_plot.png'
            })
    
    return render(request, 'index.html', {
        'form' : uploadFilesForm
    })