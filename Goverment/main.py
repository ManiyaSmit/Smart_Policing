from pathlib import Path
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage, filedialog
from PIL import Image, ImageTk
import tkinter as tk    
import translator, time, detect_lang, file_opener, os, news, threading, random, string, requests
import s_tk, bard_ai, ps
import firebase_gov

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/anton/Desktop/new_code/main/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def go_to_login():
    canvas_login.place(x = 0, y = 0)
    canvas_home.place_forget()

def go_back_from_login():
    canvas_home.place(x = 0, y  = 0)
    canvas_login.place_forget()

def go_to_funcs():
    clear_login()
    canvas_functions.place(x = 0, y = 0)
    canvas_login.place_forget()

id = 0                
def set_news_on_textarea(id):
    new_text = news.get_latest_news(id)
    ai_main_act_textarea.config(state=tk.NORMAL)
    ai_main_act_textarea.delete(1.0, 'end')
    ai_main_act_textarea.insert(tk.END, new_text)
    ai_main_act_textarea.config(state=tk.DISABLED)

def go_to_ai_main_act():
    global ai_img_id, ppsu_logo_img, id
    ai_img_id = canvas_nav.create_image(
        1431.0,
        55.0,
        image=ai_logo
    )
    canvas_nav.delete(ppsu_logo_img)
    canvas_ai_how_can_i_help.place(x = 340, y = 114)
    canvas_ai_main_act.place(x = 0, y = 0)
    canvas_functions.place_forget()
    window.after(300, set_news_on_textarea, id)
    id += 1
    #news_text = threading.Thread(target=set_news_on_textarea(), args=())
    #news_text.start()

def go_to_main_act():
    global img_id
    #clear_login()
    search.place(
        x=926.0,
        y=67.0,
        width=486.0,
        height=24.0
    )
    img_id = canvas_nav.create_image(
        960.0,
        43.0,
        image=search_img
    )
    canvas_how_can_i_help.place(x = 340, y = 114)
    canvas_main_act.place(x = 0, y = 0)
    canvas_functions.place_forget()

def go_back_from_ai_main_act():
    global ai_img_id, ppsu_logo_img
    canvas_functions.place(x = 0, y = 0)
    canvas_nav.delete(ai_img_id)
    ppsu_logo_img = canvas_nav.create_image(
        1449.0,
        59.0,
        image=ppsu_logo
    )
    canvas_ai_main_act.place_forget()
    canvas_ai_how_can_i_help.place_forget()
    canvas_translate_service.place_forget()
    canvas_summarize_document.place_forget()
    ai_main_act_textarea.delete(1.0, 'end')


def go_back_from_main_act():
    global img_id
    canvas_functions.place(x = 0, y = 0)
    search.place_forget()
    canvas_nav.delete(img_id)
    canvas_main_act.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()
    icd_clear()
    imd_clear()

def go_back_from_func():
    canvas_login.place(x = 0, y = 0)
    canvas_functions.place_forget()

def go_to_vcd():
    canvas_view_citizen_data.place(x = 340, y = 114)
    canvas_how_can_i_help.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_icd():
    canvas_insert_criminal_data.place(x = 340, y = 114)
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_imd():
    canvas_insert_missing_data.place(x = 340, y = 114)
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_vmd():
    canvas_view_missing_data.place(x = 340, y = 114)
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_va():
    canvas_view_alerts.place(x = 340, y= 114)
    canvas_view_missing_data.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_vcmd():
    canvas_view_crim_data.place(x = 340, y = 114)
    canvas_view_alerts.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_del_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_dcd():
    canvas_del_crim_data.place(x = 340, y = 114)
    canvas_view_alerts.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_crim_data.place_forget()
    canvas_del_missing_data.place_forget()

def go_to_dmd():
    canvas_del_missing_data.place(x = 340, y = 114)
    canvas_del_crim_data.place_forget()
    canvas_view_alerts.place_forget()
    canvas_view_missing_data.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_view_citizen_data.place_forget()
    canvas_insert_criminal_data.place_forget()
    canvas_insert_missing_data.place_forget()
    canvas_view_crim_data.place_forget()

def icd_insert():
    global img_path_criminal
    firstname = icd_first_name.get()
    lastname = icd_last_name.get()
    age = icd_age.get()
    gender = icd_gender.get()
    desc = icd_textarea.get(1.0, 'end')
    image = img_path_criminal
    print(img_path_criminal)
    if firstname != '' and lastname != '' and age != '' and gender != '' and desc != '' and image != '':
        firebase_gov.insert_into_criminal_database(firstname, lastname, age, gender, desc, image)
        icd_clear()
        img_path_criminal = ''
    else:
        print("no")


def imd_insert():
    print(imd_first_name.get(), imd_last_name.get(), imd_age.get(), imd_gender.get())

def icd_clear():
    icd_first_name.delete(0, 'end')
    icd_last_name.delete(0, 'end')
    icd_age.delete(0, 'end')
    icd_gender.delete(0, 'end')
    icd_textarea.delete(1.0, 'end')

