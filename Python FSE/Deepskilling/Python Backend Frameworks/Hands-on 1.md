## Hands-on 1

##  Task 1: Understand the Request-Response Cycle

# -------------------------------------------------------------------
# 1. Request–Response Cycle in Django
# -------------------------------------------------------------------

"""
When a user sends a GET request to /api/courses/, Django processes it as follows:

1. The browser sends an HTTP request.
2. Django receives the request.
3. The URL Dispatcher (urls.py) matches the requested URL.
4. The matched URL calls the appropriate View.
5. The View interacts with the Model to retrieve data from the database.
6. The Model executes the database query and returns the results.
7. The View processes the data.
8. The View returns an HttpResponse (or renders a Template).
9. Django sends the response back to the browser.
"""

# -------------------------------------------------------------------
# 2. Middleware
# -------------------------------------------------------------------

"""
Middleware sits between the incoming request and the view, and also
between the view and the outgoing response.

It processes requests before they reach the view and responses before
they are sent back to the client.

Examples of built-in middleware:

1. SecurityMiddleware
   - Adds security features such as HTTPS redirects and security headers.

2. SessionMiddleware
   - Enables session management so user-specific data can be stored
     across multiple requests.
"""

# -------------------------------------------------------------------
# 3. WSGI vs ASGI
# -------------------------------------------------------------------

"""
WSGI (Web Server Gateway Interface)

- Supports synchronous request handling.
- Suitable for traditional web applications.
- Django uses WSGI by default.
- Best for applications that do not require real-time communication.

ASGI (Asynchronous Server Gateway Interface)

- Supports asynchronous request handling.
- Handles WebSockets, long-lived connections, and real-time applications.
- Used when building chat applications, live notifications, or other
  asynchronous services.
"""

# -------------------------------------------------------------------
# 4. MVC vs Django MVT
# -------------------------------------------------------------------

"""
MVC Architecture

Model      -> Handles database operations.
View       -> Handles the user interface.
Controller -> Handles business logic and user requests.

Django MVT Architecture

Model      -> Database layer (same as MVC Model).
View       -> Contains business logic (acts like the Controller in MVC).
Template   -> Presentation layer (acts like the View in MVC).

MVC Mapping to Django:

MVC Model       = Django Model
MVC View        = Django Template
MVC Controller  = Django View
"""


## Task 2: Scaffold and Explore the Django Project

"""
## settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
]

"""

### views.py

"""
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Course Management API is running")

"""

## Courses/urls.py

"""

from django.urls import path
from .views import hello_view

urlpatterns = [
    path("hello/", hello_view),
]

"""

## Courses/urls.py

"""

from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("courses.urls")),
]

"""

## OUTPUT

http://127.0.0.1:8000/api/hello/

<img width="1911" height="1070" alt="image" src="https://github.com/user-attachments/assets/27479a02-692b-4aed-8887-9584e6a2322a" />
