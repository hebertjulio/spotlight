import re


def get_current_news(request):
    http_refer = request.META['HTTP_REFERER']
    regex = r'news\/(\d)\/change'
    matches = re.search(regex, http_refer, re.DOTALL)
    return matches.group(1) if matches else None
