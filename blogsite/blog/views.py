from django.core.mail import send_mail
from django.shortcuts import redirect
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
        form = Contact(request.POST)
        if form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'dibya.das96@gmail.com'),
                ['dibya.das96@gmail.com'],
            )
            return redirect('PostList')

        return self.render_to_response({'form': form})

    def get(self, request):
        form = Contact()
        return self.render_to_response({'form':form})
