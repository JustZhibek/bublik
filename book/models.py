from django.db import models

class Lost(models.Model):

    TYPES = (
        ('Fantasy', 'Фэнтези'),
        ('Romance novel', 'Любовный роман'),
        ('Short stories', 'Короткие истории'),
        ('Western', 'Вэстерн')
)
    title = models.CharField('Название книги', max_length=190)
    description = models.TextField('Описание книги')
    types = models.CharField(max_length=100, choices=TYPES)
    image = models.ImageField(upload_to='')
    price = models.PositiveIntegerField('цена', null=True)


    def __str__(self):
        return self.title

class RatingLost(models.Model):
    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    choice_book = models.ForeignKey(Lost, on_delete=models.CASCADE, related_name='comment_object')
    rate = models.IntegerField('Оценка: ', choices=RATING)
    comment = models.TextField('Комментарий: ')
    created_date = models.DateTimeField(auto_now_add=True)
