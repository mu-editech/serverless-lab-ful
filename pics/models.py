from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Picture(models.Model):
    """
    写真のフィールドを保持する。

    Attributes
    ----------
    deleted : Boolean
        写真が削除されているかどうか判断するためのフラグ。
    image : Image
        写真データ
    thumbnail : ImageSpecField
        リサイズを行った写真
    """
    deleted = models.BooleanField()
    image = models.ImageField(upload_to='pictures')
    thumbnail = ImageSpecField(source='image',
                            processors=[ResizeToFill(300,300)],
                            format="JPEG",
                            options={'quality': 60}
                            )
