from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField


class CreationModel(models.Model):
    """An abstract base class model that provides self-updating ``created_at`` and ``created_by`` fields.
    """
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, editable=False,
                                      help_text=_('Date when it was created.'))
    created_by = CurrentUserField(verbose_name=_('Created by'), related_name='created_%(class)s',
                                  help_text=_('User who created it.'))

    class Meta:
        abstract = True
