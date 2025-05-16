from django.db import models

class Band(models.Model):
    title = models.CharField(max_length=300)
    startYear = models.IntegerField()
    endYear = models.IntegerField(null=True, blank=True) #NULL if the band is still active (=nowdays)
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='band_images/', null=True, blank=True, default='band_images/default.png')
    link = models.URLField(blank=True, default="#")
    
    def __str__(self):
        return f"{self.title} ({self.startYear} - {self.endYear if self.endYear else 'Nowdays'})"
    

class Album(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField()
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='album_images/', null=True, blank=True, default='album_images/default.png')
    band = models.ForeignKey('Band', null=True, on_delete=models.SET_NULL)
    link = models.URLField(blank=True, default="#")

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.band}"
    
class Artist(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True) #NULL if the artist is still alive
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True, default='artist_images/default.png')

    def __str__(self):
        return f"{self.name} ({self.birth_year} - {self.death_year if self.death_year else 'Today'})"

class Song(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    lyrics = models.TextField(blank=True, default="")
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='song_images/', null=True, blank=True, default='song_images/default.png')
    link = models.URLField(blank=True, default="#")


    def __str__(self):
        return f"{self.title} ({self.album})"

class Genre(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"
    
    
class Instrument(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"


class BandGenre(models.Model):
    band = models.ForeignKey('Band', null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.band} - {self.genre}"


class BandArtist(models.Model):
    band = models.ForeignKey('Band', null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey('Artist', null=True, on_delete=models.SET_NULL)
    startYear = models.IntegerField()
    endYear = models.IntegerField(null=True, blank=True) #NULL if the artist is still part of the band (=nowdays)

    def __str__(self):
        return f"{self.band} - {self.artist} ({self.startYear} - {self.endYear if self.endYear else 'Nowdays'})"


class ArtistInstrument(models.Model):
    artist = models.ForeignKey('Artist', null=True, on_delete=models.SET_NULL)
    instrument = models.ForeignKey('Instrument', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.artist} - {self.instrument}"



