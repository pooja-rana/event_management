from django.db import models


class Event(models.Model):
    """ This is event model that contain details model"""
    name = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField()
    total_tickets = models.IntegerField(null=True, blank=True)
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    """ This is ticket model and also contain relation model user and event """
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)