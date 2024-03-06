from pathlib import Path
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import verification 
import tkinter as tk
import cv2, face_recognition, threading
from PIL import Image, ImageTk
import newsc, bard_ai_c, datetime
import c_tk, firebase_cit, firebase_cit_data, math, pygame, time, pc
import numpy as np

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/anton/Desktop/new_code_cit/mainc")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def go_to_login_page():
    canvas_login.place(x = 0, y = 0)
    canvas_home.place_forget()

def go_to_create_acc():
    canvas_login.delete(verify_notification)
    login_username.delete(0, 'end')
    login_password.delete(0, 'end')
    canvas_registration.place(x = 0, y = 110)

def go_back_to_login():
    canvas_registration.place_forget()
    canvas_login.place(x = 0, y = 0)

def go_back_to_home():
    global verify_notification
    canvas_home.place(x = 0, y = 0)
    canvas_login.itemconfig(verify_notification, text = "")
    canvas_login.place_forget()

logged_in_username = ''
logged_in_password = ''
def go_to_func():
    global verify_notification, logged_in_username, logged_in_password
    canvas_login.delete(verify_notification)
    if login_username.get() != '' and login_password.get() != '':
        if(firebase_cit_data.check_citizen_login(login_username.get(), login_password.get())):
            canvas_function.place(x = 0, y = 0)
            canvas_login.place_forget()
            logged_in_username = login_username.get()
            logged_in_password = login_password.get()
            login_username.delete(0, 'end')
            login_password.delete(0, 'end')
        else:
            verify_notification = canvas_login.create_text(
                760.0,
                115.0,
                anchor="nw",
                text="No such user found!",
                fill="#000000",
                font=("Raleway", "14")
            )
    else:
        verify_notification = canvas_login.create_text(
                760.0,
                115.0,
                anchor="nw",
                text="Please fill up the login username and password before logging in..",
                fill="#000000",
                font=("Raleway", "14")
            )

def go_back_from_func():
    canvas_login.place(x = 0, y = 0)
    canvas_function.place_forget()

def go_to_cam():
    canvas_camera.place(x = 0, y = 0)
    canvas_function.place_forget()

def go_back_cam():
    global webcam_on, webcam_off
    canvas_function.place(x = 0, y = 0)
    if webcam_on:
        stop_webcam()
    canvas_camera.place_forget()

id = 0
def set_news_on_textarea(id):
    news_text = newsc.get_latest_news(id)
    news_textarea.config(state=tk.NORMAL)
    news_textarea.delete(1.0, 'end')
    news_textarea.insert(tk.END, news_text)
    news_textarea.config(state=tk.DISABLED)

def go_to_file_complaint():
    global id
    canvas_file_complaint_super.place(x = 0, y = 0)
    canvas_how_can_i_help.place(x = 340, y = 114)
    canvas_function.place_forget()
    window.after(300, set_news_on_textarea, id)
    id += 1

def go_back_file_complaint():
    canvas_function.place(x = 0, y = 0)
    canvas_file_complaint_super.place_forget()
    canvas_file_complaint_sub.place_forget()
    canvas_how_can_i_help.place_forget()
    canvas_use_ai.place_forget()

def go_to_report_complaint_sub():
    canvas_file_complaint_sub.place(x = 340, y = 114)
    canvas_how_can_i_help.place_forget()
    canvas_use_ai.place_forget()

def clear_sub():
    file_textarea.delete(1.0, 'end')

def ai_clear():
    ai_textarea.delete(1.0, 'end')

def go_to_use_ai():
    canvas_use_ai.place(x = 340, y = 114)
    canvas_file_complaint_sub.place_forget()
    canvas_how_can_i_help.place_forget()

ind_searches = 0
def place_answer(entered_search):
    global ind_searches, responding_text
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    answer = str(ind_searches + 1) + "] Time : " + cur_time + "\nPrompt : " + entered_search + "\n\n" + bard_ai_c.bard_answer(entered_search) + "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"
    ind_searches += 1
    ai_textarea.insert(tk.END, answer)
    canvas_use_ai.delete(responding_text)


