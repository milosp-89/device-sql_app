# main application page:

# modules and librarie:
from tkinter import *

# imported custom based functions from ds_01.py:
from ds_01 import msg
from ds_01 import email
from ds_01 import wd_path

import tkinter.ttk as ttk
from ds_01 import sql_conn
from tkinter import messagebox
from selenium import webdriver
from flatten_json import flatten
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, validators, re, os, os.path, warnings, datetime, time, sys, pandas as pd

# opening log file:
now = datetime.datetime.now()
final_date_time = (now.strftime("%d-%m-%Y, %H:%M:%S"))

f = open("device_sql_app_log_file.txt", "a")

f.write("-------------------- Log date: ")
f.write(final_date_time)
f.write("\n")
f.write("\n")

f.close()

# removing messages:
sys.stderr = sys.stdout

# function for navigating to next page or create sql table:
def page_one():
    window_main.withdraw()
    first_page()
    
# function for navigating to page two or map sql table:
def page_two():
    window_main.withdraw()
    second_page()
    
###########################
# main window:
window_main = Tk()
window_main.title('Device SQL')

p1 = PhotoImage(file = "ds.png")
window_main.iconphoto(False, p1)

# center window:
w = 700
h = 678
 
screen_width = window_main.winfo_screenwidth()
screen_height = window_main.winfo_screenheight()
 
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
 
window_main.geometry('%dx%d+%d+%d' % (w, h, x, y))

