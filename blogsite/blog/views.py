from django.views import generic

from models import Post, Contact


class PostListView(generic.ListView):

    model = Post
    template_name = 'post_list.html'


class ContactView(generic.FormView):

    model = Contact
    template_name = 'contact.html'
