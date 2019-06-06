from decimal import Decimal


def do(tr, params):
    tr.data = params
    tr.data['description'] = 'Резервирование суммы на отправку SMS'
    balance = tr.accountBalance('business', [
        {'business': params['business']}])
    if balance - Decimal(params['amount']) < 0:
        tr.cancel()
        res = {'message': 'Недостаточно суммы на ЛС'}
        return(res)
    tr.postTransaction()
    tr.postEntry(account='business', amount=-params['amount'],
                 analytics={'business': params['business']},
                 data={'description': 'Зарезервирована сумма на отправку SMS'}
                 )

    res = tr.save()
    return(res)
