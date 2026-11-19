import json
import hmac
import hashlib
from django.shortcuts import render
from django.http import HttpResponseForbidden,HttpResponse,JsonResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

 

@csrf_exempt
def VerificarFirma (request):
    secret = 'i4]|uw<]#:f:+ubzl9nG6-q,ql{UKI=R'
    signature_header = request.META.get("HTTP_X_GITHUB_EVENT","ping")

    if not signature_header.startswith("sha256="):
        return False

    sha_name, signature = signature_header.split("=")
    mac = hmac.new(secret, msg=request.body, digestmod=hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(),signature)

# Create your views here.