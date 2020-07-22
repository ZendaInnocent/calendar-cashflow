from calendar import HTMLCalendar
from datetime import datetime as dtime
import datetime


class CashFlowCalendar(HTMLCalendar):

    def __init__(self, transactions=None):
        super(HTMLCalendar, self).__init__()
        self.transactions = transactions

    def formatday(self, day, weekday, transactions=None):
        """
        Return a day as a table cell.
        """
        # transactions_from_a_day = transactions.filter(day__day=day)
        transactions_html = "<div>"
        # for transaction in transactions_from_a_day:
        # for transaction in (1, 7):
        transactions_html += '<p class="title">\
            Funds Out: <span class="amount">54,0493</span></p>'
        transactions_html += '<p class="title">\
            Funds In: <span class="amount">430,090</span></p>'
        transactions_html += '<p class="title">\
            Ending: <span class="amount">430,090</span>'

        transactions_html += "</div>"

        if day == 0:
            return '<td class="noday">&nbsp</td>'  # day outside the month
        else:
            return f'<td class="date">{day}\
                {transactions_html}</td>'

    def formatweek(self, theweek, transactions=None):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, transactions) for (d, wd) in theweek)
        return f'<tr>{s}</tr>'
