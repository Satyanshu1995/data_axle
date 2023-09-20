from rest_framework import viewsets
from .models import Employee, Event, EmailTemplate, EmailLog
from .serializers import EmployeeSerializer, EventSerializer, EmailTemplateSerializer, EmailLogSerializer
from django.utils import timezone
from .logic_email import send_event_emails
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

admin_user = User.objects.get(username='admin')
token, created = Token.objects.get_or_create(user=admin_user)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.filter(event_date=timezone.now().date())
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    @action(detail=False, methods=['post'])
    def send_event_emails_action(self, request):
        try:
            # Call the send_event_emails function here
            send_event_emails()
            return Response({'message': 'Emails sent successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer