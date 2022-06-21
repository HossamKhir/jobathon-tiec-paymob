from rest_framework import viewsets
from rest_framework import permissions

from task2.models import Person
from task2.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """

    # add code here
    queryset = Person.objects.all().order_by("-created_date").reverse()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
