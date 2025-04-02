from django.contrib import admin
from .models import *

class BandAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "startYear", "endYear", "description"]

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "year", "description", "band"]

class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year", "death_year"]

class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class BandGenreAdmin(admin.ModelAdmin):
    list_display = ["id", "band", "genre"]

class BandMemberAdmin(admin.ModelAdmin):
    list_display = ["id", "band", "member"]

class MemberInstrumentAdmin(admin.ModelAdmin):
    list_display = ["id", "member", "instrument"]


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(BandGenre, BandGenreAdmin)
admin.site.register(BandMember, BandMemberAdmin)
admin.site.register(MemberInstrument, MemberInstrumentAdmin)
