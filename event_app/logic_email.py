import logging
from django.utils import timezone
from .models import Event, EmailTemplate, EmailLog

def send_event_emails():
    current_date = timezone.now().date()
    events = Event.objects.filter(event_date=current_date)

    for event in events:
        try:
            email_template = EmailTemplate.objects.get(event_type=event.event_type)
            # Populate the email template with event-specific content and member details
            email_content = email_template.body.format(employee_name=event.employee.name, event_type=event.event_type)
            # Send the personalized email to event.employee.email
            # Log successful delivery
            EmailLog.objects.create(
                employee=event.employee,
                event_type=event.event_type,
                sent_date=timezone.now(),
                status='SUCCESS'
            )
        except EmailTemplate.DoesNotExist:
            logging.error(f"Email template not found for event type: {event.event_type}")
        except Exception as e:
            logging.error(f"Error sending email for event: {event.event_type}. Error: {str(e)}")
            # Retry logic can be implemented here
