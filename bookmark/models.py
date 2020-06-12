from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length = 100)# char인 100byte
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        # reverse 메소드는 URL 패턴의 이름과 추가 인자를 전달받아 URL생성
        return reverse('detail', args=[self.id])