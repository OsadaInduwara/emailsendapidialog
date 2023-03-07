from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    sender = serializers.EmailField()
    recipients = serializers.EmailField()
    cc_recipients = serializers.EmailField(required=False)
    subject = serializers.CharField()
    body = serializers.CharField()
