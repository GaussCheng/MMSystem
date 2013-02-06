from django.shortcuts import render_to_response

def index(request, queryset):
    maintain_logs = queryset
    return render_to_response('maintain_log/index.html',
                              {'maintain_logs': maintain_logs})