def fire_prompt(event):
    global responding_text
    responding_text = canvas_use_ai.create_text(
        40.0,
        800.0,
        anchor="nw",
        text="Responding to the prompt, wait...",
        fill="#000000",
        font=("RalewayRoman", "14")
    )
    entered_search = search_bar.get()
    add_search_history()
    search_bar.delete(0, 'end')
    window.after(300, place_answer, entered_search)

search_history = []
def add_search_history():
    global search_history
    entered_search = search_bar.get()
    if entered_search:
        current_searches = search_history
        if entered_search not in current_searches:
            search_history.append(entered_search)
            dropdown.configure(values=search_history)

def fire_selected_search_history(event):
    selected_search = dropdown.get()
    search_bar.delete(0, 'end')
    search_bar.insert(0, selected_search)

img_path = ''
def attach_photos():
    global img_path
    img_path = filedialog.askopenfilename(title = 'Open file to be read', initialdir='/home/anton/Pictures/', filetypes = [("Photos", "*.png *.jpg *.jpeg")])

def send():
    pass

def registration(): 
    global verify_notification
    canvas_login.itemconfig(verify_notification, text = "")

    retrieved_firstname = firstname.get()
    retrieved_lastname = lastname.get()
    retrieved_email = email.get()
    retrieved_email_pass = email_pass.get()
    retrieved_postal = postal.get()
    retrieved_mobile = mobile.get()
    retrieved_username = username.get()
    retrieve_password = password.get()
    retrieve__confirm_password = confirm_pass.get()
    retrieve_address = address.get(1.0, 'end')
    
    if retrieved_firstname != '' and retrieved_lastname != '' and retrieved_email != '' and retrieved_email_pass != '' and retrieved_postal != '' and retrieved_mobile != '' and retrieved_username != '' and  retrieve_password != '' and retrieve__confirm_password != '' and retrieve_address != '' and retrieve__confirm_password == retrieve_password:
        msg, status, verification_code = verification.send_verification_email(firstname.get(), lastname.get(), email.get())
        if status:
            verification_window = tk.Toplevel(window)
            verification_window.title("SafeCity : Verify the code")
            tk.Label(verification_window, text="Enter your verification code here..").pack()
            user_input = tk.Entry(verification_window)
            user_input.pack()
            verify_button = tk.Button(verification_window, text="Verify", command=lambda: return_user_input(user_input.get(), verification_window, verification_code))
            verify_button.pack()
        else:
            print("something went wrong while sending an email")

def return_user_input(input_value, input_dialog, verification_code):
    global verify_notification
    canvas_login.itemconfig(verify_notification, text = "")

    if input_value == verification_code:
        firebase_cit_data.insert_citizen_registered_data(firstname.get(), lastname.get(), email.get(), email_pass.get(), address.get(1.0, 'end'), postal.get(), mobile.get(), username.get(), password.get())
        reg_clear()
        verify_notification = canvas_login.create_text(
            760.0,
            115.0,
            anchor="nw",
            text="Verified the code successfully, registration completed. \nLogin to your account to go further.",
            fill="#000000",
            font=("Raleway", "14")
        )
        canvas_registration.place_forget()
    else:
        print("not verified")
        verify_notification = canvas_login.create_text(
            760.0,
            115.0,
            anchor="nw",
            text="Sorry, the given verification code does not match. Try again!",
            fill="#000000",
            font=("Raleway", "14")
        )
    input_dialog.destroy()             
    
def reg_clear():
    firstname.delete(0, 'end')
    lastname.delete(0, 'end')
    email.delete(0, 'end')
    email_pass.delete(0, 'end')
    postal.delete(0, 'end')
    mobile.delete(0, 'end')
    username.delete(0, 'end')
    password.delete(0, 'end')
    confirm_pass.delete(0, 'end')
    address.delete(1.0, 'end')

pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sine_x(amp, freq, time):
    return int(amp * math.sin(2 * math.pi * freq * time))

class Tone:
    def sine(freq, duration=1, speaker=None):
        num_samples = int(round(duration * sample_rate))
        sound_buffer = np.zeros((num_samples, 2), dtype = np.int16)
        amplitude = 2 ** (bits - 1) - 1

        for sample_num in range(num_samples):
            t = float(sample_num) / sample_rate
            sine = sine_x(amplitude, freq, t)

            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            if speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine
        
        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops = 1, maxtime=int(duration * 1000))
        time.sleep(duration)

ENCODED_CRIMINAL_IMAGES = []
DETECTED_CRIMINALS = []
fetched_images = False
def recognise(frame):
    global ENCODED_CRIMINAL_IMAGES, DETECTED_CRIMINALS, fetched_images, logged_in_username, logged_in_password
    
    if not fetched_images:
        ENCODED_CRIMINAL_IMAGES = firebase_cit.retrieve_criminal_encoded_imgs()
        fetched_images = True

    if len(ENCODED_CRIMINAL_IMAGES) == 0:
        print("No images inserted")
        return
    
    face_location = face_recognition.face_locations(frame)
    encoded_frame = face_recognition.face_encodings(frame, face_location)

    for encoded in encoded_frame:
        if len(encoded) != 0:
            match = face_recognition.compare_faces(ENCODED_CRIMINAL_IMAGES, encoded)
            match_dist = face_recognition.face_distance(ENCODED_CRIMINAL_IMAGES, encoded)
            min_dist_ind = np.argmin(match_dist) 

            if match[min_dist_ind]: # TO_DO (make it faster)
                FIRSTNAME, LASTNAME, AGE, GENDER, DESC = firebase_cit.get_criminal_data(min_dist_ind)
                CIT_ADDR, CIT_POSTAL, CIT_MOBILE, CIT_FIRSTNAME, CIT_LASTNAME = firebase_cit_data.alert_citizen_details(logged_in_username, logged_in_password) 
                
                Tone.sine(800, 0.4)
                Tone.sine(800, 0.4)
                crim_message = f"Criminal Detected \nCriminal's Details given below : \nFirst-name : {FIRSTNAME} \nLast-name : {LASTNAME} \nAge : {AGE} \nGender : {GENDER} \nDescription : {DESC} \n"
                cit_message = f"Detail's of citizen through which detected: \nName of citizen : {CIT_FIRSTNAME} {CIT_LASTNAME} \nAddress of citizen where detected : {CIT_ADDR} \nPostal : {CIT_POSTAL} \nCitizen's registered mobile number : {CIT_MOBILE} \n\n"
                
                RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pc.send_photo(RGB_frame)
                c_tk.send_message("\n" + crim_message + '$' + cit_message)

                if (FIRSTNAME + " " + LASTNAME) not in DETECTED_CRIMINALS:
                    cam_textarea.insert(tk.END, f"\n{crim_message} - An alert message has been sent to the police, make sure to keep yourself safe for a while \n------------------------------------------------------------------------------------------------------------\n")
                    DETECTED_CRIMINALS.append(FIRSTNAME + " " + LASTNAME)

webcam_on , webcam_off = False, True 
cam_url = 'http://192.168.1.5:8080/shot.jpg'
def start_webcam():
    global cap, update_id, webcam_on, webcam_off
    cap = cv2.VideoCapture(0)
    webcam_on = True
    webcam_off = False
    update_id = canvas_camera.after(10, update_webcam)

counter = 0
def update_webcam():
    global cap, update_id, counter
    ret, frame = cap.read()

    if frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if counter % 30 == 0:
            recognise(frame)

        frame = cv2.resize(frame, (806, 700))
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image = img)
        canvas_camera.create_image(423, 480, image = photo)
        canvas_camera.image = photo
        counter += 1
        update_id = canvas_camera.after(30, update_webcam)

