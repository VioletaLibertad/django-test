from django.shortcuts import render
from blog.forms import ContactForm


def custom_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()
    return render(request, 'blog/custom_form_b.html', {'form': form})
