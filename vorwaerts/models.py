from django.db import models
from django.urls import reverse


# Create your models here.
class NewspaperPage(models.Model):
    file_id = models.CharField(max_length=100)
    publish_date = models.DateField(null=True)
    issue_number = models.IntegerField(null=True)
    page_number = models.IntegerField(null=True)
    width = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=5, null=True)

    class Meta:
        indexes = [models.Index(fields=['publish_date', 'page_number'])]
        ordering = ['publish_date', 'page_number']

    def __str__(self):
        return self.image_name

    def get_absolute_url(self):
        return reverse('page_detail', args=[str(self.id)])


class ClassifiedAd(models.Model):
    image_name = models.CharField(max_length=100)
    text = models.TextField()
    newspaper_page = models.ForeignKey(
        NewspaperPage,
        on_delete=models.CASCADE,
        related_name='advertisements',
        related_query_name='advertisment',
    )
