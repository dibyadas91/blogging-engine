from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title

# Create new model to store the contact messages in the database
class Contact(models.Model):
    pass

class About(models.Model):

    title = models.CharField(max_length=255)
    about = models.TextField()
