from django.db import models

class TVShow(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('MELODRAMME', 'MELLODRAMME')
    )



    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество фильмов')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена билета', null=True)
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title