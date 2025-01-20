from rest_framework.exceptions import ValidationError

from events.messages import CommonMessages
from events.models import Event, Ticket


class PurchaseTicketService:
    """This service is implemented for the update the data of purchase ticket and sold ticket"""

    def execute(self, request, id):
        event = Event.objects.get(id=id)
        if not event:
            raise ValidationError({"message":CommonMessages.EVENT_NOT_FOUND})

        quantity = request.data.get('quantity')
        if event.tickets_sold + quantity > event.total_tickets:
            raise ValidationError({"message": CommonMessages.TICKET_NOT_AVAILABLE.format(quantity=quantity)})

        Ticket.objects.create(user=request.user, event=event, quantity=quantity)
        event.tickets_sold += quantity
        event.save()
        return quantity
