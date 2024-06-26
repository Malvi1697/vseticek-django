from django.db import models


class InsuranceSubject(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name")
    surname = models.CharField(max_length=64, verbose_name="Surname")
    email = models.EmailField(blank=True, verbose_name="Email")
    adress = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)

    class Meta:
        verbose_name = "Insurance Subject"
        verbose_name_plural = "Insurance Subjects"

    def __str__(self):
        return f'{self.id}: {self.name} {self.surname}'
