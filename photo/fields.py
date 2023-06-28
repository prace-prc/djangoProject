from django.db.models.fields.files import ImageFieldFile, ImageField


class ThumbnailImageFieldFile(ImageFieldFile):
    pass


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb.width, self.thumb.height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)

