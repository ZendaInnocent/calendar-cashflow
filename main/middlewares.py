import datetime

today = datetime.datetime.now()


def current_year_and_month_middleware(get_response):
    def middleware(request):
        request.month = today.month
        request.year = today.year
        response = get_response(request)
        return response
    return middleware