def imd_clear():
    imd_first_name.delete(0, 'end')
    imd_last_name.delete(0, 'end')
    imd_age.delete(0, 'end')
    imd_gender.delete(0, 'end')
    imd_textarea.delete(1.0, 'end')

def go_to_translation_service():
    canvas_translate_service.place(x = 340, y = 114)
    canvas_ai_how_can_i_help.place_forget()
    canvas_summarize_document.place_forget()

def go_to_summarize_document():
    canvas_summarize_document.place(x = 340, y = 114)
    canvas_translate_service.place_forget()
    canvas_ai_how_can_i_help.place_forget()

def clear_login():
    gov_id.delete(0, 'end')
    pwd.delete(0, 'end')

img_path_criminal = ''
def select_image_criminal():
    global img_path_criminal
    img_path_criminal = filedialog.askopenfilename(title = 'Open file to be read', initialdir='/home/anton/Pictures/', filetypes = [("Photos", "*.png *.jpg *.jpeg")])

# function to clear the text from translation service
def ts_clear():
    ts_textarea.delete(1.0, 'end')

def sd_clear():
    sd_textarea.delete(1.0, 'end')

# function will translate the text
def ts_translate_text():
    text = ts_textarea.get(1.0, 'end')
    source_language = detect_lang.detect_language(text)
    translated_text = translator.translate_text(text, source_language, dropdown_var.get())
    ts_textarea.delete(1.0, 'end')
    ts_textarea.insert(tk.END, translated_text)

# function to summarize the data
def sd_summarize_text():
    text = sd_textarea.get(1.0, 'end')
    summarized_text = bard_ai.bard_answer(summarization=True, doc=text)
    sd_textarea.delete(1.0, 'end')
    sd_textarea.insert(tk.END, summarized_text)

# function to read the pdf or docx or text
def ts_choose_file():
    file_path = filedialog.askopenfilename(title = 'Open file to be read', filetypes = [("Readable Files", "*.pdf *.docx *.txt")])
    if file_path:
        ts_textarea.delete(1.0, 'end')
        file_name, file_ext = os.path.splitext(file_path)
        if file_ext == '.pdf':
            text = file_opener.read_pdf(file_path)
            ts_textarea.insert(tk.END, text)
        elif file_ext == '.docx':
            text = file_opener.read_docx(file_path)
            ts_textarea.insert(tk.END, text)
        elif file_ext == '.txt':
            with open(file_path, 'r') as file:
                text = file.read()
                ts_textarea.insert(tk.END, text)

# function to read the pdf or docx or text for summarization
def sd_choose_file():
    file_path = filedialog.askopenfilename(title = 'Open file to be read', filetypes = [("Readable Files", "*.pdf *.docx *.txt")])
    if file_path:
        sd_textarea.delete(1.0, 'end')
        file_name, file_ext = os.path.splitext(file_path)
        if file_ext == '.pdf':
            text = file_opener.read_pdf(file_path)
            sd_textarea.insert(tk.END, text)
        elif file_ext == '.docx':
            text = file_opener.read_docx(file_path)
            sd_textarea.insert(tk.END, text)
        elif file_ext == '.txt':
            with open(file_path, 'r') as file:
                text = file.read()
                sd_textarea.insert(tk.END, text)

# function to generate random name
def generate_random_filename():
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(10))
    return random_id

def ts_download():
    global saved_notification
    canvas_translate_service.itemconfig(saved_notification, text = '')
    file_path = filedialog.askdirectory(title = 'Choose dir to download file')
    if file_path:
        text = ts_textarea.get(1.0, 'end')
        file_name = generate_random_filename() + '.txt'
        #file_path += '/' + generate_random_filename() + '.txt'
        if os.path.exists(f'{file_path}/{file_name}'):
            file_name = generate_random_filename() + '.txt'
            #file_path += '/' + generate_random_filename() + '.txt'
            while not os.path.exists(f'{file_path}/{file_name}'):
                file_name = generate_random_filename() + '.txt'
                #file_path += '/' + generate_random_filename() + '.txt'
        
        file_opener.create_txt(f'{file_path}/{file_name}', text)
        saved_notification = canvas_translate_service.create_text(
            45.0,
            800.0,
            anchor="nw",
            text=f"File has been saved to path : {file_path} and filename : {file_name}",
            fill="#74B72E",
            font=("RalewayRoman", "14")
        )

