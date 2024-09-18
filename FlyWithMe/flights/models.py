from django.db import models


class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    dep_airport = models.CharField(max_length=100)
    dep_date = models.DateField()
    dep_time = models.TimeField()
    arr_airport = models.CharField(max_length=100)
    arr_date = models.DateField()
    arr_time = models.TimeField()

    def __str__(self):
        return f'{self.flight_id} from {self.dep_airport} to {self.arr_airport}'
