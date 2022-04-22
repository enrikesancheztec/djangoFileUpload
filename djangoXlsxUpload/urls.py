from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path
import pandas as pd

@api_view(['POST'])
def xlsx_upload(request):
    df = pd.read_excel(request.FILES['file'])
    print (df)
    return Response({"data": df})

urlpatterns = [
    path('xlsx', xlsx_upload),
]
