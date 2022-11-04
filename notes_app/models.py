from django.db import models

class Note(models.Model):
    title = models.CharField(max_length = 10)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Notes"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

