from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name

class Position(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="positions")
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]