def stop_webcam():
    global cap, update_id, webcam_on, webcam_off, fetched_images
    if cap is not None:
        cap.release()
        canvas_camera.after_cancel(update_id)
        #res_img = Image.open(relative_to_assets("webcam.png"))
        canvas_camera.create_image(
            423,
            480,
            image=web_img
        )
        webcam_on = False
        webcam_off = True
        fetched_images = False

window = Tk()
window.title("SafeCity For Citizen)")
window.geometry("1500x940")
window.configure(bg = "#F5F5F5")

#---------------------------------------

#---------------------------------------
# HOME

title_img = PhotoImage(file=relative_to_assets("title.png"))
desc_img = PhotoImage(file=relative_to_assets("desc.png"))
get_started_btn_img = PhotoImage(file=relative_to_assets("get.png"))
home_pol_img = PhotoImage(file=relative_to_assets("home_pol.png"))

canvas_home = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_home.create_image(
    187.0,
    55.0,
    image=title_img
)
image_2 = canvas_home.create_image(
    1164.0,
    469.0,
    image=desc_img
)

get_started_btn = Button(
    canvas_home,
    image=get_started_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_login_page,
    relief="flat"
)
get_started_btn.place(
    x=921.0,
    y=681.0,
    width=198.0,
    height=62.0
)

canvas_home.create_image(
    421.0,
    518.0,
    image=home_pol_img
)
canvas_home.place(x = 0, y = 0)

#---------------------------------------------------

# LOGIN

login_img = PhotoImage(file=relative_to_assets("login.png"))
create_acc_btn_img = PhotoImage(file=relative_to_assets("create.png"))
forgot_pass_btn_img = PhotoImage(file=relative_to_assets("forgot.png"))
login_btn_img = PhotoImage(file=relative_to_assets("login_btn.png"))
back_blue_btn_img = PhotoImage(file=relative_to_assets("back_blu.png"))

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
    750.0,
    470.0,
    image=login_img
)
create_acc_btn = Button(
    canvas_login,
    image=create_acc_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_create_acc,
    relief="flat"
)
create_acc_btn.place(
    x=82.0,
    y=630.0,
    width=229.0,
    height=29.0
)
forgot_pass_btn = Button(
    canvas_login,
    image=forgot_pass_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("forgot pass"),
    relief="flat"
)
forgot_pass_btn.place(
    x=86.0,
    y=667.0,
    width=166.0,
    height=31.0
)
login_btn = Button(
    canvas_login,
    image=login_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_func,
    relief="flat"
)
login_btn.place(
    x=188.0,
    y=768.0,
    width=332.0,
    height=72.0
)
login_username = Entry(
    canvas_login,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14")
)
login_username.place(
    x=124.0,
    y=386.0,
    width=479.0,
    height=42.0
)
login_password = Entry(
    canvas_login,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "14"),
    show = "*"
)
login_password.place(
    x=124.0,
    y=516.0,
    width=479.0,
    height=42.0
)
login_back_btn = Button(
    canvas_login,
    image=back_blue_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_to_home,
    relief="flat"
)
login_back_btn.place(
    x=-8.0,
    y=871.0,
    width=84.0,
    height=69.0
)
verify_notification = canvas_login.create_text(
    760.0,
    115.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Raleway", "14")
)
#---------------------------------------------------
# REGISTRATION


reg_bg = PhotoImage(file=relative_to_assets("reg_bg.png"))
reg_btn_img = PhotoImage(file=relative_to_assets("reg_reg.png"))
reg_clear_btn_img = PhotoImage(file=relative_to_assets("reg_clear.png"))

