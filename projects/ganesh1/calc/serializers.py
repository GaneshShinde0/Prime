from rest_framework import serializers 
from django.contrib.auth.models import User,Group
from calc.models import APIBASE

class CalcSerializer(serializers.Serializer):
    timeStamp=serializers.DateTimeField()
    ex_range=serializers.CharField(max_length=20,default='')
    #@property
    #p,q=map(int,str(ex_range).split())
    time_elapsed=serializers.DateTimeField()
    alg_chosen=serializers.CharField(max_length=30,default='')
    time_complexity=serializers.CharField(max_length=20)
    number_of_primes_returned=serializers.IntegerField()
    

    ''''
    def create(self,validated_data):
        return APIBASE.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.release_Date=validated_data.get
        '''