from decimal import Decimal


def do(tr, params):
    tr.data = params
    tr.data['description'] = 'Резервирование суммы на отправку SMS'
    balance = tr.accountBalance('business', [
        {'business': params['business']}])
    if balance - Decimal(params['amount']) < 0:
        tr.cancel()
        res = 'Недостаточно суммы на ЛС'
        return(res)

    tr.entry('business', -params['amount'], {
        'business': params['business']})

    res = tr.save()
    return(res)

