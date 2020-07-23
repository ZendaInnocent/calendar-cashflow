import datetime
import calendar

from django.db.models import Sum
from django.shortcuts import render, reverse, redirect

from .utils import CashFlowCalendar
from .models import Transaction


def index(request):
    context = {

    }
    return render(request, 'main/index.html', context)


def month_detail_view(request, year, month):

    if request.method == "POST":
        q = Transaction.objects.values('date').annotate(total=Sum('amount'))
        start_day = request.POST['start-day'].upper()
        month = request.POST['month']
        year = request.POST['year']

        d = datetime.date(int(year), int(month), 1)
        cal = CashFlowCalendar(transactions=q, month=month, year=year)

        previous_month = datetime.date(year=d.year, month=d.month, day=1)
        previous_month = previous_month - datetime.timedelta(days=1)
        previous_month = datetime.date(
            year=previous_month.year, month=previous_month.month, day=1)

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
        next_month = next_month + datetime.timedelta(days=1)
        next_month = datetime.date(
            year=next_month.year, month=next_month.month, day=1)

        for i in range(0, 7):
            if calendar.day_name[i].upper() == start_day:
                day = i

        cal.setfirstweekday(day)

        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace(
            '<table ', '<table class="table table-bordered"')

        context = {
            'days_names': [day for day in calendar.day_name],
            'months_names': {i: calendar.month_name[i] for i in range(1, 13)},
            'years': [i for i in range(2019, 2022)],
            'previous_month': reverse(
                'main:month-detail', kwargs={
                    'year': previous_month.year, 'month': previous_month.month}
                    ),
            'current_month': reverse(
                'main:month-detail', kwargs={
                    'year': d.year, 'month': d.month}),
            'next_month': reverse(
                'main:month-detail', kwargs={
                    'year': next_month.year, 'month': next_month.month}),
            'selected_day': calendar.day_name[day].capitalize(),
            'month_name': calendar.month_name[d.month].capitalize(),
            'selected_month': d.month,
            'selected_year': d.year,
            'html_calendar': html_calendar
        }

        return redirect(reverse('main:month-detail', kwargs={
            'year': year, 'month': month}), context)

    elif request.method == 'GET':
        q = Transaction.objects.values('date').annotate(total=Sum('amount'))
        d = datetime.date(
            year=year, month=month, day=1)

        cal = CashFlowCalendar(transactions=q, year=year, month=month)
        day = 0

        previous_month = datetime.date(year=d.year, month=d.month, day=1)
        previous_month = previous_month - datetime.timedelta(days=1)
        previous_month = datetime.date(
            year=previous_month.year, month=previous_month.month, day=1)

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
        next_month = next_month + datetime.timedelta(days=1)
        next_month = datetime.date(
            year=next_month.year, month=next_month.month, day=1)

        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace(
            '<table ', '<table class="table table-bordered"')

        context = {
            'days_names': [day for day in calendar.day_name],
            'months_names': {i: calendar.month_name[i] for i in range(1, 13)},
            'years': [i for i in range(2019, 2022)],
            'previous_month': reverse(
                'main:month-detail', kwargs={
                    'year': previous_month.year, 'month': previous_month.month}
                    ),
            'current_month': reverse(
                'main:month-detail', kwargs={
                    'year': d.year, 'month': d.month}),
            'next_month': reverse(
                'main:month-detail', kwargs={
                    'year': next_month.year, 'month': next_month.month}),
            'selected_day': calendar.day_name[day].capitalize(),
            'month_name': calendar.month_name[d.month].capitalize(),
            'selected_month': d.month,
            'selected_year': d.year,
            'html_calendar': html_calendar
        }

    return render(request, 'main/month_detail.html', context)
