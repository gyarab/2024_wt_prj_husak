from django.contrib import admin
from .models import *

class BandAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "startYear", "endYear", "description", "link"]

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "year", "description", "band", "link"]

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year", "death_year"]

class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "album", "link"]

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class BandGenreAdmin(admin.ModelAdmin):
    list_display = ["id", "band", "genre"]

class BandArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "band", "artist"]

class ArtistInstrumentAdmin(admin.ModelAdmin):
    list_display = ["id", "artist", "instrument"]


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(BandGenre, BandGenreAdmin)
admin.site.register(BandArtist, BandArtistAdmin)
admin.site.register(ArtistInstrument, ArtistInstrumentAdmin)
