from django.core.mail import send_mail
from django.views import generic

from forms import Contact
from models import Post


class PostListView(generic.ListView):

    model = Post
    template_name = 'post_list.html'


class ContactView(generic.FormView):

    form_class = Contact
    template_name = 'contact.html'

    def post(self, request):
        #raise Exception('Hey I am currently in the post method!')
        errors = []
        if request.method == 'POST':
            if not request.POST.get('subject', ''):
                errors.append('Enter a subject.')
            if not request.POST.get('message', ''):
                errors.append('Enter a message.')
            if request.POST.get('email') and '@' not in request.POST['email']:
                errors.append('Enter a valid e-mail address.')
            if not errors:
                send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email', 'dibya.das96@gmail.com'),
                    ['dibya.das96@gmail.com'],
                )
        return self.render_to_response({'errors': errors})

    def get(self, request):
        return self.render_to_response(context={})

#def AboutView(generic.)