def sd_download():
    global saved_notification
    canvas_summarize_document.itemconfig(saved_notification, text = '')
    file_path = filedialog.askdirectory(title = 'Choose dir to download file')
    if file_path:
        text = sd_textarea.get(1.0, 'end')
        file_name = generate_random_filename() + '.txt'
        #file_path += '/' + generate_random_filename() + '.txt'
        if os.path.exists(f'{file_path}/{file_name}'):
            file_name = generate_random_filename() + '.txt'
            #file_path += '/' + generate_random_filename() + '.txt'
            while not os.path.exists(f'{file_path}/{file_name}'):
                file_name = generate_random_filename() + '.txt'
                #file_path += '/' + generate_random_filename() + '.txt'
        
        file_opener.create_txt(f'{file_path}/{file_name}', text)
        saved_notification = canvas_summarize_document.create_text(
            45.0,
            800.0,
            anchor="nw",
            text=f"File has been saved to path : {file_path} and filename : {file_name}",
            fill="#74B72E",
            font=("RalewayRoman", "14")
        )

window = Tk()
window.title("Smart Police")
window.geometry("1500x940")
window.configure(bg = "#F5F5F5")

ai_logo = PhotoImage(file=relative_to_assets("ai_logo.png"))
police_img = PhotoImage(file=relative_to_assets("police.png"))
ppsu_logo = PhotoImage(file=relative_to_assets("ppsu.png"))
safe_city_img = PhotoImage(file=relative_to_assets("safe_city.png"))
method_btn_img = PhotoImage(file=relative_to_assets("method.png"))
about_btn_img = PhotoImage(file=relative_to_assets("about.png"))
req_btn_img = PhotoImage(file=relative_to_assets("req.png"))
desc_img = PhotoImage(file=relative_to_assets("desc.png"))
login_home_btn_img = PhotoImage(file=relative_to_assets("login_home.png"))
ai_pol_img = PhotoImage(file=relative_to_assets("ai_pol.png"))


# ------------------------------------------------------------
# HOME PAGE

canvas_home = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
about_btn = Button(
    canvas_home,
    image=about_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("about this"),
    relief="flat"
)
about_btn.place(
    x=343.0,
    y=42.0,
    width=78.0,
    height=39.0
)
method_btn = Button(
    canvas_home,
    image=method_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("method this"),
    relief="flat"
)
method_btn.place(
    x=472.0,
    y=38.0,
    width=96.0,
    height=43.0
)
req_btn = Button(
    canvas_home,
    image=req_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("req this"),
    relief="flat"
)
req_btn.place(
    x=626.0,
    y=44.0,
    width=162.0,
    height=42.0
)
canvas_home.create_image(
    358.0,
    443.0,
    image=desc_img
)
login_home_btn = Button(
    canvas_home,
    image=login_home_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_login,
    relief="flat"
)
login_home_btn.place(
    x=127.0,
    y=686.0,
    width=198.0,
    height=62.0
)
canvas_home.create_image(
    1103.0,
    490.0,
    image=ai_pol_img
)

canvas_home.place(x = 0, y = 0)

# --------------------------------------------------------------


# -------------------------------------------------------------
# LOGIN PAGE

log_img = PhotoImage(file=relative_to_assets("log.png"))
get_started_btn_img = PhotoImage(file=relative_to_assets("gs.png"))
forgot_btn_img = PhotoImage(file=relative_to_assets("forgot.png"))
back_btn_img = PhotoImage(file=relative_to_assets("back.png"))
gov_id_bg_img = PhotoImage(file=relative_to_assets("gov_id_bg.png"))
login_desc_img = PhotoImage(file=relative_to_assets("login_desc.png"))
pols_light_img = PhotoImage(file=relative_to_assets("pols_light.png"))


canvas_login = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_login.create_image(
    1114.0,
    525.0,
    image=log_img
)
canvas_login.create_rectangle(
    0.0,
    102.0,
    729.5,
    940.0,
    fill="#D3D3D3",
    outline="")
# go_to_main_act was here
get_started_btn = Button(
    canvas_login,
    image=get_started_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_funcs,
    relief="flat"
)
get_started_btn.place(
    x=949.0,
    y=723.0,
    width=326.0,
    height=69.0
)
forgot_btn = Button(
    canvas_login,
    image=forgot_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("forgot this"),
    relief="flat"
)
forgot_btn.place(
    x=986.0,
    y=792.0,
    width=275.0,
    height=38.0
)
back_btn = Button(
    canvas_login,
    image=back_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command = go_back_from_login,
    relief="flat"
)
back_btn.place(
    x=9.0,
    y=853.0,
    width=76.0,
    height=75.0
)
canvas_login.create_image(
    1118.0,
    436.0,
    image=gov_id_bg_img
)
gov_id = Entry(
    canvas_login,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "16")
)
gov_id.place(
    x=907.0,
    y=417.0,
    width=422.0,
    height=36.0
)
canvas_login.create_image(
    1118.0,
    571.0,
    image=gov_id_bg_img
)
pwd = Entry(
    canvas_login,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "16"),
    show = "*"
)
pwd.place(
    x=907.0,
    y=552.0,
    width=422.0,
    height=36.0
)
canvas_login.create_image(
    363.0,
    668.0,
    image=login_desc_img
)
canvas_login.create_image(
    364.0,
    282.0,
    image=pols_light_img
)
# ---------------------------------------------------------


#----------------------------------------------------------
# main activity

