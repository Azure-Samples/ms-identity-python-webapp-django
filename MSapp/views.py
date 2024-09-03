from django.http import HttpResponse

def analytical_review_detail_raw(request, aid, *, context):
    return HttpResponse(f"analytical_review_detail_raw {aid} {context}")

