#######################

# web driver path, sql connection, messages and email functions!


# function for web driver path:
def wd_path():
    
    import os

    empty_path_list_wd = []
    path_dir = "C:\\Users\\Public\\driver" 
    ext_dir = "\\chromedriver.exe"

    for x, y, z in os.walk(path_dir):
        empty_path_list_wd.append(x)
        partial_path_wd = empty_path_list_wd[-1]
        full_path_wd = partial_path_wd + ext_dir
    wdpath = full_path_wd
    return(wdpath)

# function for sql connection:
def sql_conn(**data):
    
    import pyodbc
    
    driver = "{ODBC Driver 17 for SQL Server}"
    server_name = "xxx"
    
    sql_conn.db_name = list(data.values())[0]
    sql_conn.sql_tbl = list(data.values())[1]

    connection_string = """
    Driver={driver};
    Server={server};
    Database={database};
    Trusted_Connection=yes;
    """.format(
        driver=driver,
        server=server_name,
        database=sql_conn.db_name)
    
    sql_conn.conn = pyodbc.connect(connection_string)
    sql_conn.cur = sql_conn.conn.cursor()
    

# function for messages:
def msg(**t):
    
    from tkinter import messagebox
    import time
    
    msg.t = list(t.values())[0]
    msg.m = list(t.values())[1]
    
    msg_one = 'c' # created
    msg_two = 'o' # overwritten
    msg_three = 'm' # mapped
    
    if msg.m == msg_one:
            time.sleep(5)
            messagebox.showinfo('Device SQL', f'SQL table: {msg.t} has been successfully created!')
    elif msg.m == msg_two:
        
            time.sleep(5)
            messagebox.showinfo('Device SQL', f'SQL table: {msg.t} has been successfully overwritten!')
    elif msg.m == msg_three:

            time.sleep(5)
            messagebox.showinfo('Device SQL', f'SQL table: {msg.t} has been successfully mapped!')
    else:
        pass


# function for emails:
    
def email(**e):
    
    import datetime, win32com.client as win32
    
    fn = list(e.values())[0] # form name
    fl = list(e.values())[1] # form link
    db = list(e.values())[2] # database name
    tn = list(e.values())[3] # table name
    ms = list(e.values())[4] # message
    
    ms_one = 't' # table name
    ms_two = 'ot' # overwritten table name
    ms_three = 'm' # mapped table name
    
    now = datetime.datetime.now()
    date_time = (now.strftime("%d-%m-%Y, %H:%M:%S"))
    
    try:
        if ms == ms_one:
            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = "xxx"
            mail.Subject = "- Device SQL log information -"
            mail.HTMLBody = f'<h4 style = color:blue;> Form name: {fn}, Form URL: {fl} Database name: {db}, Table name: {tn}, Date and time: {date_time} </h4>'
            mail.Send()
        elif ms == ms_two:
            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = "yyy"
            mail.Subject = "- Device SQL log information -"
            mail.HTMLBody = f'<h4 style = color:blue;> Form name: {fn}, Form URL: {fl} Database name: {db}, Overwritten Table name: {tn}, Date and time: {date_time} </h4>'
            mail.Send()
        elif ms == ms_three:
            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = "zzz"
            mail.Subject = "- Device SQL log information -"
            mail.HTMLBody = f'<h4 style = color:blue;> Form name: {fn}, Form URL: {fl} Database name: {db}, Mapped Table name: {tn}, Date and time: {date_time} </h4>'
            mail.Send()
        else:
            pass
    except:
        pass