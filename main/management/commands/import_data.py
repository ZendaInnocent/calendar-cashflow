import csv
import datetime

from django.core.management.base import BaseCommand

from main.models import Transaction

filename = "D:\esktop\Projects\cash flow calendar\Transactions.csv"


class Command(BaseCommand):
    help = "Import data from csv file."

    def handle(self, *args, **kwargs):
        self.stdout.write("Importing data...")

        csvRows = []

        csvFileObj = open(filename)
        readerObj = csv.reader(csvFileObj)

        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)

        csvFileObj.close()

        for item in csvRows:
            theDate = item[0].split(' ')
            date = datetime.date(year=int(theDate[2]), month=int(
                theDate[1]), day=int(theDate[0]))
            theType = item[1]
            name = item[2]
            account = item[3]
            deposit = item[4].strip()
            withdrawal = item[5].strip()

            if deposit == "":
                status = 'W'
                if withdrawal == "":
                    amount = 0
                else:
                    amount = int(withdrawal)
            else:
                status = 'D'
                if deposit == '':
                    amount = 0
                else:
                    amount = int(deposit)

            trans = Transaction(
                name=name, amount=amount, payment_type=theType,
                account=account, status=status, date=date)
            trans.save()

        self.stdout.write(f"{Transaction.objects.count()} Data Processed")
