from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer


#create short url 
class ShortenURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get url
class RetrieveURL(APIView):
    def get(self, request, code):
        try:
            short_url = ShortURL.objects.get(short_code=code)
            short_url.access_count += 1
            short_url.save()
            serializer = ShortURLSerializer(short_url)
            return Response(serializer.data)
        except ShortURL.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


#update url
class UpdateURL(APIView):
    def put(self, request, code):
        try:
            short_url = ShortURL.objects.get(short_code=code)
            serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ShortURL.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


#delete url
class DeleteURL(APIView):
    def delete(self, request, code):
        try:
            short_url = ShortURL.objects.get(short_code=code)
            short_url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShortURL.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        