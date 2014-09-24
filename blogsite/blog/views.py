from django.views import generic

from models import Post


class PostView(generic.DetailView):

    model = Post
    template_name = 'post.html'

    def get_template_names(self):
        return self.template_name

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]


class PostListView(generic.ListView):

    model = Post
    template_name = 'post_list.html'