# main canvas:
window_main.configure(bg = "#ffffff")
canvas = Canvas(
    window_main,
    bg = "#ffffff",
    height = 678,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_main.png")
background = canvas.create_image(
    350.0, 339.0,
    image=background_img)

# button for page two or map sql table:
img0 = PhotoImage(file = f"btn1_main.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = page_two,
    cursor = 'hand2',
    relief = "flat")

b0.place(
    x = 350, y = 487,
    width = 350,
    height = 191)

# button for page one or create sql table:
img1 = PhotoImage(file = f"btn2_main.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = page_one,
    cursor = 'hand2',
    relief = "flat")

b1.place(
    x = 0, y = 487,
    width = 363,
    height = 191)

###########################
# window one or function for create sql table:
def first_page():
    
    def submit_all():
        
        formu = furl.get()
        fn = fname.get()
        at = token.get()
        dbn = dbname.get()
        tbln = tname.get()
        defaults = default.get()
    
        l1 = list(formu)
        l2 = list(fn)
        l3 = list(at)
        l4 = list(dbn)
        l5 = list(tbln)
        l6 = list(defaults)
        
        list1 = ''.join(l1)
        list2 = ''.join(l2)
        list3 = ''.join(l3)
        list4 = ''.join(l4)
        list5 = ''.join(l5)
        list6 = ''.join(l6)
        
        user_name = os.getlogin()
        
        # main variables used for the main script:
        submit_all.user_name = user_name
        submit_all.form_url = list1
        submit_all.form_name = list2
        submit_all.api_token = list3
        submit_all.database_name = list4
        submit_all.table_name = list5
        submit_all.default_selection = list6
        
        return[submit_all.user_name, # 0
               submit_all.form_url, # 1
               submit_all.form_url, # 2
               submit_all.form_name, # 3
               submit_all.api_token, # 4
               submit_all.database_name, # 5
               submit_all.table_name, # 6
               submit_all.default_selection] #7

# function to delete a file:
    def delete_file():
        user_name = submit_all.user_name
        form_name = submit_all.form_name
        delete_file.file_location = f"C:\\Users\\{user_name}\\Downloads\\{form_name}.csv"
        try:
            os.remove(delete_file.file_location)
        except:
            pass

# function to check url:
    def check_url():
        submit_all()
        url_string = submit_all.form_url
        text = re.compile(r".*[0-9]$")
        valid = validators.url(url_string)
        if valid == True and url_string.startswith('url/') and text.match(url_string) and "web_stores" in url_string:
            entry5.configure(foreground="black")
            check_url.url = 0
            return(check_url.url)
        else:
            entry5.configure(foreground="red")
            check_url.error = messagebox.showerror('ERROR', 'Invalid Form URL!')
            check_url.error
            check_url.url = 1
            return(check_url.url)
            exit()
    
    # function to check form name:
    def check_form_name():
        
        submit_all()
        fname_string = submit_all.form_name
        if re.search('[a-zA-Z]', fname_string):
            entry4.configure(foreground="black")
            check_form_name.form = 0
            return(check_form_name.form)
        else:
            entry4.configure(foreground="red")
            check_form_name_error = messagebox.showerror('ERROR',
                                                         'Invalid Form name!')
            check_form_name_error
            check_form_name.form = 1
            return(check_form_name.form)
            exit()
            
    # function to check api token:
    def check_api_token():
        
        submit_all()
        
        api_string = submit_all.api_token
        if api_string.startswith('Basic ') and api_string.endswith('=='):
            entry3.configure(foreground="black")
            check_api_token.api = 0
            return(check_api_token.api)
        else:
            entry3.configure(foreground="red")
            check_api_token.api_error = messagebox.showerror('ERROR', 'Invalid API token!')
            check_api_token.api_error
            check_api_token.api = 1
            return(check_api_token.api)
            exit()
            
    # function to check database name:
    def check_db():
    
        sql_conn(db = 'master',
                 tbl = '')
        
        submit_all()
        db_name_string = submit_all.database_name
        get_dbs = 'EXEC sp_databases'
        sql_conn.cur.execute(get_dbs)
        df_db = pd.DataFrame(sql_conn.cur.fetchall())
        df_db.rename(columns={0:'databases'},
                      inplace=True)
        df_db['databases'] = df_db['databases'].str[0]
        sql_db_list = df_db['databases'].tolist()
        sql_db_list = [e for e in sql_db_list if e not in ('master', 'model', 'msdb', 'tempdb')]
        
        if db_name_string in sql_db_list:
            entry2.configure(foreground="black")
            check_db.db = 0
            return(check_db.db)
        else:
            entry2.configure(foreground="red")
            check_db.db_error = messagebox.showerror('ERROR', f'Invalid Database, Database: {db_name_string} does NOT exist within a server!')
            check_db.db_error
            check_db.db = 1
            return(check_db.db)
            exit()
        sql_conn.conn.close()
            
    # function to check sql table:
    def check_sql_tbl_name():
        
        submit_all()
        tbl_string = submit_all.table_name
    
        if ' ' not in tbl_string:
            entry1.configure(foreground="black")
            check_sql_tbl_name.tbl = 0
            return(check_sql_tbl_name.tbl)
        
        else:
            entry1.configure(foreground="red")
            check_sql_tbl_name_error = messagebox.showerror('ERROR',
                                                            'Invalid Table name!')
            check_sql_tbl_name_error
            check_sql_tbl_name.tbl = 1
            return(check_sql_tbl_name.tbl)
            
            exit()
            
    # function to check if there are submissions within a form:
    def check_submissions():
        submit_all()
        formname = submit_all.form_name
        main_url = submit_all.form_url
        api_token = submit_all.api_token
        form_number = main_url.rpartition('/')[-1]
        url = f"url/{form_number}/url2/"
        
        headers = {'Authorization': api_token}
        response = requests.get(url + '?page = 1', headers=headers)
    
        data = response.json()
        check_submissions.final_data = flatten(data)
        nmb_of_subs = check_submissions.final_data['total_count']
        
        if nmb_of_subs == 0:
            check_submissions_error = messagebox.showerror('ERROR', f'Device Magic form: {formname} has no submissions!')
            check_submissions_error
            exit()
        else:
            pass
        
    # function for setting up download file and path:
    def file_and_path():
        
        submit_all()
        user_name = submit_all.user_name
        urlx = submit_all.form_url
        
        # form name part:
        form_name = submit_all.form_name
        urly = "url"
        file_and_path.full_url = urlx + urly
        final_user = f"C:\\Users\\{user_name}\\Downloads\\"
        try:
            pathd = final_user
            pathdd = f'{form_name}.csv'
            full_pathd = pathd + pathdd
            os.remove(full_pathd)
        except:
            pass
        path0 = final_user
        path1 = f'{form_name}.csv'
        file_and_path.full_path = path0 + path1
        return(file_and_path.full_path)
    
    # function fow download a dm form in df mode:
    def dm_download():
        
        submit_all()
        file_and_path()
        
        username = submit_all.user_name
        url_fixed = file_and_path.full_url
        final_wd_path = wd_path()
        wdpath = Service(final_wd_path)
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory" : f"C:\\Users\\{username}\\Downloads\\", # path to the download file
            "download.prompt_for_download" : False,})

        wdpath.creationflags = CREATE_NO_WINDOW
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=wdpath, options=options)
            
        # path to the download file:
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd' : 'Page.setDownloadBehavior', 'params' : 
                     {'behavior': 'allow', 'downloadPath' : f"C:\\Users\\{username}\\Downloads\\"}}
    
        driver.execute("send_command", params)
        driver.get(url_fixed)
    
        driver.implicitly_wait(5)
    
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.ID, "user_remember_me_1")))
    
        driver.find_element(By.ID, 'user_remember_me_1').click()
        mail = 'xxx'
        mail_enter = driver.find_element(By.ID, 'user_email')
        mail_enter.send_keys(mail)

        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.NAME, "commit"))).click()
    
        driver.implicitly_wait(5)
    
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.ID, "user_password")))
    
        pswd = 'yyy'
        pswd_enter = driver.find_element(By.ID, 'user_password')
        pswd_enter.send_keys(pswd)
        
        driver.implicitly_wait(5)
    
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.NAME, "commit"))).click()
    
        # check if the file is downloaded or not (if yes break the code):
        file_present = False
        while file_present is False:
            if os.path.isfile(file_and_path.full_path):
                file_present = True
                break
    
        time.sleep(1)
    
        driver.quit()
        
        dm_download.df = pd.read_csv(file_and_path.full_path, skiprows = 2)
        return(dm_download.df)
    
    # function for api request:
    def api_request():
        
        submit_all()
    
        main_url = submit_all.form_url
        api_token = submit_all.api_token
    
        form_number = main_url.rpartition('/')[-1]
        url = f"url/{form_number}/url"
        
        headers = {'Authorization': api_token}
        response = requests.get(url + '?page = 1', headers=headers)
        
        api_request.data = response.json()
        return(api_request.data)
    
    # function for flatenization of the api:
    def api_flatten():
        
        api_request()
        data = api_request.data
        api_flatten.final_data = flatten(data)
        return(api_flatten.final_data)
    
    # function for getting a form_name:
    def form_name():
        
        submit_all()
        api_request()
        api_flatten()
        
        data = api_flatten.final_data
        form_name.formname = data["submissions_0_form_name"]
        if form_name.formname == submit_all.form_name:
            form_name.fname = 0
            pass
        elif form_name.formname != submit_all.form_name:
            messagebox.showerror('ERROR', 'Form name and URL are not applicable, please try again!')
            form_name.fname = 1
            exit()
     
    # function for extracting keys and values:
    def flt():
        
        api_flatten()

        final_data = api_flatten.final_data
    
        keys_origin = []
        values_origin = []
    
        for x, y in final_data.items():
            if x.startswith('submissions_0_') and x.endswith('_type') and y != 'subform':
                keys_origin.append(x)
                values_origin.append(y)

                flt.keys = keys_origin
                flt.values = values_origin
                
        return(flt.keys)
        return(flt.values)
    
    # function for preparation of the keys:
    def keys_prep():
        
        flt()

        keys_origin = flt.keys

        keys_list_a = []
        for a in keys_origin:
            if '_type_type' in a:
                a = a + '-type'
            else:
                a = a
            keys_list_a.append(a)

        # transformation phase b:
        keys_list_b = []
        for b in keys_list_a:
    
            b = re.sub('submissions_0_metadata_', '', b)
            b = re.sub('submissions_0_submission_', '', b)
            b = re.sub('_type', '', b)
    
            keys_list_b.append(b)
    
        # transformation phase c:
        keys_list_c = []

        for c in keys_list_b:
            if '-type' in c:
                c = re.sub('-type', '_type', c)
            else:
                c = c
            keys_list_c.append(c)
    
        # transformation phase d:
        keys_list_d = []
    
        for d in keys_list_c:
            if '_0_' in d:
                d = d.split('_0_',1)[1]
            else:
                d = d
            keys_list_d.append(d)
    
        # transformation phase e: 
        keys_list_e = []
    
        for e in keys_list_d:
            if '_0_' in e:
                e = e.split('_0_',1)[1]
            else:
                e = e
            keys_list_e.append(e)
    
        # additional transformation I:
        try:
            keys_final_one = []
            for x in keys_list_e:
                if '_0_' in x:
                    x = x.split('_0_',1)[1]
                else:
                    x = x
                keys_final_one.append(x)
        except:
            pass
    
        # additional transformation II:
        try:
    
            keys_final_two = []
    
            for y in keys_final_one:
                if '_0_' in y:
                    y = y.split('_0_',1)[1]
                else:
                    y = y
                keys_final_two.append(y)
                keys_prep.dict_of_keys = keys_final_two
            return(keys_prep.dict_of_keys)
        except:
            pass
        
    # function for preparation of the values:
    def values_prep():
        
        flt()

        values_origin = flt.values
        final_list_values = []
    
        for a in values_origin:
            if 'select' in a:
                final_list_values.append('nvarchar(MAX)')
            elif a == 'text':
                final_list_values.append('nvarchar(MAX)')
            elif a == 'string':
                final_list_values.append('nvarchar(MAX)')
            elif a == 'boolean':
                final_list_values.append('nchar(5)')
            elif a == 'phoneNumber':
                final_list_values.append('nvarchar(50)')
            elif a == 'date':
                final_list_values.append('date')
            elif a == 'time':
                final_list_values.append('time')
            elif a == 'datetime':
                final_list_values.append('smalldatetime')
            elif a == 'integer':
                final_list_values.append('int')
            elif a == 'decimal':
                final_list_values.append('float')
            elif a == 'gpsLocation':
                final_list_values.append('nvarchar(100)')
            elif a == 'email':
                final_list_values.append('nvarchar(50)')
            else:
                final_list_values.append('nvarchar(MAX)')
            values_prep.dict_of_values = final_list_values

        return(values_prep.dict_of_values)
    
    # function for preparation of the final dictionary:
    def final_dict():
        
        dm_download()
        keys_prep()
        values_prep()
        
        column_names = dm_download.df.columns.tolist()
        dict_keys = keys_prep.dict_of_keys
        dict_values = values_prep.dict_of_values
        dict_main = dict.fromkeys(column_names,
                                  'nvarchar(MAX)')
        
        dict_second = {dict_keys[i]: dict_values[i] for i in range(len(dict_values))}

        # clean dict second or api dict:
        diff = set(dict_second) - set(dict_main)
        diff_final = list(diff)
        dict_second = {key: dict_second[key] for key in dict_second if key not in diff_final}

        # dict_final = (dict_main)|(dict_second) as previous version!
        dict_final = {**dict_main, **dict_second}
        dt = 'nvarchar(MAX)'
        dict_final.update({'submitted_at': dt, 'received_at': dt})
        final_dict.dict_final = dict_final
        
        return(final_dict.dict_final)

    # main function:
    def initiate_main_function():
        
        try:
    
            form_name()
            if check_url.url == 0 and check_form_name.form == 0 and check_api_token.api == 0 and check_db.db == 0 and check_sql_tbl_name.tbl == 0 and form_name.fname == 0:
                res = messagebox.askyesno('Device SQL', 'Do you want to continue?', icon = 'warning') # implement a logic to be active when all checks are good!!!
            else:
                pass
            if res == True:
                sql_conn(db = submit_all()[5],
                         tbl = submit_all()[6])
                dm_download()
                final_dict()
                
                # prep sql tables in a list:
                get_tables = 'select table_name from information_schema.tables'
                sql_conn.cur.execute(get_tables)
                df_tbl = pd.DataFrame(sql_conn.cur.fetchall())
                df_tbl.rename(columns={0:'tables'},
                              inplace=True)
                df_tbl['tables'] = df_tbl['tables'].str[0]
                sql_tbls_list = df_tbl['tables'].tolist()
                
                # column names:
                column_name = dm_download.df.columns.tolist()
            
                # data type nvarchar max for all:
                column_data_type = 'nvarchar(max)'
                
                # for second api creation:
                dict_final = final_dict.dict_final
                
                column_name_two = dict_final.keys()
                column_name_two = list(column_name_two)
                
                column_data_type_two = dict_final.values()
                column_data_type_two = list(column_data_type_two)
                
                # first query
                sql_tbl = sql_conn.sql_tbl
                drop_table = f'DROP TABLE IF EXISTS {sql_tbl}'
                
                # second query:
                create_tbl = f'CREATE TABLE {sql_tbl} ('
                for x in column_name:
                    create_tbl = create_tbl + x + ' ' + column_data_type + ' ' + 'NULL' + ',' + ' '
                create_tbl = create_tbl[:-1] + ' );'
                
                # first query part II:
                drop_table_two = f'DROP TABLE IF EXISTS {sql_tbl}'
                
                # second query part II:
                create_tbl_two = f'CREATE TABLE {sql_tbl} ('
                for x in range(len(column_data_type_two)):
                    create_tbl_two = create_tbl_two + column_name_two[x] + ' ' + column_data_type_two[x] + ' ' + 'NULL' + ',' + ' '
                create_tbl_two = create_tbl_two[:-1] + ' );'
                selection = submit_all.default_selection
    
                if selection == 'YES' and sql_tbl in sql_tbls_list:
                    res2 = messagebox.askyesno('Device SQL', f'SQL table {sql_tbl} already exist, by clicking YES current table will be overwritten, do you want to continue?', icon = 'warning')
                    if res2 == True:
                        sql_conn.cur.execute(drop_table)
                        sql_conn.cur.commit()
                        
                        # creating table with nvarchar for everything:
                        sql_conn.cur.execute(create_tbl)
                        sql_conn.cur.commit()
                        
                        msg(t = submit_all()[6],
                            m = 'o')
                        
                        email(f = submit_all()[3],
                              l = submit_all()[1],
                              d = submit_all()[5],
                              t = submit_all()[6],
                              m = 'ot')
                    elif res2 == False:
                        warnings.filterwarnings("ignore")
                        messagebox.showinfo('Device SQL', 'You will be brought to previous window')
                        exit()
                elif selection == 'NO' and sql_tbl in sql_tbls_list:
                    res3 = messagebox.askyesno('Device SQL', f'SQL table {sql_tbl} already exist, by clicking YES current table will be overwritten, do you want to continue?', icon = 'warning')
                    if res3 == True:
                        
                        # droping table if exist:
                        sql_conn.cur.execute(drop_table_two)
                        sql_conn.cur.commit()
                        
                        sql_conn.cur.execute(create_tbl_two)
                        sql_conn.cur.commit()
                        
                        msg(t = submit_all()[6],
                            m = 'o')
                        
                        email(f = submit_all()[3],
                              l = submit_all()[1],
                              d = submit_all()[5],
                              t = submit_all()[6],
                              m = 'ot')
                    elif res3 == False:
                        warnings.filterwarnings("ignore")
                        messagebox.showinfo('Device SQL', 'You will be brought to previous window')
                        exit() 
                elif selection == 'YES' and sql_tbl not in sql_tbls_list:
                    sql_conn.cur.execute(drop_table)
                    sql_conn.cur.commit()
                    
                    # creating table with nvarchar for everything:
                    sql_conn.cur.execute(create_tbl)
                    sql_conn.cur.commit()
                    
                    msg(t = submit_all()[6],
                            m = 'c')
                        
                    email(f = submit_all()[3],
                          l = submit_all()[1],
                          d = submit_all()[5],
                          t = submit_all()[6],
                          m = 't')  
                elif selection == 'NO' and sql_tbl not in sql_tbls_list:
                    
                    sql_conn.cur.execute(drop_table_two)
                    sql_conn.cur.commit()
                    
                    # creating table with specific data types for everything:
                    sql_conn.cur.execute(create_tbl_two)
                    sql_conn.cur.commit()
                    
                    msg(t = submit_all()[6],
                            m = 'c')
                    
                    email(f = submit_all()[3],
                          l = submit_all()[1],
                          d = submit_all()[5],
                          t = submit_all()[6],
                          m = 't')
                else:
                    pass
            elif res == False:
                warnings.filterwarnings("ignore")
                messagebox.showinfo('Device SQL', 'You will be brought to previous window')
                exit()
            else:
                pass
        except Exception as Argument:
            
            f = open("device_sql_app_log_file.txt", "a")
    
            f.write(" **** Create SQL table ERROR: ")
            f.write("\n")
            f.write("\n")
            f.write(str(Argument)) # catching all erros within Argument variable!
            f.write("\n")
            f.write("\n")
            
            f.close()
            
            messagebox.showerror('ERROR', 'Device SQL application interrupted, please check: device_sql_app_log_file for more information!')
            
            exit()
            
        sql_conn.conn.close()
            
    # function for cursor:
    def cursor():
            window_01.config(cursor="watch")
            window_01.update()
            time.sleep(5)
            window_01.config(cursor="")
            
    # function for navigating to the next page or map sql table:
    def next_page():
        window_01.withdraw()
        page_two()
        
    ###########################    
    # window one:
    
    window_01 = Toplevel(window_main)
    
    s = ttk.Style()
    s.configure("custom.TButton", foreground="#ffffff", background="#1c1c1c")
    
    window_01.title('Device SQL: Create SQL table')
    
    p1 = PhotoImage(file = "ds.png")
    window_01.iconphoto(False, p1)
    
    # center window:
    w = 700
    h = 678
     
    screen_width = window_01.winfo_screenwidth()
    screen_height = window_01.winfo_screenheight()
     
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
     
    window_01.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    # canvas for window one:
    window_01.configure(bg = "#ffffff")
    canvas = Canvas(
        window_01,
        bg = "#ffffff",
        height = 678,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background_img = PhotoImage(file = f"background_01.png")
    background = canvas.create_image(
        350.0, 339.0,
        image=background_img)
    
    # default creation (yes/no) radio button:
    default = StringVar()
    default.set('YES')
    
    entry0 = Radiobutton(
        window_01,
        bd = 2,
        bg = "#908A8A",
        highlightthickness = 2,
        text = 'YES',
        variable = default,
        value = 'YES',
        cursor = 'hand2')
    
    entry0.place(
        x = 46, y = 495,
        width = 100,
        height = 33)
    
    entry00 = Radiobutton(
        window_01,
        bd = 2,
        bg = "#908A8A",
        highlightthickness = 2,
        text = 'NO',
        variable = default,
        value = 'NO',
        cursor = 'hand2')
    
    entry00.place(
        x = 147, y = 495,
        width = 100,
        height = 33)
    
    # table name:
    tname = StringVar()
    tname.set("E.G: table_name/tablename/ (use underscore '_' to separate characters or combine them without spaces !)")
    
    entry1_img = PhotoImage(file = f"img_textBox1_01.png")
    entry1_bg = canvas.create_image(
        353.0, 441.5,
        image = entry1_img)
    
    entry1 = Entry(
        window_01,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = tname)
    
    entry1.place(
        x = 46, y = 424,
        width = 614,
        height = 33)
    
    # database name:
    dbname = StringVar()
    dbname.set("E.G: db_name")

    entry2_img = PhotoImage(file = f"img_textBox2_01.png")
    entry2_bg = canvas.create_image(
        353.0, 299.5,
        image = entry2_img)
    
    entry2 = Entry(
        window_01,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = dbname)
    
    entry2.place(
        x = 46, y = 353,
        width = 614,
        height = 33)
    
    # api token:
    token = StringVar()
    token.set("E.G: Basic xxxxxxyyyyyy==")
    
    entry3_img = PhotoImage(file = f"img_textBox3_01.png")
    entry3_bg = canvas.create_image(
        353.0, 299.5,
        image = entry3_img)
    
    entry3 = Entry(
        window_01,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = token)
    
    entry3.place(
        x = 46, y = 282,
        width = 614,
        height = 33)
    
    # form name:
    fname = StringVar()
    fname.set("E.G: form_name")
    
    entry4_img = PhotoImage(file = f"img_textBox4_01.png")
    entry4_bg = canvas.create_image(
        353.0, 228.5,
        image = entry4_img)
    
    entry4 = Entry(
        window_01,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = fname)
    
    entry4.place(
        x = 46, y = 211,
        width = 614,
        height = 33)
    
    # form url:
    furl = StringVar()
    furl.set("E.G: https://devicemagic.ext.icrc.org/organizations/xxx/web_stores/yyyyy")
    
    entry5_img = PhotoImage(file = f"img_textBox5_01.png")
    entry5_bg = canvas.create_image(
        353.0, 155.5,
        image = entry5_img)
    
    entry5 = Entry(
        window_01,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = furl)
    
    entry5.place(
        x = 46, y = 138,
        width = 614,
        height = 33)
    
    # button two NEXT page (map sql table part):
    img1 = PhotoImage(file = f"img1_01.png")
    b1 = Button(
        window_01,
        image = img1,
        borderwidth = 2,
        highlightthickness = 2,
        command = next_page,
        cursor = 'hand2',
        relief = "flat")
    
    b1.place(
        x = 230, y = 628,
        width = 245,
        height = 50)
    
    # button three main button Create SQL table:
    img2 = PhotoImage(file = f"img2_01.png")
    b2 = Button(
        window_01,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:[check_url(), check_form_name(), check_api_token(), check_db(), check_sql_tbl_name(), check_submissions(),
                          initiate_main_function(),
                          cursor(),
                          delete_file()],
        cursor = 'hand2',
        relief = "flat")
    
    b2.place(
        x = 3, y = 530,
        width = 700,
        height = 83)
    
    window_01.resizable(False, False)

    window_01.mainloop()
    
###########################
# second window or page:

def second_page():
    
    def map_all():
        
        formu = furl_02.get()
        fn = fname_02.get()
        dbn = dbname_02.get()
        tbln = tname_02.get()
    
        l1 = list(formu)
        l2 = list(fn)
        l3 = list(dbn)
        l4 = list(tbln)
        
        list1 = ''.join(l1)
        list2 = ''.join(l2)
        list3 = ''.join(l3)
        list4 = ''.join(l4)
        
        # main variables used for the main script:
        map_all.form_url = list1
        map_all.form_name = list2
        map_all.database_name = list3
        map_all.table_name = list4
        
        return(map_all.form_url, # 0
               map_all.form_name, # 1
               map_all.database_name, # 2
               map_all.table_name) # 3
    
    # function to check url:
    def check_url():
        
        map_all()
        url_string = map_all.form_url
        text = re.compile(r".*[0-9]$")
        valid = validators.url(url_string)
        
        if valid == True and url_string.startswith('url/') and text.match(url_string) and "forms" in url_string:
            entry3.configure(foreground="black")
            check_url.url = 0
            return(check_url.url)
        else:
            entry3.configure(foreground="red")
            check_url.error = messagebox.showerror('ERROR', 'Invalid Form URL!')
            check_url.error
            check_url.url = 1
            return(check_url.url)
            exit()
            
    # function to check form name:
    def check_form_name():
        
        map_all()
        
        fname_string = map_all.form_name
        if fname_string == fname_string.strip():
            entry2.configure(foreground="black")
            check_form_name.form = 0
            return(check_form_name.form)
        else:
            entry2.configure(foreground="red")
            check_form_name_error = messagebox.showerror('ERROR', 'Invalid Form name!')
            check_form_name_error
            check_form_name.form = 1
            return(check_form_name.form)
            exit()
            
    # function to check db name:
    def check_db():
        
        sql_conn(db = 'master',
                 tbl = '')

        map_all()
        db_name_string = map_all.database_name
            
        # query:
        get_dbs = 'EXEC sp_databases'
        sql_conn.cur.execute(get_dbs)
        df_db = pd.DataFrame(sql_conn.cur.fetchall())
        df_db.rename(columns={0:'databases'},
                      inplace=True)
        df_db['databases'] = df_db['databases'].str[0]
        sql_db_list = df_db['databases'].tolist()
        sql_db_list = [e for e in sql_db_list if e not in ('master', 'model', 'msdb', 'tempdb')]
        if db_name_string in sql_db_list:
            entry1.configure(foreground="black")
            check_db.db = 0
            return(check_db.db)
        else:
            entry1.configure(foreground="red")
            check_db.db_error = messagebox.showerror('ERROR', f'Invalid Database, Database: {db_name_string} does NOT exist within a server!')
            check_db.db_error
            check_db.db = 1
            return(check_db.db)
            exit()
        sql_conn.conn.close()
            
    # function to check sql table:
    def check_sql_tbl_name():
        
        map_all()
        tbl_string = map_all.table_name
        if ' ' not in tbl_string:
            entry0.configure(foreground="black")
            check_sql_tbl_name.tbl = 0
            return(check_sql_tbl_name.tbl)
        else:
            entry0.configure(foreground="red")
            check_sql_tbl_name_error = messagebox.showerror('ERROR', 'Invalid Table name!')
            check_sql_tbl_name_error
            check_sql_tbl_name.tbl = 1
            return(check_sql_tbl_name.tbl)
            exit()
            
    # function for preparation of the sql table ids:
    def prep_sql_tbl_id():
        
        sql_conn(db = map_all()[2],
                 tbl = map_all()[3])
        
        db_name = sql_conn.db_name
        tbl_name = sql_conn.sql_tbl
    
        try:
           warnings.filterwarnings("ignore")
           df0 = pd.read_sql(f"SELECT * FROM {tbl_name}", sql_conn.conn)
        except:
            messagebox.showerror('ERROR', f'SQL table: {tbl_name} does not exist within: {db_name} database!')
            exit()
           
        # keep only standard columns before insertion in SQL:
        standard_columns = df0.columns.tolist()
        
        # logic of preparation:
        sql_table_ids = []
        for x in standard_columns:
            x = 'templates_' + x
            sql_table_ids.append(x)
            prep_sql_tbl_id.sql_tbl_ids = sql_table_ids
        return(prep_sql_tbl_id.sql_tbl_ids)
        sql_conn.conn.close()
    
    # function for preparation of the meta data dm table ids:
    def meta_data():
        
        dm_table_id_meta = ['x',
                            'y',
                            'c',
                            'r',
                            'e',
                            'r']
        dm_table_id_meta_final = []
        for y in dm_table_id_meta:
            y = '{{' + y + '}}'
            dm_table_id_meta_final.append(y)
            meta_data.dm_table_id_meta_final = dm_table_id_meta_final
        return(meta_data.dm_table_id_meta_final)
    
    # main function for preparation of the dm table ids:
    def sql_destination():
        
        try:
            map_all()
            prep_sql_tbl_id()
            meta_data()
        
            dmformpath = map_all.form_url
            
            final_wd_path = wd_path()
            wdpath = Service(final_wd_path)
            
            options = webdriver.ChromeOptions()
            
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("--headless")
            
            options.add_argument("--no-sandbox")
            
            options.add_argument("--disable-gpu")
            
            options.add_argument("--disable-infobars")
            
            options.add_argument("--ignore-certificata-errors")
            
            options.add_argument("--disable-extensions")
            
            # run:
            wdpath.creationflags = CREATE_NO_WINDOW
            driver = webdriver.Chrome(service=wdpath, options=options)
            driver.get(dmformpath)
            driver.implicitly_wait(5)
        
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "user_remember_me_1"))).click()
            
            mail = 'xxx'
            mail_enter = driver.find_element(By.ID, 'user_email')
            mail_enter.send_keys(mail)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "commit"))).click()
        
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "user_password")))
            
            pswd = 'ttt'
            pswd_enter = driver.find_element(By.ID, 'user_password')
            pswd_enter.send_keys(pswd)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "commit"))).click()
            
            driver.implicitly_wait(5)
            
            # creation of the sql destination:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "create_destination_link"))).click()
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport-list-item"))).click()
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "xml_format-list-item"))).click()
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "destination_description")))
            
            dstn = driver.find_element(By.ID, 'destination_description')
            dstn.send_keys('db')
            dstn.send_keys(Keys.RETURN)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_host")))
            
            host = driver.find_element(By.ID, 'sql_transport_host')
            host.send_keys('sss')
            host.send_keys(Keys.RETURN)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_username")))
            
            usrnm = driver.find_element(By.ID, 'sql_transport_username')
            usrnm.send_keys('fff')
            usrnm.send_keys(Keys.RETURN)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_password")))
            
            pswd1 = 'ppp'
            pswd_enter1 = driver.find_element(By.ID, 'sql_transport_password')
            pswd_enter1.send_keys(pswd1)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_port")))
            
            port = driver.find_element(By.ID, 'sql_transport_port')
            port.send_keys('port')
            port.send_keys(Keys.RETURN)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "sql_transport_database_name")))
            
            # database variable:
            database = map_all.database_name
            dbnm = driver.find_element(By.ID, 'template')
            dbnm.send_keys(f'{database}')
            
            time.sleep(1)
            
            driver.implicitly_wait(5)
            s1 = driver.find_element(By.ID, 'fetch-table-names')
            driver.execute_script("arguments[0].click();",s1)
        
            driver.implicitly_wait(5)
            
            s2 = driver.find_element(By.XPATH, '//*[@id="ttt"]')
            driver.execute_script("arguments[0].click();",s2)
            
            table =  map_all.table_name
            select = Select(driver.find_element(By.XPATH, '//*[@id="s"]'))
            select.select_by_visible_text(f'{table}')
            driver.implicitly_wait(5)
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="sql_transport_config"]/div[2]/div/div[9]/div[2]/p[1]/a'))).click()
            
            # prep I:
            fields_list = []
            items = driver.find_elements(By.TAG_NAME, "li")
            for x in items:
                fields_list.append(x.text)
                
            # prep II:
            dm_table_id_fields = []
            for x in fields_list:
                if x.startswith('{{') and x.endswith('}}'):
                    dm_table_id_fields.append(x)
                    
            # delete IT not needed field:  
            try:
                dm_table_id_fields.remove('{{device.IT}}')
            except:
                pass
            
            # prep III (final):
            dm_table_id_meta = meta_data.dm_table_id_meta_final
            dm_table_id_meta.extend(dm_table_id_fields)
            dm_table_id = dm_table_id_meta
            sql_table_id = prep_sql_tbl_id.sql_tbl_ids
               
            # part III (mapping):
            dm_table_id_list = dm_table_id
            sql_table_id_list = sql_table_id
            
            # for loop:
            driver.implicitly_wait(5)
            for x, y in zip (dm_table_id_list, sql_table_id_list):
                field_enter = driver.find_element(By.ID, y)
                field_enter.send_keys(x)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "create_new_destination_button"))).click()
            
            driver.quit()
            
            msg(t = map_all()[3],
                m = 'm')
            
            email(f = map_all()[1],
                  l = map_all()[0],
                  d = map_all()[2],
                  t = map_all()[3],
                  m = 'm')
        
        except Exception as Argument:
            
            f = open("device_sql_app_log_file.txt", "a")
    
            f.write("---- Map DM for with a SQL table ERROR: ")
            f.write("\n")
            f.write("\n")
            f.write(str(Argument)) # catching all erros within Argument variable!
            f.write("\n")
            f.write("\n")
            
            f.close()
            
            messagebox.showerror('ERROR', 'Device SQL application interrupted, please check: device_sql_app_log_file for more details!')
            
            exit()        
        
    # function for cursor:
    def cursor():
            window_02.config(cursor="watch")
            window_02.update()
            time.sleep(1)
            window_02.config(cursor="")
            
    # main function:
    def main_func():
        if check_url.url == 0 and check_form_name.form == 0 and check_db.db == 0 and check_sql_tbl_name.tbl == 0:
            res = messagebox.askyesno('Device SQL', 'Do you want to continue?', icon = 'warning') # implement a logic to be active when all checks are good!!!
        else:
            pass
        if res == True:
            sql_destination()
            cursor()
        elif res == False:
            warnings.filterwarnings("ignore")
            messagebox.showinfo('Device SQL', 'You will be brought to previous window')
            exit()
        else:
            pass
        
    def back_page():
        window_02.withdraw()
        first_page()
        
    #############
    # window two:
    
    window_02 = Toplevel(window_main)
    
    window_02.title('Device SQL: Map SQL table')
    
    p1 = PhotoImage(file = "ds.png")
    window_02.iconphoto(False, p1)
    
    # center window:
    w = 700
    h = 678
     
    screen_width = window_02.winfo_screenwidth()
    screen_height = window_02.winfo_screenheight()
     
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
     
    window_02.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    # canvas:
    canvas = Canvas(
        window_02,
        bg = "#ffffff",
        height = 678,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background_img = PhotoImage(file = f"background_02.png")
    background = canvas.create_image(
        350.0, 339.0,
        image=background_img)
    
    # sql table name:
    tname_02 = StringVar()
    tname_02.set("E.G: table_name/tablename/ (use underscore '_' to separate characters or combine them without spaces !)")
    
    entry0_img = PhotoImage(file = f"img_textBox0_02.png")
    entry0_bg = canvas.create_image(
        353.0, 434.5,
        image = entry0_img)
    
    entry0 = Entry(
        window_02,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = tname_02)
    
    entry0.place(
        x = 46, y = 417,
        width = 614,
        height = 33)
    
    # database name:
    dbname_02 = StringVar()
    dbname_02.set("E.G: db_name")

    entry1_img = PhotoImage(file = f"img_textBox1_02.png")
    entry1_bg = canvas.create_image(
        353.0, 299.5,
        image = entry1_img)
    
    entry1 = Entry(
        window_02,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = dbname_02)
    
    entry1.place(
        x = 46, y = 353,
        width = 614,
        height = 33)
    
    # form name
    fname_02 = StringVar()
    fname_02.set("E.G:_form_name")
    
    entry2_img = PhotoImage(file = f"img_textBox2_02.png")
    entry2_bg = canvas.create_image(
        353.0, 292.5,
        image = entry2_img)
    
    entry2 = Entry(
        window_02,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        textvariable = fname_02)
    
    entry2.place(
        x = 46, y = 280,
        width = 614,
        height = 33)
    
    # url name:
    furl_02 = StringVar()
    furl_02.set("E.G: xxx")
    
    entry3_img = PhotoImage(file = f"img_textBox3_02.png")
    entry3_bg = canvas.create_image(
        353.0, 219.5,
        image = entry3_img)
    
    entry3 = Entry(
        window_02,
        bd = 1,
        bg = "#ffffff",
        highlightthickness = 1,
        textvariable = furl_02)
    
    entry3.place(
        x = 46, y = 202,
        width = 614,
        height = 33)
    
    # previous button:
    img0 = PhotoImage(file = f"img0_02.png")
    b0 = Button(
        window_02,
        image = img0,
        borderwidth = 2,
        highlightthickness = 2,
        command = back_page,
        cursor = 'hand2',
        relief = "flat")
    
    b0.place(
        x = 225, y = 627,
        width = 255,
        height = 51)
    
    # main button (map):
    img2 = PhotoImage(file = f"img2_02.png")
    b2 = Button(
        window_02,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        
        command = lambda:[check_url(),
                          check_form_name(),
                          check_db(),
                          check_sql_tbl_name(),
                          main_func()],
        
        cursor = 'hand2',
        relief = "flat")
    
    b2.place(
        x = 3, y = 452,
        width = 700,
        height = 152)
    

    window_02.resizable(False, False)
    window_02.mainloop()

# calling mains and closing the loop app:
window_main.resizable(False, False)
window_main.mainloop()
