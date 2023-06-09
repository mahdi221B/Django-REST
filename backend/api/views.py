from django.shortcuts import render
from django.http import JsonResponse
import json



def api_home(request, *args, **kwargs):
    #print(dir(request))
    body = request.body #Byte string of JSON DATA    
    print(request.GET)    
    print(request.content_type)    
    print(request.headers)    
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    #return JsonResponse({"message":"Hey there :)"})
    return JsonResponse(data)