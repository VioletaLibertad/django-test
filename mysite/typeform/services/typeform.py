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
  
  def retrieve_form_answers(self, token):
    endpoint = '{url}forms/{form_id}/responses?included_response_ids={token}'
    url = endpoint.format(url=self.url, form_id=self.form_id, token=token)
    headers = {'Authorization': 'Bearer ' + self.typeform_api_key}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    form_answers = response_json['items'][0]['answers']
    return form_answers