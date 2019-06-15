from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractManager(models.Manager):
    def safe_get(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class AbstractModel(models.Model):
    objects = AbstractManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractModel):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.name


class Area(AbstractModel):
    name = models.CharField(max_length=120)


class Tag(AbstractModel):
    name = models.CharField(max_length=120)


class Yurukai(AbstractModel):
    name = models.CharField(max_length=120)
    tag = models.ManyToManyField(Tag)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)


class Schedule(AbstractModel):
    yurukai = models.ForeignKey(Yurukai, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    members = models.ManyToManyField(User, through="Entry")


class Entry(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_join = models.BooleanField()
    is_teacher = models.BooleanField()