view_cit_data_btn_img = PhotoImage(file=relative_to_assets("view_cit_data.png"))
view_crime_data_btn_img = PhotoImage(file=relative_to_assets("view_crim_data.png"))
view_miss_person_data_btn_img = PhotoImage(file=relative_to_assets("view_miss_person_data.png"))
insert_crim_data_btn_img = PhotoImage(file=relative_to_assets("insert_crim_data.png"))
view_alert_hist_btn_img = PhotoImage(file=relative_to_assets("view_alert_hist.png"))
insert_miss_person_data_btn_img = PhotoImage(file=relative_to_assets("insert_miss_person_data.png"))
del_crim_data_btn_img = PhotoImage(file=relative_to_assets("del_crim_data.png"))
del_miss_person_data_btn_img = PhotoImage(file=relative_to_assets("del_miss_person_data.png"))
search_img = PhotoImage(file=relative_to_assets("search_img.png"))
search_entry = PhotoImage(file=relative_to_assets("search_entry.png"))
back_white_btn_img = PhotoImage(file=relative_to_assets("back_white.png"))

canvas_main_act = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_main_act.create_rectangle(
    0.0,
    107.0,
    338.0,
    940.0,
    fill="#1B293E",
    outline="")

canvas_main_act.create_rectangle(
    -1.999267578125,
    110.0,
    338.002197265625,
    112.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    209.0,
    338.00146484375,
    211.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    308.0,
    338.00146484375,
    310.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    407.0,
    338.00146484375,
    409.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    506.0,
    338.00146484375,
    508.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    605.0,
    338.00146484375,
    607.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    -2.0,
    704.0,
    338.00146484375,
    706.0,
    fill="#EAEAEA",
    outline="")

canvas_main_act.create_rectangle(
    1.0,
    803.0,
    341.00146484375,
    805.0,
    fill="#EAEAEA",
    outline="")

view_cit_data_btn = Button(
    canvas_main_act,
    image=view_cit_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_vcd,
    relief="flat"
)
view_cit_data_btn.place(
    x=13.0,
    y=120.0,
    width=310.0,
    height=80.0
)
view_crime_data_btn = Button(
    canvas_main_act,
    image=view_crime_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_vcmd,
    relief="flat"
)
view_crime_data_btn.place(
    x=14.0,
    y=716.0,
    width=310.0,
    height=80.0
)
view_miss_person_data_btn = Button(
    canvas_main_act,
    image=view_miss_person_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_vmd,
    relief="flat"
)
view_miss_person_data_btn.place(
    x=17.0,
    y=816.0,
    width=310.0,
    height=55.0
)
insert_crim_data_btn = Button(
    canvas_main_act,    
    image=insert_crim_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_icd,
    relief="flat"
)
insert_crim_data_btn.place(
    x=13.0,
    y=221.0,
    width=310.0,
    height=80.0
)
view_alert_hist_btn = Button(
    canvas_main_act,
    image=view_alert_hist_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_va,
    relief="flat"
)
view_alert_hist_btn.place(
    x=13.0,
    y=617.0,
    width=310.0,
    height=80.0
)
insert_miss_person_data_btn = Button(
    canvas_main_act,
    image=insert_miss_person_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_imd,
    relief="flat"
)
insert_miss_person_data_btn.place(
    x=13.0,
    y=318.0,
    width=310.0,
    height=80.0
)
del_crim_data_btn = Button(
    canvas_main_act,
    image=del_crim_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_dcd,
    relief="flat"
)
del_crim_data_btn.place(
    x=17.0,
    y=418.0,
    width=310.0,
    height=80.0
)
del_miss_person_data_btn = Button(
    canvas_main_act,
    image=del_miss_person_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_dmd,
    relief="flat"
)
del_miss_person_data_btn.place(
    x=14.0,
    y=517.0,
    width=310.0,
    height=80.0
)
canvas_main_act.create_rectangle(
    930.0,
    63.0,
    1450.0,
    98.0,
    fill="#F5F5F5",
    outline="")
canvas_main_act.create_rectangle(
    343.0,
    113.0,
    1500.0,
    935.0,
    fill="#D9D9D9",
    outline="")
canvas_main_act.create_image(
    1189.0,
    80.0,
    image=search_entry
)
canvas_main_act.create_image(
    56.0,
    54.0,
    image=police_img
)
canvas_main_act.create_image(
    187.0,
    55.0,
    image=safe_city_img
)

back_white_btn = Button(
    canvas_main_act,
    image=back_white_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_from_main_act,
    relief="flat"
)
back_white_btn.place(
    x=0.0,
    y=880.0,
    width=71.0,
    height=49.0
)
#----------------------------------------------------------



#----------------------------------------------------------
# Functions

use_ai_btn_img = PhotoImage(file=relative_to_assets("ai_btn.png"))
manipulate_data_btn_img = PhotoImage(file=relative_to_assets("data_man.png"))
complain_btn_img = PhotoImage(file=relative_to_assets("complain.png"))
func_back_btn_img = PhotoImage(file=relative_to_assets("func_back.png"))

