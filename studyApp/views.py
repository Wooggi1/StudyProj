from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Camera'
    feature1.details = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
                            nostrud exercitation ullamco laboris nisi '''
    feature1.image_path = 'img/gallery/tn/img-11.jpg'
    feature1.is_legal = True
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Eh o dobras'
    feature2.details = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
                            nostrud exercitation ullamco laboris nisi '''
    feature2.image_path = 'img/gallery/tn/img-12.jpg'
    feature2.is_legal = True
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Viado da Nasa'
    feature3.details = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
                            nostrud exercitation ullamco laboris nisi '''
    feature3.image_path = 'img/gallery/tn/img-18.jpg'
    feature3.is_legal = True
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Sorriso Ronaldo isso num eh legal'
    feature4.details = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
                            nostrud exercitation ullamco laboris nisi '''
    feature4.image_path = 'img/gallery/tn/img-26.jpg'
    feature4.is_legal = False
    

    features = [feature1, feature2, feature3, feature4]
    
    return render(request, 'index.html', {'features' : features})

def counter(request):
    text = request.POST['text']
    amountOfWords = len(text.split())
    return render(request, 'counter.html', {'amount': amountOfWords})