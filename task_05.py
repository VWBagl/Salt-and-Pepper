from datetime import datetime, timedelta

def date_in_future(integer):
    if type(integer) is not int:
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    result_date = datetime.now() + timedelta(days=integer)
    
    return result_date.strftime('%d-%m-%Y %H:%M:%S')