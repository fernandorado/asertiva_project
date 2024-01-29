from wagtail.images.formats import Format, register_image_format

register_image_format(Format('img-fluid', 'Imagen Responsiva', 'richtext-image img-fluid', 'original'))