from django.db import models
from rusilomer.utils import location_geoconing



class Location(models.Model):
    class Meta:
        verbose_name = ('Место проведения')
        verbose_name_plural = ('Места проведения')

    city = models.CharField('Город' ,max_length=30,)
    venue = models.CharField('Точка сбора', max_length=40)
    gps_lat = models.CharField(max_length=30,editable=False)
    gps_lng = models.CharField(max_length=30,editable=False)

    def save(self, *args, **kwargs):
        from rusilomer.utils import location_geoconing
        geocod = location_geoconing(self.city, self.venue)
        self.gps_lat = geocod['lat']
        self.gps_lng = geocod['lng']
        super(Location, self).save(*args,**kwargs)

    def __str__(self):
        return '%s , гор.%s' %(self.venue, self.city)

# class Content(models.Model):
#     class Meta:
#         verbose_name = ('')
#         verbose_name_plural = ('')
#
#     pass
#
#
# class Media(models.Model):
#     class Meta:
#         verbose_name = ('')
#         verbose_name_plural = ('')
#
#     pass
#
class News(models.Model):
    class Meta:
        verbose_name = ('Новость')
        verbose_name_plural = ('Новости')

    location = models.ForeignKey (Location, verbose_name='Место проведения', on_delete=models.CASCADE)
    event_date = models.DateTimeField ('Дата проведения', )