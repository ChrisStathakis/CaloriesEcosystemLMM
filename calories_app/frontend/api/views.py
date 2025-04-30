from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_homepage(request, format=None):
    return Response({
        "recipes": reverse('api_recipes:homepage', request=request, format=format),
        "profiles": reverse('api_profile:home', request=request, format=format)
    })