canvas_functions = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
use_ai_btn = Button(
    canvas_functions,
    image=use_ai_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_ai_main_act,
    relief="flat"
)
use_ai_btn.place(
    x=128.0,
    y=243.0,
    width=371.0,
    height=573.0
)
manipulate_data_btn = Button(
    canvas_functions,
    image=manipulate_data_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_main_act,
    relief="flat"
)
manipulate_data_btn.place(
    x=567.0,
    y=287.0,
    width=373.0,
    height=569.0
)
complain_btn = Button(
    canvas_functions,
    image=complain_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("complain"),
    relief="flat"
)
complain_btn.place(
    x=1008.0,
    y=243.0,
    width=371.0,
    height=566.0
)
func_back_btn = Button(
    canvas_functions,
    image=func_back_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command = go_back_from_func,
    relief="flat"
)
func_back_btn.place(
    x=9.0,
    y=853.0,
    width=76.0,
    height=75.0
)

#---------------------------------------------------------


#----------------------------------------------------------
# AI_main activity

translation_service_act_btn_img = PhotoImage(file=relative_to_assets("translation_s.png"))
summarise_act_btn_img = PhotoImage(file=relative_to_assets("sum.png"))
classify_data_act_btn_img = PhotoImage(file=relative_to_assets("classify.png"))

canvas_ai_main_act = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_ai_main_act.create_rectangle(
    0.0,
    107.0,
    338.0,
    940.0,
    fill="#1B293E",
    outline="")

canvas_ai_main_act.create_rectangle(
    -1.999267578125,
    110.0,
    338.002197265625,
    112.0,
    fill="#EAEAEA",
    outline="")

canvas_ai_main_act.create_rectangle(
    -2.0,
    209.0,
    338.00146484375,
    211.0,
    fill="#EAEAEA",
    outline="")

canvas_ai_main_act.create_rectangle(
    -2.0,
    308.0,
    338.00146484375,
    310.0,
    fill="#EAEAEA",
    outline="")

canvas_ai_main_act.create_rectangle(
    -2.0,
    407.0,
    338.00146484375,
    409.0,
    fill="#EAEAEA",
    outline="")

translation_service_btn = Button(
    canvas_ai_main_act,
    image=translation_service_act_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_translation_service,
    relief="flat"
)
translation_service_btn.place(
    x=13.0,
    y=120.0,
    width=310.0,
    height=80.0
)
summarise_act_btn = Button(
    canvas_ai_main_act,
    image=summarise_act_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_summarize_document,
    relief="flat"
)
summarise_act_btn.place(
    x=13.0,
    y=222.0,
    width=300.0,
    height=80.0
)
classify_data_act_btn = Button(
    canvas_ai_main_act,
    image=classify_data_act_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("classify data"),
    relief="flat"
)
classify_data_act_btn.place(
    x=13.0,
    y=318.0,
    width=310.0,
    height=80.0
)
ai_main_act_textarea = Text(
    canvas_ai_main_act,
    bd=0,
    bg="#1B293E",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Raleway", "15"),
    state=tk.DISABLED
)
ai_main_act_textarea.place(
    x=7.0,
    y=490.0,
    width=322.0,
    height=360.0
)
ai_back_white_btn = Button(
    canvas_ai_main_act,
    image=back_white_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_from_ai_main_act,
    relief="flat"
)
ai_back_white_btn.place(
    x=0.0,
    y=880.0,
    width=71.0,
    height=49.0
)
canvas_ai_main_act.create_text(
    85.0,
    442.0,
    anchor="nw",
    text="Today’s headline",
    fill="#F7F7F7",
    font=("RalewayRoman", "16")
)

#----------------------------------------------------------

#----------------------------------------------------------
# ai how can i help

ai_how_img = PhotoImage(file=relative_to_assets("ai_how.png"))

