from django import forms
from .models import Toukou, Thread, Otoiawase
from django.utils import timezone
from django.forms import ImageField, forms, CharField, DateTimeField, EmailField, Textarea

class toukouForm(forms.Form):
    class Meta:
        model = Toukou
        fields = "__all__"

    username = CharField(label='名前', required=True)
    time = DateTimeField(label='時間', required=True)
    text = CharField(label='本文', widget = Textarea, required=True)
    image = ImageField(label='画像', required=False) # この行が大切です

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = '風吹けば名無し'
        self.fields['time'].initial = timezone.now()
        self.fields['text'].widget.attrs['placeholder'] = 'テキストを入力してください'

class threadForm(forms.Form):
    class Meta:
        model = Thread
        fields = "__all__"
    title = CharField(label='件名', required=False)
    time = DateTimeField(label='時間', required=False)
    username = CharField(label='名前', required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'スレッド名を入力してください'
        self.fields['username'].widget.attrs['placeholder'] = '名前を入力してください'
        self.fields['time'].initial = timezone.now()

class otoiawaseForm(forms.Form):
    class Meta:
        model = Otoiawase
        fields = "__all__"

    title = CharField(label='件名　　　　　　', required=True)
    time = DateTimeField(label='時間　　　　　　', required=True)
    username = CharField(label='お名前　　　　　', required=True)
    mailadd = EmailField(label='メールアドレス　',required=True)
    text = CharField(label='お問い合わせ内容', widget = Textarea, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '件名を簡潔に入力してください'
        self.fields['username'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['mailadd'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['time'].initial = timezone.now()
        self.fields['text'].widget.attrs['placeholder'] = 'お問い合わせ内容を入力してください'