canvas_registration = Canvas(
    window,
    bg = "#F5F5F5",
    height = 830,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_registration.create_image(
    375.0,
    415.0,
    image=reg_bg
)
firstname = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
firstname.place(
    x=59.0,
    y=165.0,
    width=264.0,
    height=26.0
)
lastname= Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
lastname.place(
    x=59.0,
    y=250.0,
    width=264.0,
    height=26.0
)
email = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
email.place(
    x=59.0,
    y=335.0,
    width=264.0,
    height=26.0
)
email_pass = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    show = "*",
    font = ("Raleway", "13")
)
email_pass.place(
    x=59.0,
    y=420.0,
    width=264.0,
    height=26.0
)
postal = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
postal.place(
    x=395.0,
    y=165.0,
    width=264.0,
    height=26.0
)
mobile = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
mobile.place(
    x=395.0,
    y=250.0,
    width=264.0,
    height=26.0
)
username = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
username.place(
    x=395.0,
    y=335.0,
    width=264.0,
    height=26.0
)
password = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
password.place(
    x=395.0,
    y=420.0,
    width=264.0,
    height=26.0
)
confirm_pass = Entry(
    canvas_registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "13")
)
confirm_pass.place(
    x=395.0,
    y=505.0,
    width=264.0,
    height=26.0
)
address = Text(
    canvas_registration,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Raleway", "12")
)
address.place(
    x=61.0,
    y=517.0,
    width=262.0,
    height=98.0
)
reg_btn = Button(
    canvas_registration,
    image=reg_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=registration,
    relief="flat"
)
reg_btn.place(
    x=194.0,
    y=672.0,
    width=332.0,
    height=72.0
)
reg_clear_btn = Button(
    canvas_registration,
    image=reg_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=reg_clear,
    relief="flat"
)
reg_clear_btn.place(
    x=305.0,
    y=757.0,
    width=105.0,
    height=36.0
)
reg_back_btn = Button(
    canvas_registration,
    image=back_blue_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_to_login,
    relief="flat"
)
reg_back_btn.place(
    x=-8.0,
    y=761.0,
    width=84.0,
    height=69.0
)
#--------------------------------------------------
# FUNCTION

func = PhotoImage(file=relative_to_assets("func.png"))
cam_btn_img = PhotoImage(file=relative_to_assets("web_btn.png"))
complain_btn_img = PhotoImage(file=relative_to_assets("com.png"))

canvas_function = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_function.create_image(
    750.0,
    470.0,
    image=func
)
cam_btn = Button(
    canvas_function,
    image=cam_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_cam,
    relief="flat"
)
cam_btn.place(
    x=229.0,
    y=260.0,
    width=397.0,
    height=606.0
)
complain_btn = Button(
    canvas_function,
    image=complain_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_file_complaint,
    relief="flat"
)
complain_btn.place(
    x=857.0,
    y=256.0,
    width=415.0,
    height=625.0
)
func_back_btn = Button(
    canvas_function,
    image=back_blue_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_from_func,
    relief="flat"
)
func_back_btn.place(
    x=-8.0,
    y=871.0,
    width=84.0,
    height=69.0
)

#----------------------------------------------------
# CAMERA

cam_bg = PhotoImage(file=relative_to_assets("c.png"))
off_btn_img = PhotoImage(file=relative_to_assets("off.png"))
on_btn_img = PhotoImage(file=relative_to_assets("on.png"))
web_img = PhotoImage(file=relative_to_assets("webcam.png"))

