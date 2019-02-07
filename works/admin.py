from django.contrib import admin

from works.models import Artist, Album, Song, Gallery, Video

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Gallery)
admin.site.register(Video)
