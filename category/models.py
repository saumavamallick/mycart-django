from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
import os
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=100,unique=True,blank=True)
    description = models.TextField(max_length=255,blank=True)
    image = models.ImageField(upload_to = 'photos/categories/',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:product_by_category',kwargs={'category_slug':self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
#https://stackoverflow.com/questions/16041232/django-delete-filefield
# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Category)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Category` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Category)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Category` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_image = Category.objects.get(pk=instance.pk).image
    except Category.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
