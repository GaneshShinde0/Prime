from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime
# Create your views here.
#create function home here after adding path('',views.home,name='home')#homepage 

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

    return render(request,"result.html",{'time_stamp':timestamp,'count':len(result),'alg':alg,'time_complexity':time_complexity,'result':' '.join(result),'range':str(p)+' '+str(q),'time_elapsed':time.time()-start_time})

#Code FOr Converting Request To API

'''
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
def article_list(request):

    if request.method=='POST':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='GET':
        data=JSONParser().parse(request)
        serializer=ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
            '''