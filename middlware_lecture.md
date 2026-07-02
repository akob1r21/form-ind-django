# Django Middleware -- Lecture Notes

## Goal

By the end of this lesson students should understand:

-   What middleware is
-   Why Django uses middleware
-   Request/Response lifecycle
-   Built-in middleware
-   Custom middleware
-   `get_response(request)`
-   `request.META`
-   `REMOTE_ADDR`
-   When middleware should and should not be used

------------------------------------------------------------------------

# 1. What is Middleware?

Middleware is a **layer that sits between the browser and your Django
views**.

Think of it as a **security checkpoint**.

Every request passes through middleware before reaching the view.

Every response passes through middleware before returning to the
browser.

   Browser
      |
      v
   Middleware
   Middleware
   Middleware
      |
      v
   View
      |
      ^
   Middleware
      |
      ^
   Browser

------------------------------------------------------------------------

# 2. Why does Django need Middleware?

Without middleware, every view would have to repeat code such as:

-   Logging
-   Authentication checks
-   IP logging
-   Security checks

Middleware allows us to write this logic **once** for the whole project.

------------------------------------------------------------------------

# 3. Request / Response Flow

Suppose a user visits:

   /products/

The flow is:

   Browser
       |
       v
   SecurityMiddleware
       |
   SessionMiddleware
       |
   AuthenticationMiddleware
       |
   MyMiddleware
       |
   View
       |
   MyMiddleware
       |
   AuthenticationMiddleware
       |
   SessionMiddleware
       |
   SecurityMiddleware
       |
   Browser

Notice:

-   Request goes **down**
-   Response comes **back up**

------------------------------------------------------------------------

# 4. Creating a Custom Middleware

``` python
class MyMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):
        
       response = self.get_response(request)

       return response
```

------------------------------------------------------------------------

# 5. Understanding Every Part

## `__init__(self, get_response)`

Runs **only once** when Django starts.

Django passes the next callable into your middleware.

``` python
self.get_response = get_response
```

stores it for later.

------------------------------------------------------------------------

## `__call__(self, request)`

Runs **for every request**.

Every page visit executes this method.

------------------------------------------------------------------------

## `self.get_response(request)`

This is the most important line.

It means:

> "Pass this request to the next middleware (or eventually the view)."

Example flow:

   Middleware A
         |
   Middleware B
         |
   View

Inside Middleware A:

``` python
response = self.get_response(request)
```

The request goes to Middleware B.

Middleware B calls its own `get_response()`.

Eventually the request reaches the view.

------------------------------------------------------------------------

# 6. What is `response`?

Suppose the view is:

``` python
from django.http import HttpResponse

def home(request):
   return HttpResponse("Hello")
```

The view returns:

   HttpResponse("Hello")

That object becomes:

``` python
response = self.get_response(request)
```

So `response` is usually an `HttpResponse` object.

------------------------------------------------------------------------

# 7. Why do we `return response`?

   Browser
       |
   Middleware
       |
   View

The view returns an HttpResponse.

Your middleware receives it.

If you do:

``` python
return response
```

the response continues back to Django and finally to the browser.

If you forget to return it, the browser receives nothing.

------------------------------------------------------------------------

# 8. Before and After the View

``` python
print("Before")

response = self.get_response(request)

print("After")

return response
```

Execution order:

   Before

   

   After

Everything before `get_response()` runs **before** the view.

Everything after it runs **after** the view.

------------------------------------------------------------------------

# 9. Stopping the Request

``` python
from django.http import HttpResponseForbidden

class BlockMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):

       return HttpResponseForbidden("Blocked")
```

Since `get_response()` is never called, the view never executes.

------------------------------------------------------------------------

# 10. Registering Middleware

In `settings.py`:

``` python
MIDDLEWARE = [
   ...
   "shop.middleware.MyMiddleware",
]
```

If you don't register it here, Django will never execute it.

------------------------------------------------------------------------

# 11. Built-in Middleware

## SecurityMiddleware

Provides security features:

-   HTTPS support
-   Secure cookies
-   HSTS

------------------------------------------------------------------------

## SessionMiddleware

Adds:

``` python
request.session
```

Without it, sessions don't work.

------------------------------------------------------------------------

## AuthenticationMiddleware

Adds:

``` python
request.user
```

Without it:

``` python
request.user
```

does not exist.

------------------------------------------------------------------------

## CsrfViewMiddleware

Protects POST requests from CSRF attacks.

Required for:

``` html
{% csrf_token %}
```

------------------------------------------------------------------------

## MessageMiddleware

Enables:

``` python
messages.success(request, "Saved")
```

------------------------------------------------------------------------

## CommonMiddleware

General HTTP improvements such as automatic slash redirects.

------------------------------------------------------------------------

## XFrameOptionsMiddleware

Protects against clickjacking attacks.

------------------------------------------------------------------------

# 12. request.META

`request.META` is a Python dictionary containing technical information
about the request.

Example:

``` python
print(request.META)
```

Possible keys:

-   REMOTE_ADDR
-   HTTP_USER_AGENT
-   HTTP_HOST
-   REQUEST_METHOD

------------------------------------------------------------------------

# 13. REMOTE_ADDR

Returns the IP address of the incoming connection.

``` python
ip = request.META.get("REMOTE_ADDR")
```

Example output:

   127.0.0.1

or

   192.168.1.20

In production behind a reverse proxy, it may be the proxy's IP instead
of the user's real IP.

------------------------------------------------------------------------

# 14. Print Visitor IP

``` python
class PrintIPMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):

       ip = request.META.get("REMOTE_ADDR")
       print(ip)

       return self.get_response(request)
```

Remember to add it to `MIDDLEWARE`.

------------------------------------------------------------------------

# 15. When to Use Middleware

Good use cases:

-   Logging requests
-   Logging IP addresses
-   Measuring request time
-   Blocking IPs
-   Maintenance mode
-   Adding headers

------------------------------------------------------------------------

# 16. When NOT to Use Middleware

Don't use middleware for:

-   Form validation
-   Saving models
-   Sending one email
-   Product calculations

Those belong in views, forms, models, or services.

------------------------------------------------------------------------

# Interview Questions

1.  What is middleware?
2.  Does middleware execute before or after the view?
3.  What does `get_response(request)` do?
4.  What is stored in `response`?
5.  Why must we return `response`?
6.  What is `request.META`?
7.  What is `REMOTE_ADDR`?
8.  Where do we register custom middleware?