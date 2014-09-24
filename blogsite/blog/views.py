from django.views import generic
from django.http import HttpResponse

from models import Post


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_template_names(self):
        return self.template_name

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")
