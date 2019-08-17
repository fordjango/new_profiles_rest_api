from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API Views"""


    def get(self, request, fromat=None):
        """Returns a list of API View features"""
        an_apiview=['Uses HTTP methods as a function (get, post, patch, put, delete )' ,
        'Is similar to traditional Django view',
        'Gives you the most control over your application logic.'
        'Is mapped manually to URLs.',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
