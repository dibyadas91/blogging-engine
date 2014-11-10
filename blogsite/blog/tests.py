from django.core.urlresolvers import reverse
from django.test import TestCase


class PostListViewTests(TestCase):

    def test_post_list_view_get(self):
        response = self.client.get(reverse('PostList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')


class ContactViewTests(TestCase):

    def test_contact_view_get(self):
        response = self.client.get(reverse('Contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_invalid_email(self):
        response = self.client.post(reverse('Contact'), {
            'subject': 'Some subject',
            'message': 'Some message',
            'email': 'dibyagmail.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_missing_email(self):
        response = self.client.post(reverse('Contact'), {
            'subject': 'Some subject',
            'message': 'Some message',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_missing_subject(self):
        response = self.client.post(reverse('Contact'), {
            'message': 'Some message',
            'email': 'dibya@gmail.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_missing_message(self):
        response = self.client.post(reverse('Contact'), {
            'subject': 'Some subject',
            'email': 'dibya@gmail.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post(self):
        response = self.client.post(reverse('Contact'), {
            'subject': 'Some subject',
            'message': 'blah',
            'email': 'dibya@gmail.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('PostList'))

class AboutViewTests(TestCase):
    pass

class HobbiesViewTests(TestCase):
    pass
