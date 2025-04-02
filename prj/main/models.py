from django.db import models

class Band(models.Model):
    title = models.CharField(max_length=300)
    startYear = models.IntegerField()
    endYear = models.IntegerField(null=True, blank=True) #NULL if the band is still active (=nowdays)
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='band_images/', null=True, blank=True, default='band_images/default.png')
    
    def __str__(self):
        return f"{self.title} ({self.startYear} - {self.endYear if self.endYear else 'Nowdays'})"
    

class Album(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField()
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='album_images/', null=True, blank=True, default='album_images/default.png')
    band = models.ForeignKey('Band', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.band}"
    
class Member(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True) #NULL if the member is still alive
    image = models.ImageField(upload_to='member_images/', null=True, blank=True, default='member_images/default.png')

    def __str__(self):
        return f"{self.name} ({self.birth_year} - {self.death_year if self.death_year else 'Today'})"


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


class BandMember(models.Model):
    band = models.ForeignKey('Band', null=True, on_delete=models.SET_NULL)
    member = models.ForeignKey('Member', null=True, on_delete=models.SET_NULL)
    startYear = models.IntegerField()
    endYear = models.IntegerField(null=True, blank=True) #NULL if the member is still part of the band (=nowdays)

    def __str__(self):
        return f"{self.band} - {self.member} ({self.startYear} - {self.endYear if self.endYear else 'Nowdays'})"


class MemberInstrument(models.Model):
    member = models.ForeignKey('Member', null=True, on_delete=models.SET_NULL)
    instrument = models.ForeignKey('Instrument', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.member} - {self.instrument}"