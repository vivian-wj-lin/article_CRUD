from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    title_image = models.ImageField(upload_to='images/')
    date = models.DateField()

    # 內文相關
    content_title = models.CharField(max_length=255)
    content_description = models.TextField()
    content_image_url = models.URLField(max_length=1000)
    section_image_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(
        Article, related_name='sections', on_delete=models.CASCADE)
    section_title = models.CharField(max_length=255)
    section_content = models.TextField()
    section_link = models.URLField(max_length=1000)
    section_image = models.URLField(max_length=1000)
    section_image_source = models.CharField(max_length=255)

    def __str__(self):
        return self.section_title
