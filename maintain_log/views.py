from django.shortcuts import render_to_response
from maintain_log.models import MaintainLog

def index(request):
    maintain_logs = MaintainLog.objects.all().order_by('-carry_date')
    bugs = maintain_logs[0].maintainbug_set.all()
    return render_to_response('maintain_log/index.html',
                              {'maintain_logs': maintain_logs,
                               'bugs': bugs})
