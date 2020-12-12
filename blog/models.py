from os.path import splitext
from django.db import models
from imagekit.models import ProcessedImageField
from colorfield.fields import ColorField


def upload_to_image(instance, filename):
    extension = splitext(filename)[1].lower()
    img_name = splitext(filename)[0].replace(" ", "_")
    path = 'images/%(img_name)s' % {'img_name': img_name}
    return '%(path)s%(extension)s' % {'path': path,
                                      'extension': extension}


class Index(models.Model):
    image = ProcessedImageField(upload_to=upload_to_image, format='JPEG', blank=True)
    color = ColorField(default='#FF0000')

    def remove_on_image_update(self):
        try:
            obj = Index.objects.get(id=self.id)
        except Index.DoesNotExist:
            return
        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super(Index, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.remove_on_image_update()
        return super(Index, self).save(*args, **kwargs)

    class Meta:
        db_table = 'index'
