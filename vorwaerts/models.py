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
        return self.file_id

    def get_absolute_url(self):
        return reverse('page_detail', args=[str(self.id)])


class ClassifiedAd(models.Model):
    file_id = models.CharField(max_length=100)
    block_id = models.CharField(max_length=5, null=True)
    text = models.TextField()
    x = models.CharField(max_length=5, null=True)
    y = models.CharField(max_length=5, null=True)
    width = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=5, null=True)
    newspaper_page = models.ForeignKey(
        NewspaperPage,
        on_delete=models.CASCADE,
        related_name='advertisements',
        related_query_name='advertisement',
    )
    ocr_confidence = models.FloatField()

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])
