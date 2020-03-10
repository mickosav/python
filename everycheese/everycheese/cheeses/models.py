from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# TimeStampedModel automatically gives the model created
# and modified fields which automatically track when
# the object is created or modified
class Cheese(TimeStampedModel):
    name = models.CharField('Name of Cheese', max_length=255)
    slug = AutoSlugField('Cheese Address', unique=True, always_update=False, populate_from='name')
    description = models.TextField('Description', blank=True)