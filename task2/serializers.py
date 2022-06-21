from rest_framework import serializers

from task2.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    # add code here
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email", "created_date"]
