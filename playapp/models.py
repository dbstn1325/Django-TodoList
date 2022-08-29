from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Play(models.Model):
    class PlayType(models.TextChoices):
        JOB = 'JOB', _('업무')
        SOCIAL = 'SOCIAL', _('사회')
        OWN = 'OWN', _('개인')
    title = models.CharField(max_length=90, null=False)
    playType = models.CharField(
        choices=PlayType.choices,
        max_length=25,
        default=PlayType.JOB
    )
    due = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ChecklistItem(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    content = models.CharField(max_length=150, null=False)
    checked = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)



