from calendar import HTMLCalendar
from datetime import datetime as dtime
import datetime


class CashFlowCalendar(HTMLCalendar):

    def __init__(self, year, month, transactions=None):
        super(HTMLCalendar, self).__init__()
        self.transactions = transactions
        self.year = int(year)
        self.month = int(month)

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        starting_amount = 0
        funds_in = 0
        funds_out = 0
        ending_amount = 0

        if day != 0:
            q = self.transactions.filter(
                date=datetime.date(year=self.year, month=self.month, day=day))

            if day == 1:
                starting_amount = 0

            for item in q.values():
                if item['status'] == 'D':
                    funds_in = item['amount']
                    funds_out = 0
                    ending_amount = starting_amount + funds_in - funds_out
                elif item['status'] == 'W':
                    funds_in = 0
                    funds_out = item['amount']

        transactions_html = "<div>"
        transactions_html += '<p class="title">\
            Starting: <span class="amount"> ' + str(starting_amount) +'<span/></p>'
        transactions_html += '<p class="title">\
            Funds Out: <span class="amount">' + str(funds_out) + '</span></p>'
        transactions_html += '<p class="title">\
            Funds In: <span class="amount">' + str(funds_in) + '</span></p>'
        transactions_html += '<p class="title">\
            Ending: <span class="amount">' + str(ending_amount) + '</span></p>'

        transactions_html += "</div>"

        if day == 0:     # day outside the month
            return '<td class="noday">&nbsp</td>'
        else:
            return f'<td><b>{day}</b>\
                {transactions_html}</td>'

    # def formatweek(self, theweek, transactions=None):
    #     """
    #     Return a complete week as a table row.
    #     """
    #     s = ''.join(self.formatday(d, wd, transactions) for (d, wd) in theweek)
    #     return f'<tr>{s}</tr>'
