from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from wordcloud import WordCloud
from PIL import Image
from django.template import loader
from janome.tokenizer import Tokenizer
import os

# Create your views here.
class InputForm(forms.Form):
    text = forms.CharField(max_length=999999999, label="target")
    
def register(request):
    if request.POST:
        form = InputForm(request.POST)
        #if form.is_valid():
        if len(request.POST['target']) != 0:
            # ここで受け取った値を処理する。
            #return updated(request)
            updated(request)
            #return HttpResponse(template.render(context, request))
    else:
        try:
            os.remove('media/wordcloud.png')
        except:
            print('Exception!')
        form = InputForm()
    template = loader.get_template('input_form.html')
    context = {
    		'form': form,
    }
    return HttpResponse(template.render(context, request))

def updated(request):

    text = request.POST.get("target")
    fpath = r'msgothic.ttc'

    t = Tokenizer()
    tokens = t.tokenize(text)
    word_list=[]
    for token in tokens:
        word = token.surface
        partOfSpeech = token.part_of_speech.split(',')[0]
        partOfSpeech2 = token.part_of_speech.split(',')[1]
         
        if partOfSpeech == "名詞":
            if (partOfSpeech2 != "非自立") and (partOfSpeech2 != "代名詞") and (partOfSpeech2 != "数"):
                word_list.append(word)
     
    words_wakati=" ".join(word_list)


    wordcloud = WordCloud(width=900, height=900,
                      background_color="white",
                      collocations = False,
                      font_path=fpath)

    wordcloud.generate(words_wakati)
    wordcloud.to_file('media/wordcloud.png')
    
    response = HttpResponse(content_type="image/png")
    img = Image.open('media/wordcloud.png')
    img.save(response,'png')
    #return HttpResponse(message)
    #return response
    return True
