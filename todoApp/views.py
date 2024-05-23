from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    return redirect('/todos')
def health_check(request):
    """
    Health check endpoint to verify the application's status.
    """
    # Add any additional checks if needed
    # For example, check the database connection, cache availability, etc.

    # Return an HTTP response with a status code of 200 (OK)
    return HttpResponse("OK", status=200)
