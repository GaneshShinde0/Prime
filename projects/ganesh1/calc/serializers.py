from rest_framework import serializers 
class PrimeSerializer(serializers.Serializer):
    timeStamp=serializers.DateTimeField(auto_now_add=True)
    ex_range=serializers.CharField(max_length=20,default='')
    #@property
    #p,q=map(int,str(ex_range).split())
    time_elapsed=serializers.DateTimeField()
    alg_chosen=serializers.CharField(max_length=30,blank=True,default='')
    number_of_primes_returned=serializers.IntegerField()