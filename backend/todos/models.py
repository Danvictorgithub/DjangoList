from audioop import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

class Todo(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    isFinished = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})


