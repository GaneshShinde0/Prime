from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime
# Create your views here.
#create function home here after adding path('',views.home,name='home')#homepage 
from .models import APIBASE

def home(request):
    return render(request, 'home.html',{'name':'Ganesh'})# You can use html files or add html tags as well
    #http response text
def primes(request):
    #Simple
    timestamp=datetime.datetime.now()
    start_time=time.time()
    p=int(request.POST['num1'])
    q=int(request.POST['num2'])
    meth=request.POST['meth']
    
    def simple(p,q):
        z=[]
        for i in range(p,q+1):
            if i>1:
                for j in range(2,i):
                    if i%j==0:
                        break
                else:
                    z.append(str(i))
        return z
    #Easier
    def prime(p,q):
        z=[]
        for i in range(p,q+1):
            if i>1:
                for j in range(2,int(i**0.5)+1):
                    if i%j==0:
                        break
                else:
                    z.append(str(i))
        return z
    #Sieve of Eratosthenes
    #Time Complexity O(N log (log N))

    #profiler = cProfile.Profile()
    #profiler.enable()
    #p,q=map(int, input().strip().split())

    def eras(p,q):
        #z=[]
        prime = [True for i in range(q+1)]
        l = 2
        while (l * l <= q):
            # If prime[p] is not
            # changed, then it is a prime
            if (prime[l] == True):
                # Update all multiples of l
                for i in range(l * l, q+1, l):
                    prime[i] = False
            l += 1
        # Print all prime numbers
        z=[]
        for l in range(p,q+1):
            if prime[l]:
                z.append(str(l))
        return z
    if meth=='Optimized':
        alg='Optimized'
        result=prime(p,q)
        time_complexity='O(N*LOG(N))'

    if meth=='Simple':
        alg='Simple'
        result=simple(p,q)
        time_complexity='O(N*N)'

    if meth=='Sieve Of Eratosthenes':
        alg='Sieve Of Eratosthenes'
        time_complexity='O(N*LOG(LOG(N)))'
        result=eras(p,q)

    te=time.time()-start_time
    print(te)
    np=len(result)
    b=APIBASE(timeStamp=timestamp,ex_range=str(p)+' '+str(q),alg_chosen=alg,time_complexity=time_complexity,time_elapsed=te,number_of_primes_returned=np)
    b.save()
    return render(request,"result.html",{'time_stamp':timestamp,'count':np,'alg':alg,'time_complexity':time_complexity,'result':' '.join(result),'range':str(p)+' '+str(q),'time_elapsed':te})

#Code FOr Converting Request To API

'''
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .models import APIBASE
from .serializers import CalcSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def calc_list(request):

    if request.method=='POST':
        apibase=APIBASE.objects.all()
        serializer=CalcSerializer(apibase,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='GET':
        data=JSONParser().parse(request)
        calc_serializer=CalcSerializer(data=data)

        if calc_serializer.is_valid():
            calc_serializer.save()
            return JsonResponse(calc_serializer.data,status=201)
        return JSONResponse(calc_serializer.errors,status=400) 

@csrf_exempt
def calc_detail(request,pk):
    try:
        calc=APIBASE.objects.get(pk=pk)
    except APIBASE.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET':
        calc_serializer=CalcSerializer(calc)
        return JSONResponse(calc_serializer.data)
    elif request.method=='PUT':
        calc_data=JSONParser().parse(request)
        calc_serializer=CalcSerializer(calc,data=calc_data)
        if calc_serializer.is_valid():
            calc_serializer.save()
            return JSONResponse(calc_serializer.data)
        return JSONResponse(calc_serializer.errors,status=400)
    elif request.method=='DELETE':
        calc.delete()
        return HttpResponse(status=204)
'''
from rest_framework import viewsets

from .serializers import CalcSerializer


class APIBASEViewSet(viewsets.ModelViewSet):
    queryset = APIBASE.objects.all().order_by('timeStamp')
    serializer_class = CalcSerializer
