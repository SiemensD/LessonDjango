from statistics import mode
from tabnanny import verbose
from tokenize import group
from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(verbose_name='Имя',
                            max_length=100)

    def __str__(self) -> str:
        return self.name

    def seve(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class StudentGroup(models.Model):
    name = models.CharField(verbose_name='Имя',
                             max_length=50)
    students_number = models.IntegerField(verbose_name='Количество студентов',
                                          blank=True,                                          
                                          null=True)

    subject = models.ForeignKey(Subject,
                                verbose_name='Предмет',
                                on_delete=models.SET_NULL,
                                blank=True,
                                related_name='students',
                                null=True)                                      

    def __str__(self) -> str:
        return self.name

    def seve(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'


class Student(models.Model):
    name = models.CharField(verbose_name='Имя', 
                            max_length=50,
                            blank=True,
                             null=True)
    surname = models.CharField(verbose_name='Фамилия',
                               max_length=50,
                               blank=True,
                               null=True)
    birthday = models.DateField(verbose_name='День рождения',
                                blank=True,
                                null=True)
    group = models.ForeignKey(StudentGroup,
                                verbose_name='Группа',
                                on_delete=models.SET_NULL,
                                blank=True,
                                related_name='students',
                                null=True)

    def __str__(self) -> str:
        return self.name

    def seve(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
