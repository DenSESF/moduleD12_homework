import logging

from django.http import HttpResponse, HttpResponseBadRequest


def get_error(request):
    if request.GET:
        try:
            x = 10/int(request.GET.get('cat'))
            return HttpResponse(f'<h1>Ответ: {x}</h1>')
        except ZeroDivisionError as e:
            log_request = logging.getLogger('django.request')
            log_request.error(e)
            return HttpResponseBadRequest(f'<h1>{e}</h1>')
    return HttpResponse('<h1><a href="/?cat=0">Неверный запрос</a></h1>')
