from django.shortcuts import render
import requests
from .services.typeform import Typeform


def retrieve_form_questions(request):
    typeform_instance = Typeform('tO8Dy6')
    form_data = typeform_instance.retrieve_form_questions()
    return render(request, 'blog/results.html', {
        'form': form_data, 
    })



# def retrieve_form_questions(request):
#     response = requests.get('https://api.typeform.com/forms/tO8Dy6')
#     form_response = response.json()
#     questions = []
#     for field in form_response['fields']:
#         questions.append(field['title'])
#     return render(request, 'blog/results.html', {
#         'questions': questions, 
#         'title': form_response['title']
#         })