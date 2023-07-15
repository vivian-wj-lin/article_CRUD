from django.db import models


class Article(models.Model):
    # 標題圖片、標題、副標題、日期
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    title_image = models.ImageField(upload_to='images/')
    date = models.DateField()

    # 內文標題、內文說明、內文圖片、內文圖片來源
    content_title = models.CharField(max_length=255)
    content_description = models.TextField()
    content_image_url = models.URLField(max_length=1000)
    content_image_source = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    # 標題1、標題1內文、標題1內文連結、標題1圖片、標題1圖片、標題1圖片來源
    article = models.ForeignKey(
        Article, related_name='sections', on_delete=models.CASCADE)
    section_title = models.CharField(max_length=255)
    section_content = models.TextField()
    section_link = models.URLField(max_length=1000)
    section_image = models.URLField(max_length=1000)
    section_image_source = models.CharField(max_length=500)

    def __str__(self):
        return self.section_title