canvas_ai_how_can_i_help = Canvas(
    window,
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_ai_how_can_i_help.create_image(
    578.0,
    409.0,
    image=ai_how_img
)

#-----------------------------------------------------------

#-----------------------------------------------------------
# Translation service

ts_img = PhotoImage(file=relative_to_assets("ts.png"))
ts_choose_btn_img = PhotoImage(file=relative_to_assets("ts_choose.png"))
ts_translate_btn_img = PhotoImage(file=relative_to_assets("ts_translate.png"))
ts_download_btn_img = PhotoImage(file=relative_to_assets("ts_down.png"))
ts_clear_btn_img = PhotoImage(file=relative_to_assets("ts_clear.png"))

canvas_translate_service = Canvas(
    window,
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_translate_service.create_image(
    578.0,
    412.0,
    image=ts_img
)
ts_choose_btn = Button(
    canvas_translate_service,
    image=ts_choose_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=ts_choose_file,
    relief="flat"
)
ts_choose_btn.place(
    x=874.0,
    y=600.0,
    width=198.4853515625,
    height=58.14111328125
)
ts_translate_btn = Button(
    canvas_translate_service,
    image=ts_translate_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=ts_translate_text,
    relief="flat"
)
ts_translate_btn.place(
    x=874.0,
    y=658.14111328125,
    width=201.47760009765625,
    height=58.14111328125
)
ts_download_btn = Button(
    canvas_translate_service,
    image=ts_download_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=ts_download,
    relief="flat"
)
ts_download_btn.place(
    x=877.9896240234375,
    y=716.2822265625,
    width=198.4853515625,
    height=64.15570068359375
)
ts_textarea = Text(
    canvas_translate_service,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Raleway", "13")
)
ts_textarea.place(
    x=45.0,
    y=299.0,
    width=741.0,
    height=479.0
)

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(
    canvas_translate_service,
    textvariable=dropdown_var,
    values=["English", "Hindi", "Marathi", "Telugu", "Bengali", "Tamil", "Gujarati", "Kannada", "Punjabi", "Malayalam", "Urdu"],
    font=("Raleway", "14")
)
dropdown.place(
    x=835.83,
    y=527.28,
    width=276.0,
    height=31.08
)
ts_clear_btn = Button(
    canvas_translate_service,
    image=ts_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=ts_clear,
    relief="flat"
)
ts_clear_btn.place(
    x=730.0,
    y=280.0,
    width=48.0,
    height=19.0
)
saved_notification = canvas_translate_service.create_text(
    50.0,
    800.0,
    anchor="nw",
    text="",
    fill="#74B72E",
    font=("RalewayRoman", "14")
)

#------------------------------------------------------------
# Summarize documents

sd_img = PhotoImage(file=relative_to_assets("sd.png"))
sd_summarize_btn_img = PhotoImage(file=relative_to_assets("sd_sum.png"))
sd_down_btn_img = PhotoImage(file=relative_to_assets("sd_down.png"))

canvas_summarize_document = Canvas(
    window,
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_summarize_document.create_image(
    578.0,
    412.0,
    image=sd_img
)
sd_textarea = Text(
    canvas_summarize_document,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Raleway", "13")
)
sd_textarea.place(
    x=45.0,
    y=306.0,
    width=741.0,
    height=472.0
)
sd_summarize_btn = Button(
    canvas_summarize_document,
    image=sd_summarize_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=sd_summarize_text,
    relief="flat"
)
sd_summarize_btn.place(
    x=868.0,
    y=609.0,
    width=201.47760009765625,
    height=58.14111328125
)
sd_clear_btn = Button(
    canvas_summarize_document,
    image=ts_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=sd_clear,
    relief="flat"
)
sd_clear_btn.place(
    x=730.0,
    y=280.0,
    width=48.0,
    height=19.0
)
sd_choose_btn = Button(
    canvas_summarize_document,
    image=ts_choose_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=sd_choose_file,
    relief="flat"
)
sd_choose_btn.place(
    x=868.0,
    y=529.0,
    width=198.4853515625,
    height=58.14111328125
)
sd_download_btn = Button(
    canvas_summarize_document,
    image=sd_down_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=sd_download,
    relief="flat"
)
sd_download_btn.place(
    x=872.0,
    y=689.0,
    width=198.0,
    height=71.0
)

#-------------------------------------------------------------


#-----------------------------------------------------------
# NAV
canvas_nav = Canvas(
    window, 
    bg = "#1B293E",
    height=110,
    width=1508,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_nav.create_rectangle(
    0.0,
    0.0,
    1508.0,
    110.0,
    fill="#1B293E",
    outline="")
canvas_nav.create_image(
    56.0,
    54.0,
    image=police_img
)
canvas_nav.create_image(
    187.0,
    55.0,
    image=safe_city_img
)
ppsu_logo_img = canvas_nav.create_image(
    1449.0,
    59.0,
    image=ppsu_logo
)
search = Entry(
    canvas_nav,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
canvas_nav.place(x=0, y=0)

#---------------------------------------------------------------



#---------------------------------------------------------------
# How can i help you image

how_can_i_help_img = PhotoImage(file=relative_to_assets("how.png"))

canvas_how_can_i_help = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_how_can_i_help.create_image(
    578.0,
    411.0,
    image=how_can_i_help_img
)

#---------------------------------------------------------------
# View citizen data page

vcd_img = PhotoImage(file=relative_to_assets("vcd.png"))

canvas_view_citizen_data = Canvas(
    window, 
    bg = "#1A1A1A",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_view_citizen_data.create_image(
    578.0,
    411.0,
    image=vcd_img
)
vcd_textarea = Text(
    canvas_view_citizen_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
vcd_textarea.place(
    x=78.0,
    y=229.0,
    width=1003.0,
    height=507.0
)

#------------------------------------------------------
# Insert criminal data page

icd_img = PhotoImage(file=relative_to_assets("icd.png"))
i_select_btn_img = PhotoImage(file=relative_to_assets("i_select.png"))
i_insert_btn_img = PhotoImage(file=relative_to_assets("i_insert.png"))
i_clear_btn_img = PhotoImage(file=relative_to_assets("i_clear.png"))


canvas_insert_criminal_data = Canvas(
    window,
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_insert_criminal_data.create_image(
    578.0,
    410.0,
    image=icd_img
)
icd_select_btn = Button(
    canvas_insert_criminal_data,
    image=i_select_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=select_image_criminal,
    relief="flat"
)
icd_select_btn.place(
    x=262.0,
    y=624.0,
    width=122.0,
    height=30.0
)
icd_insert_btn = Button(
    canvas_insert_criminal_data,
    image=i_insert_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=icd_insert,
    relief="flat"
)
icd_insert_btn.place(
    x=69.0,
    y=741.0,
    width=181.0,
    height=48.0
)
icd_clear_btn = Button(
    canvas_insert_criminal_data,
    image=i_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=icd_clear,
    relief="flat"
)
icd_clear_btn.place(
    x=265.0,
    y=741.0,
    width=177.0,
    height=48.0
)
icd_gender = Entry(
    canvas_insert_criminal_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
icd_gender.place(
    x=104.00616455078125,
    y=426.0,
    width=354.0,
    height=23.79962730407715
)
icd_age = Entry(
    canvas_insert_criminal_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
icd_age.place(
    x=104.0,
    y=351.0,
    width=354.0,
    height=23.79962921142578
)
icd_last_name = Entry(
    canvas_insert_criminal_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
icd_last_name.place(
    x=104.0,
    y=276.0,
    width=354.0,
    height=23.79962158203125
)
icd_first_name = Entry(
    canvas_insert_criminal_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
icd_first_name.place(
    x=104.0,
    y=211.0,
    width=354.0,
    height=23.79962158203125
)
icd_textarea = Text(
    canvas_insert_criminal_data,
    bd=0,
    bg="#E7E7E7",
    fg="#000716",
    highlightthickness=0
)
icd_textarea.place(
    x=104.0,
    y=506.0,
    width=354.0,
    height=70.0
)

#-------------------------------------------------------



#-------------------------------------------------------
# Insert missing person data

imd_img = PhotoImage(file=relative_to_assets("imd.png"))


canvas_insert_missing_data = Canvas(
    window,
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_insert_missing_data.create_image(
    578.0,
    410.0,
    image=imd_img
)
imd_select_btn = Button(
    canvas_insert_missing_data,
    image=i_select_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("insert missing select"),
    relief="flat"
)
imd_select_btn.place(
    x=262.0,
    y=624.0,
    width=122.0,
    height=30.0
)
imd_insert_btn = Button(
    canvas_insert_missing_data,
    image=i_insert_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=imd_insert,
    relief="flat"
)
imd_insert_btn.place(
    x=69.0,
    y=741.0,
    width=181.0,
    height=48.0
)
imd_clear_btn = Button(
    canvas_insert_missing_data,
    image=i_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=imd_clear,
    relief="flat"
)
imd_clear_btn.place(
    x=265.0,
    y=741.0,
    width=177.0,
    height=48.0
)
imd_gender = Entry(
    canvas_insert_missing_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
imd_gender.place(
    x=104.00616455078125,
    y=426.0,
    width=354.0,
    height=23.79962730407715
)
imd_age = Entry(
    canvas_insert_missing_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
imd_age.place(
    x=104.0,
    y=351.0,
    width=354.0,
    height=23.79962921142578
)
imd_last_name = Entry(
    canvas_insert_missing_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
imd_last_name.place(
    x=104.0,
    y=276.0,
    width=354.0,
    height=23.79962158203125
)
imd_first_name = Entry(
    canvas_insert_missing_data,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
imd_first_name.place(
    x=104.0,
    y=211.0,
    width=354.0,
    height=23.79962158203125
)
imd_textarea = Text(
    canvas_insert_missing_data,
    bd=0,
    bg="#E7E7E7",
    fg="#000716",
    highlightthickness=0
)
imd_textarea.place(
    x=104.0,
    y=506.0,
    width=354.0,
    height=70.0
)

#-------------------------------------------------------



#-------------------------------------------------------
# View missing person data

vmd_img = PhotoImage(file=relative_to_assets("vmd.png"))

canvas_view_missing_data = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_view_missing_data.create_image(
    578.0,
    410.0,
    image=vmd_img
)
vmd_textarea = Text(
    canvas_view_missing_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
vmd_textarea.place(
    x=78.0,
    y=229.0,
    width=1003.0,
    height=507.0
)

#-------------------------------------------------------


#-------------------------------------------------------
# View alert history

va_img = PhotoImage(file=relative_to_assets("va.png"))

canvas_view_alerts = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_view_alerts.create_image(
    578.0,
    411.0,
    image=va_img
)
vmd_textarea = Text(
    canvas_view_alerts,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
vmd_textarea.place(
    x=78.0,
    y=229.0,
    width=1003.0,
    height=507.0
)

#-------------------------------------------------------


#-------------------------------------------------------
# View criminal data

vcmd_img = PhotoImage(file=relative_to_assets("vcmd.png"))

canvas_view_crim_data = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_view_crim_data.create_image(
    578.0,
    411.0,
    image=vcmd_img
)
vcmd_textarea = Text(
    canvas_view_crim_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
vcmd_textarea.place(
    x=78.0,
    y=229.0,
    width=1003.0,
    height=507.0
)


#-------------------------------------------------------



#-------------------------------------------------------
# Delete criminal data

dcd_img = PhotoImage(file=relative_to_assets("dcd.png"))
dmd_del_btn_img = PhotoImage(file=relative_to_assets("dcd_del.png"))

canvas_del_crim_data = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_del_crim_data.create_image(
    578.0,
    410.0,
    image=dcd_img
)

dcd_btn = Button(
    canvas_del_crim_data,
    image=dmd_del_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("dmd del"),
    relief="flat"
)
dcd_btn.place(
    x=32.0,
    y=579.0,
    width=157.0,
    height=46.0
)
dcd_del_id = Entry(
    canvas_del_crim_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "12")
)
dcd_del_id.place(
    x=298.0,
    y=517.0,
    width=175.0,
    height=31.0
)
dcd_textarea = Text(
    canvas_del_crim_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
dcd_textarea.place(
    x=57.0,
    y=204.0,
    width=582.0,
    height=135.0
)


#-------------------------------------------------------



#-------------------------------------------------------
# Delete missing person data

dmd_img = PhotoImage(file=relative_to_assets("dmd.png"))

canvas_del_missing_data = Canvas(
    window, 
    bg = "#F5F5F5",
    height = 824,
    width = 1157,
    bd= 0,
    highlightthickness=0,
    relief="ridge"
)
canvas_del_missing_data.create_image(
    578.0,
    410.0,
    image=dmd_img
)

dmd_btn = Button(
    canvas_del_missing_data,
    image=dmd_del_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("dmd del"),
    relief="flat"
)
dmd_btn.place(
    x=32.0,
    y=579.0,
    width=157.0,
    height=46.0
)
dmd_del_id = Entry(
    canvas_del_missing_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "12")
)
dmd_del_id.place(
    x=298.0,
    y=517.0,
    width=175.0,
    height=31.0
)
dmd_textarea = Text(
    canvas_del_missing_data,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
dmd_textarea.place(
    x=57.0,
    y=204.0,
    width=582.0,
    height=135.0
)

#-----------------------------------------------------------------
# alert pop - up

alert_bg = PhotoImage(file=relative_to_assets("alert_bg.png"))

canvas_alert = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_alert.create_image(
    750.0,
    470.0,
    image=alert_bg
)
criminal_details_textarea = Text(
    canvas_alert,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
criminal_details_textarea.place(
    x=272.0,
    y=307.0,
    width=416.0,
    height=543.0
)
citizen_details_textarea = Text(
    canvas_alert,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
citizen_details_textarea.place(
    x=772.0,
    y=689.0,
    width=490.0,
    height=182.0
)

def go_back_from_alert():
    global msg_sent
    canvas_alert.place_forget()
    msg_sent = False

alert_back_btn = Button(
    canvas_alert,
    image=func_back_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command = go_back_from_alert,
    relief="flat"
)
alert_back_btn.place(
    x=9.0,
    y=853.0,
    width=76.0,
    height=75.0
)

#----------------------------------------------------

msg_sent = False
def message_callback(message):
    global msg_sent
    canvas_alert.place(x = 0, y = 0)
    lines = message.split('$')
    print(lines)
    if not msg_sent:
        criminal_details_textarea.insert(tk.END, lines[0])
        citizen_details_textarea.insert(tk.END, lines[1])
        msg_sent = True
    
def start_server():
    s_tk.accept_connections(message_callback)

def img_callback(img_path):
    img = Image.open(img_path)
    
    resized_img = Image.new("RGBA", (503, 305))
    
    # Calculate the position to paste the original image in the center
    x_offset = (600 - img.width) // 2
    y_offset = (450 - img.height) // 2
    
    # Paste the original image onto the new image
    resized_img.paste(img, (x_offset, y_offset))

    photo = ImageTk.PhotoImage(resized_img)

    detected_image = canvas_alert.create_image(
        990.0,
        405.0,
        image = photo
    )   
    canvas_alert.photo = photo

def start_photo_server():
    ps.start_server(img_callback)

# start the server and start the listener
#accept_thread = threading.Thread(target=s_tk.accept_connections, args=(message_callback))
photo_thread = threading.Thread(target = start_photo_server)
photo_thread.daemon = True
photo_thread.start()
accept_thread = threading.Thread(target = start_server)
accept_thread.daemon = True
accept_thread.start()
#----------------   ---------------------------------------
window.resizable(False, False)
window.mainloop()
