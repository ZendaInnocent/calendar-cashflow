import datetime
import calendar

from django.db.models import Sum
from django.shortcuts import render, reverse, redirect
from django.views import generic

from .utils import CashFlowCalendar
from .models import Transaction
from .forms import TransactionForm


def index(request):
    context = {

    }
    return render(request, 'main/index.html', context)


def month_detail_view(request, year, month):
    q = Transaction.objects.values('date')
    context = {}

    if request.method == 'POST':
        # start_day = request.POST['start-day'].upper()
        month = request.POST['month']
        year = request.POST['year']
        # for i in range(0, 7):
        #     if calendar.day_name[i].upper() == start_day:
        #         day = i
        return redirect(reverse('main:month-detail', kwargs={
            'year': year, 'month': month}), context)

    day = 0
    selected_day = calendar.day_name[day].capitalize()

    d = datetime.date(int(year), int(month), 1)
    cal = CashFlowCalendar(transactions=q, year=year, month=month)
    cal.setfirstweekday(day)

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
        'month_name': calendar.month_name[d.month].capitalize(),
        'selected_day': selected_day,
        'selected_month': d.month,
        'selected_year': d.year,
        'days_names': [day for day in calendar.day_name],
        'months_names': {i: calendar.month_name[i] for i in range(1, 13)},
        'years': [i for i in range(2019, 2022)],
        'html_calendar': html_calendar,
        'previous_month': reverse('main:month-detail', kwargs={
                            'year': previous_month.year,
                            'month': previous_month.month}),
        'current_month': reverse('main:month-detail', kwargs={
                            'year': d.year, 'month': d.month}),
        'next_month': reverse('main:month-detail', kwargs={
                            'year': next_month.year,
                            'month': next_month.month}),

    }

    return render(request, 'main/month_detail.html', context)


def transactions_view(request):
    return render(request, 'main/transactions.html', {
        'transactions': Transaction.objects.all().order_by('date'),
    })


def month_transactions_view(request, year, month):
    return render(request, 'main/transactions.html', {
        'transactions': Transaction.objects.filter(
            date__month=month, date__year=year),
    })


class TransactionAddView(generic.CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = 'main:index'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Add'
        context['button'] = 'Add'
        return context


class TransactionUpdateView(generic.UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = 'main:index'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Update'
        context['button'] = 'Save'
        return context
