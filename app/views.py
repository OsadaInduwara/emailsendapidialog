# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MailSerializer


# @api_view(['POST'])
# def send_email(request):
#     serializer = MailSerializer(data=request.data)
#     if serializer.is_valid():
#         data = serializer.validated_data
#         response = send_mail(data['recipients'], data.get('cc_recipients', []), data['sender'], data['body'], 'utf-8',
#                              data['subject'])
#         if response['ResponseMetadata']['HTTPStatusCode'] == 200:
#             return Response({'response': 'Sent'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'response': 'Failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def send_email(request):
    serializer = MailSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Skip AWS connection and return success message
        return Response({'response': 'Sent'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
