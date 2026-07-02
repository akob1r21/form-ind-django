class MyMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):
       print(request.META)
       ip = request.META.get('REMOTE_ADDR')
       print('salom', ip)
       response = self.get_response(request)
       print('after view')
       return response