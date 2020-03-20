from django.views import View
from django.http import HttpResponse

from .tasks import sleeped, send_email_task


class MainView(View):

    def get(self, request):
        send_email_task.delay()
        return HttpResponse('<p>email send</p>')