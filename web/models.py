from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


class WeOffer(models.Model):
    heading = models.CharField(max_length=255)
    description = HTMLField(null=True, blank=True)
    order = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "We Offer"

    def __str__(self):
        return str(self.heading)


class EducationalPrograms(models.Model):
    course_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    image = VersatileImageField("Image", upload_to="Course/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    description = HTMLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Educational Programs"

    def __str__(self):
        return str(self.course_name)


class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField("Image", upload_to="Feature/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    order = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return str(self.name)


class SocialMedia(models.Model):
    platform = models.CharField(
        max_length=20,
        choices=[
            ("facebook", "Facebook"),
            ("twitter", "Twitter"),
            ("linkedin", "Linkedin"),
            ("instagram", "Instagram"),
        ],
    )

    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.platform)


class Team(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField("Image", upload_to="Team/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    role = models.CharField(max_length=255)
    order = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return str(self.name)


from django.db import models

class Magazine(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