canvas_camera = Canvas(
    window,
    bg = "#FFFFFF",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_camera.create_image(
    750.0,
    470.0,
    image=cam_bg
)
cam_textarea = Text(
    canvas_camera,
    bd=0,
    bg="#9E9E9E",
    fg="#000000",
    highlightthickness=0,
    font = ("Raleway", "12")
)
cam_textarea.place(
    x=864.0,
    y=410.0,
    width=570.0,
    height=292.0
)
off_btn = Button(
    canvas_camera,
    image=off_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=stop_webcam,
    relief="flat"
)
off_btn.place(
    x=1182.0,
    y=764.0,
    width=226.0,
    height=72.0
)
on_btn = Button(
    canvas_camera,
    image=on_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=start_webcam,
    relief="flat"
)
on_btn.place(
    x=903.0,
    y=764.0,
    width=226.0,
    height=72.0
)
cam_back_btn = Button(
    canvas_camera,
    image=back_blue_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_cam,
    relief="flat"
)
cam_back_btn.place(
    x=-8.0,
    y=871.0,
    width=84.0,
    height=69.0
)
#------------------------------------------------
# FILE COMPLAINT SUPER

file_complaint_btn_img = PhotoImage(file=relative_to_assets("file_c.png"))
use_ai_for_help_btn_img = PhotoImage(file=relative_to_assets("ai_c.png"))
response_btn_img = PhotoImage(file=relative_to_assets("r.png"))
back_white_btn_img = PhotoImage(file=relative_to_assets("back_white.png"))

canvas_file_complaint_super = Canvas(
    window,
    bg = "#F5F5F5",
    height = 940,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_file_complaint_super.create_rectangle(
    0.0,
    0.0,
    1508.0,
    110.0,
    fill="#1B293E",
    outline="")

canvas_file_complaint_super.create_rectangle(
    0.0,
    107.0,
    338.0,
    940.0,
    fill="#1B293E",
    outline="")

canvas_file_complaint_super.create_rectangle(
    -1.999267578125,
    110.0,
    338.002197265625,
    112.0,
    fill="#EAEAEA",
    outline="")

canvas_file_complaint_super.create_rectangle(
    -2.0,
    209.0,
    338.00146484375,
    211.0,
    fill="#EAEAEA",
    outline="")

canvas_file_complaint_super.create_rectangle(
    -2.0,
    308.0,
    338.00146484375,
    310.0,
    fill="#EAEAEA",
    outline="")

canvas_file_complaint_super.create_rectangle(
    -2.0,
    407.0,
    338.00146484375,
    409.0,
    fill="#EAEAEA",
    outline="")
file_complaint_btn = Button(
    canvas_file_complaint_super,
    image=file_complaint_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_report_complaint_sub,
    relief="flat"
)
file_complaint_btn.place(
    x=13.0,
    y=120.0,
    width=310.0,
    height=80.0
)
use_ai_for_help_btn = Button(
    canvas_file_complaint_super,
    image=use_ai_for_help_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_to_use_ai,
    relief="flat"
)
use_ai_for_help_btn.place(
    x=13.0,
    y=222.0,
    width=302.0,
    height=80.0
)
response_btn = Button(
    canvas_file_complaint_super,
    image=response_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("response"),
    relief="flat"
)
response_btn.place(
    x=13.0,
    y=318.0,
    width=310.0,
    height=80.0
)
news_textarea = Text(
    canvas_file_complaint_super,
    bd=0,
    bg="#1B293E",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Raleway", "13"),
    state="disabled"
)
news_textarea.place(
    x=7.0,
    y=490.0,
    width=322.0,
    height=370.0
)
back_white_btn = Button(
    canvas_file_complaint_super,
    image=back_white_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=go_back_file_complaint,
    relief="flat"
)
back_white_btn.place(
    x=-2.0,
    y=879.0,
    width=71.0,
    height=49.0
)

canvas_file_complaint_super.create_text(
    84.0,
    440.0,
    anchor="nw",
    text="Today’s headline",
    fill="#FFFFFF",
    font=("Raleway", "15", "bold")
)
#---------------------------------------------------
# HOW CAN I HELP

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


#----------------------------------------------------
# FILE COMPLAINT SUB

f_bg = PhotoImage(file=relative_to_assets("f_bg.png"))
send_btn_img = PhotoImage(file=relative_to_assets("send.png"))
attach_btn_img = PhotoImage(file=relative_to_assets("attach.png"))
add_btn_img = PhotoImage(file=relative_to_assets("add.png"))
file_clear_btn_img = PhotoImage(file=relative_to_assets("f_clear.png"))

canvas_file_complaint_sub = Canvas(
    window,
    bg = "#FFFFFF",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_file_complaint_sub.create_image(
    578.0,
    412.0,
    image=f_bg
)
send_btn = Button(
    canvas_file_complaint_sub,
    image=send_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=send,
    relief="flat"
)
send_btn.place(
    x=868.0,
    y=733.0,
    width=201.65008544921875,
    height=58.211761474609375
)
attach_btn = Button(
    canvas_file_complaint_sub,
    image=attach_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=attach_photos,
    relief="flat"
)
attach_btn.place(
    x=867.0,
    y=667.0,
    width=197.0,
    height=58.0
)
'''
add_btn = Button(
    canvas_file_complaint_sub,
    image=add_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=add,
    relief="flat"
)
add_btn.place(
    x=1011.0,
    y=669.0,
    width=133.0,
    height=48.0
)
'''
file_clear_btn = Button(
    canvas_file_complaint_sub,
    image=file_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=clear_sub,
    relief="flat"
)
file_clear_btn.place(
    x=740.0,
    y=258.0,
    width=57.0,
    height=16.0
)
file_textarea = Text(
    canvas_file_complaint_sub,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Raleway", "13")
)
file_textarea.place(
    x=43.0,
    y=273.0,
    width=749.0,
    height=507.0
)
#--------------------------------------------------
# USE AI

use_ai_bg = PhotoImage(file=relative_to_assets("use_ai.png"))


canvas_use_ai = Canvas(
    window,
    bg = "#FFFFFF",
    height = 824,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_use_ai.create_image(
    578.0,
    412.0,
    image=use_ai_bg
)
search_bar = Entry(
    canvas_use_ai,
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=0,
    font = ("Raleway", "12")
)
search_bar.place(
    x=139.0,
    y=750.0,
    width=760.0,
    height=25.0
)
search_bar.bind("<Return>", fire_prompt)
canvas_use_ai.create_rectangle(
    949.0,
    750.0,
    1104.0,
    777.0,
    fill="#D9D9D9",
    outline="")
ai_textarea = Text(
    canvas_use_ai,
    bd=0,
    bg="#D9D9D9",
    fg="#000000",
    highlightthickness=0,
    font = ("Raleway", "13")
)
ai_textarea.place(
    x=47.0,
    y=270.0,
    width=1057.0,
    height=462.0
)
ai_clear_btn = Button(
    canvas_use_ai,
    image=file_clear_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=ai_clear,
    relief="flat"
)
ai_clear_btn.place(
    x=1056.0,
    y=249.0,
    width=57.0,
    height=16.0
)
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(
    canvas_use_ai,
    textvariable=dropdown_var,
    values = [],
    font=("Raleway", "13")
)
dropdown.place(
    x=949.0,
    y=750.0,
    width=155.0,
    height=27.0
)
dropdown.bind("<<ComboboxSelected>>", fire_selected_search_history)

responding_text = canvas_use_ai.create_text(
    50.0,
    800.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("RalewayRoman", "14")
)

#------------------ ---------------------------------
# NAV

safe_nav_img = PhotoImage(file=relative_to_assets("safe_nav.png"))
ppsu_logo = PhotoImage(file=relative_to_assets("ppsu.png"))
main_logo = PhotoImage(file=relative_to_assets("logo.png"))

canvas_nav = Canvas(
    window,
    bg = "#FFFFFF",
    height = 110,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_nav.create_rectangle(
    0.0,
    0.0,
    1500.0,
    110.0,
    fill="#1B293E",
    outline="")
canvas_nav.create_image(
    187.0,
    55.0,
    image=safe_nav_img
)
canvas_nav.create_image(
    1449.0,
    59.0,
    image=ppsu_logo
)
canvas_nav.create_text(
    276.0,
    63.0,
    anchor="nw",
    text="( citizens )",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 22 * -1)
)
canvas_nav.create_image(
    59.0,
    55.0,
    image=main_logo
)
canvas_nav.place(x = 0, y = 0)
#---------------------------------------------------

window.resizable(False, False)
window.mainloop()
