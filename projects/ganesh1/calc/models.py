from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
# Create your models here.

class APIBASE(models.Model):
    #Things I need Are 
    #Execution in database
    #TimeStamp
    #range
    #time Elapsed
    #Algorithm Chosen
    #Number Of Primes Returned
    timeStamp=models.DateTimeField(auto_now_add=True)
    ex_range=models.CharField(max_length=20,default='')
    #@property
    #p,q=map(int,str(ex_range).split())
    alg_chosen=models.CharField(max_length=30,blank=True,default='')
    time_complexity=models.CharField(max_length=20)
    time_elapsed=models.DateTimeField()
    number_of_primes_returned=models.IntegerField()
    class Meta:
        ordering=('timeStamp',)
        