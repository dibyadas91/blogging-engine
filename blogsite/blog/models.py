import os

from string import join
from django.db import models
from django.contrib.auth.models import User
from blogsite.settings import MEDIA_ROOT
from PIL import Image as PImage
from django.core.files import File
from os.path import join as Pjoin
from tempfile import *


class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title


class About(models.Model):

    title = models.CharField(max_length=255)
    about = models.TextField()

    def __unicode__(self):
        return "%s" % self.title


class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)

    def images(self):
        lst =[x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag


class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    thumbnail2 = models.ImageField(upload_to="images", blank=True, null=True)

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, ** kwargs)

        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((128,128), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb2" + ext
        tf2 = NamedTemporaryFile()
        im.save(tf2.name, "JPEG")
        self.thumbnail2.save(thumb_fn, File(open(tf2.name)), save=False)
        tf2.close()

        im.thumbnail((40,40), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + ext
        tf = NamedTemporaryFile()
        im.save(tf.name, "JPEG")
        self.thumbnail2.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

        super(Image, self).save(*args, ** kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def __unicode__(self):
        return self.image.name

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))

    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str(join(lst, ', '))

    def thumbnail(self):
        return """<a href="/static/%s"><img border="0" alt="" src="/static/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True

