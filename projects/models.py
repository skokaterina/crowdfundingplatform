from django.db import models
from django.utils import timezone


class Project(models.Model):
    STATUS_CREATED = 'created'
    STATUS_PUBLISHED = 'published'
    STATUS_SUCCEEDED = 'succeeded'
    STATUS_REMOVED = 'removed'
    STATUS_FAILED = 'failed'

    STATUS_CHOICES = (
        (STATUS_CREATED, 'Created'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_SUCCEEDED, 'Succeeded'),
        (STATUS_REMOVED, 'Removed'),
        (STATUS_FAILED, 'Failed'),
    )
    name = models.CharField(max_length=60)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_started = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.status)
