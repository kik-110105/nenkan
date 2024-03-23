from django.db import models
from django.utils import timezone
from django.db import models

class Toukou(models.Model):

    username = models.CharField(verbose_name='名前', max_length=32)
    time = models.DateTimeField(verbose_name='時間', default=timezone.now)
    text = models.TextField(verbose_name='本文', max_length=400)
    thread_id = models.IntegerField(verbose_name='スレッドID')
    toukou_id = models.IntegerField(verbose_name='投稿ID')
    delete_TF = models.BooleanField(verbose_name='削除判断用コード', default=False)
    image = models.ImageField(upload_to='images/') # この行が大切です

    def __str__(self):
        return str(self.text) + str(self.thread_id)
    
class Thread(models.Model):

    title = models.CharField(verbose_name='件名', max_length=32)
    time = models.DateTimeField(verbose_name='時間', default=timezone.now)
    username = models.CharField(verbose_name='名前', max_length=32)

    def __str__(self):
        return self.title + ',' + self.username

class Otoiawase(models.Model):
    title = models.CharField(verbose_name='件名', max_length=32)
    time = models.DateTimeField(verbose_name='時間', default=timezone.now)
    username = models.CharField(verbose_name='お名前', max_length=32)
    mailadd = models.EmailField(verbose_name='メールアドレス', max_length=100)
    text = models.TextField(verbose_name='お問い合わせ内容', max_length=400)
    delete_TF = models.BooleanField(verbose_name='解決判断用コード', default=False)

    def __str__(self):
        return self.title + ',' + str(self.time)
