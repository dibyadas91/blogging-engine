from django.core.urlresolvers import reverse
from django.test import TestCase


class PostListViewTests(TestCase):

    def test_post_list_view_get(self):
        response = self.client.get(reverse('PostList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')