from django.db import models


class Article(models.Model):
    # 標題圖片、標題、小標、日期
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    title_image_url = models.CharField(max_length=1000)
    date = models.DateField()

    # 副標標題、副標說明、副標圖片、副標圖片來源說明、副標圖片來源連結
    subtitle = models.CharField(max_length=50)
    subtitle_description = models.TextField()
    subtitle_image_url = models.URLField(max_length=1000)
    subtitle_imageSource_description = models.CharField(max_length=50)
    subtitle_image_source_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    # 段落、段落內文、段落延伸閱讀標題、段落延伸閱讀連結、段落圖片、段落圖片來源說明、段落圖片連結
    article = models.ForeignKey(
        Article, related_name='sections', on_delete=models.CASCADE)
    section_title = models.CharField(max_length=50)
    section_content = models.TextField()
    section_extended_reading_title = models.CharField(max_length=50)
    section_extended_reading_link = models.URLField(max_length=1000)
    section_image = models.URLField(max_length=1000)
    section_imageSource_description = models.CharField(max_length=1000)
    section_image_link = models.URLField(max_length=1000)

    def __str__(self):
        return self.section_title
