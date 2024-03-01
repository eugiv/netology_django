from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=10)
    descr = models.CharField(max_length=100)

    def __str__(self):
        return self.descr


class Measurement(models.Model):
    sens_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.sens_id
