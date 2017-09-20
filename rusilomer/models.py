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
#         verbose_name = ('Новость')
#         verbose_name_plural = ('Новости')
#
#
#




# class Media(models.Model):
#     class Meta:
#         verbose_name = ('')
#         verbose_name_plural = ('')
#
#     pass
#
class Event(models.Model):
    class Meta:
        verbose_name = ('Мероприятие')
        verbose_name_plural = ('Мероприятия')

    location = models.ForeignKey (Location, verbose_name='Место проведения', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    text = models.TextField(max_length=200, verbose_name='Текст')
    event_date = models.DateField ('Дата проведения')
    publication_date = models.DateTimeField ('Дата публикации')

    def __str__(self):
        return 'гор.%s (%s)' %(self.location.city, self.event_date)