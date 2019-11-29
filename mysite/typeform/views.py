from django.shortcuts import render
import requests
from .services.typeform import Typeform


def retrieve_form_questions(request):
    typeform_instance = Typeform('tO8Dy6')
    form_data = typeform_instance.retrieve_form_questions()
    form_answers = typeform_instance.retrieve_form_answers(
        'ugdco41myb5nco9odugdco4hpoqqa81w'
    )
    complete_form = {'form_name': form_data['form_name']}
    data_set = []
    for question in form_data['questions']:
        for answers in form_answers:
            if question['id'] == answers['field']['id']:
                data = {
                    'id': question['id'],
                    'question': question['name'],
                    'answer': answers}
                data_set.append(data)
    complete_form['data'] = data_set
    return render(request, 'blog/results.html', {
        'complete_form': complete_form
    })
