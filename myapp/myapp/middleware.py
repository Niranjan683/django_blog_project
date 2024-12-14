from django.urls import reverse
from django.shortcuts import redirect
class RedirectAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        # checking the user is authenticated
        if request.user.is_authenticated:
            #List of path to check that the user is on the listed path
            paths_to_redirect = [reverse('blog:login'),reverse('blog:register')]

            if request.path in paths_to_redirect:
                return redirect(reverse('blog:index')) # redirecting to INDEX page
    
        response = self.get_response(request)
        return response
    
class RestrictUnauthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [reverse('blog:dashboard')]

        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect(reverse('blog:login'))
        
        response = self.get_response(request)
        return response