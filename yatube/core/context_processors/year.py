import datetime


def year(request):
    dat = {}
    dat_year = datetime.datetime.today().year
    return {'year': dat_year}
