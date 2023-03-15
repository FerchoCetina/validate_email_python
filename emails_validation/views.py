import json

from django.http import HttpResponse
from validate_email import validate_email

from emails_validation.models import EmailVal


def valite_email_view(request):
    is_valid = False
    if request.method == 'GET':
        data = request.GET
        email = data.get('email')
        if EmailVal.objects.filter(email=email):
            is_valid = True
        else:
            try:
                is_valid = validate_email(
                    email_address=email,
                    check_format=True,
                    check_dns=True,
                    dns_timeout=10,
                    # check_smtp=True,
                    smtp_timeout=10,
                    smtp_skip_tls=False,
                    smtp_tls_context=None,
                    smtp_debug=False,
                   )
                if is_valid:
                    new_email = EmailVal(email=email).save()
            except:
                is_valid = False

    result = {
        'is_valid': is_valid
    }
    result = json.dumps(result)

    return HttpResponse(result, content_type="application/json")