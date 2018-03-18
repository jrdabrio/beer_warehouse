from django.conf import settings
from django.db import models
from django.utils.timezone import now


class CommonInfo(models.Model):
    created_at = models.DateTimeField('Created at', default=now, blank=True)
    modified_at = models.DateTimeField('Modified at', default=now, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 'Created by', related_name='created_items',
                                   blank=True, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, 'Modified by', related_name='modified_items',
                                    blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()
        self.modified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

        class Meta:
            abstract = True
