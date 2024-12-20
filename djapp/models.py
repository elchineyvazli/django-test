from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Member(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(18)
    ])


member = Member("Elchin", "Eyvazli", 17)
member.save()

print(Member.objects.all().values())
