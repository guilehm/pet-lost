import os
import uuid
from functools import wraps

import requests
from django.contrib import messages
from django.utils.deconstruct import deconstructible

from petLost.settings import GOOGLE_RECAPTCHA_SECRET_KEY


def check_recaptcha(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
                messages.add_message(request, messages.ERROR, 'reCAPTCHA inválido. Por favor tente novamente.')
        return view_func(request, *args, **kwargs)

    return _wrapped_view


@deconstructible
class UploadToFactory:

    def __init__(self, prefix=None):
        self.prefix = prefix

    def __call__(self, instance, filename):
        instance.original_file_name = filename
        filename, extension = os.path.splitext(filename)
        path = [str(uuid.uuid4())]
        if self.prefix:
            path.insert(0, self.prefix)
        return os.path.join(*path) + extension.lower()
