from django.shortcuts import redirect
from django.contrib.auth.forms import authenticate
from django.contrib.auth.models import User


def auth_middleware(get_response):
   

    def middleware(request):
        returnUrl=request.META['PATH_INFO']
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')
     

        response = get_response(request)

        

        return response

    return middleware