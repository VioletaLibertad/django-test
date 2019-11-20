import requests


class Typeform:
  url = 'https://api.typeform.com/'
  form_id = None
  typeform_api_key = '9eJMGunGujK24qnK1eomAe3dT623kherz7VKVoujNK95'

  def __init__(self, form_id):
    self.form_id = form_id

  def retrieve_form_questions(self):
    response = requests.get(self.url + 'forms/' + self.form_id)
    form_response = response.json()
    form = {'form_name': form_response['title']}
    questions = []  
    for field in form_response['fields']:
        question = {'id': field['id'], 'name': field['title']}
        questions.append(question)
    form['questions'] = questions
    return form