from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Profile(models.Model):

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    photo = models.ImageField(upload_to='profile', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    hackerspace = models.TextField(blank=True, null=True)
    os = models.TextField(blank=True, null=True)
    programming_languages = models.TextField(blank=True, null=True)
    conventions = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    STARWARS_VS_STARTREK_CHOICES = (
        (u'sw', u'Starwars'),
        (u'st', u'Startrek'),
        (u'sg', u'Stargate'),
    )
    starwars_vs_startrek = models.CharField(max_length=2, 
                                            choices=STARWARS_VS_STARTREK_CHOICES)
    brony = models.BooleanField()
    search = models.TextField(blank=True, null=True)
    freetext = models.TextField(blank=True, null=True)
    hipster = models.TextField()

    last_update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('profiledetail', args=[self.user.username])

    def __unicode__(self):
        return "%s [%s %s]" % (self.user, self.first_name, self.last_name)

