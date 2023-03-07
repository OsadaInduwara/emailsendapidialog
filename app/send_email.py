import logging

import boto3


def send_mail(to_mail_list, cc_mail_list, source_mail, html_email_content, charset, mail_subject):
    logging.info("Mail TO Addresses: " + ','.join(to_mail_list))
    logging.info("Mail CC Addresses: " + ','.join(cc_mail_list))
    logging.info("Mail SOURCE Address: " + source_mail)
    logging.info("Mail Subject: " + mail_subject)
    ses_client = boto3.client('ses', region_name='us-west-2')
    response = ses_client.send_email(
        Destination={
            'ToAddresses': ['dumindu.ranasinghearachchi@dialog.lk'],
            'CcAddresses': ['dumindu.ranasinghearachchi@dialog.lk'],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': '<html><body><h1>Hello, World!</h1></body></html>',
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'Hello, World!',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Test email',
            },
        },
        Source='noreply@example.com',
    )

    return response
