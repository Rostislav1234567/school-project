from customtkinter import *
import math
from CTkMessagebox import CTkMessagebox
from PIL import Image
from sympy import cos, sin, tan, pi, simplify



window = CTk()
window.geometry("500x500")
window.title("Calculator")
window.configure(fg_color="black")


window.update()
width = window.winfo_width()
height = window.winfo_height()



image = Image.open("images(for pycharm).png.jpeg")
image = image.resize((width, height))



bg_image = CTkImage(dark_image = image, size=(width, height))


bg_label = CTkLabel(window, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=6, relheight=10)




window.grid_columnconfigure((0,1,2,3), weight=1)


entry = CTkEntry(window, width=300, height=50, justify="right")
entry.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky="we")





def sqrt_number():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")







knopka_sqrt = CTkButton(window, fg_color="orange", text="√", text_color="white", corner_radius=15, command=sqrt_number)
knopka_sqrt.grid(row=6, column=3, padx=2, pady=0, sticky="nsew")






def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert(0, result)
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")


def clear():
    entry.delete(0, "end")


def add_symbol(symbol):
    entry.insert("end", symbol)





knopka_is_equal_to = CTkButton(window, fg_color="orange", text="=", text_color="white", corner_radius=15, command=calculate)
knopka_is_equal_to.grid(row=2, column=4, columnspan=5)




def clear():
    msg = CTkMessagebox(
        title="Підтвердження",
        message="Що ви хочете зробити?",
        icon="question",
        option_1="← 1 символ",
        option_2="Очистити все"
    )


    response = msg.get()
    if response == "← 1 символ":
        text = entry.get()
        if text:
            entry.delete(len(text)-1, "end")

    elif response == "Очистити все":
        entry.delete(0, "end")



knopka_CLEAR = CTkButton(window, fg_color="orange", text="C", text_color="white", corner_radius=15, command=clear)
knopka_CLEAR.grid(row=1, column=4, columnspan=6)







####### MAIN WINDOW

#############################################################################################################
#############################################################################################################
############################WWWWWWWWWWWW#####################################################################
#############################IIIIIIIIIIIIIIIIIII##############################################################
########################NNNNNNNNNNNNNNNNNNNNNÑNNNNNNNNNNNNNNNN
#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW

#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW



#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW



#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW



#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


#WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW WINDOW


########################################################################################################################
#############BUTTONS FOR OPENING THE SECOND OT THIRD OT FOURTH WINDOW###################################################
########################################################################################################################


#2-4


#3-4



##################################################################################
#########################Buttons(Digits)#########################################
##################################################################################




knopka_1 = CTkButton(window, fg_color="orange", text="1", text_color="white", corner_radius=15, command=lambda: add_symbol("1"))
knopka_1.grid(row=1, column=0, padx=2, pady=0, sticky="nsew")

knopka_2 = CTkButton(window, fg_color="orange", text="2", text_color="white", corner_radius=15, command=lambda: add_symbol("2"))
knopka_2.grid(row=1, column=1, padx=2, pady=0, sticky="nsew")

knopka_3 = CTkButton(window, fg_color="orange", text="3", text_color="white", corner_radius=15, command=lambda: add_symbol("3"))
knopka_3.grid(row=1, column=2, padx=2, pady=0, sticky="nsew")


knopka_4 = CTkButton(window, fg_color="orange", text="4", text_color="white", corner_radius=15, command=lambda: add_symbol("4"))
knopka_4.grid(row=2, column=0, padx=2, pady=0, sticky="nsew")


knopka_5 = CTkButton(window, fg_color="orange", text="5", text_color="white", corner_radius=15, command=lambda: add_symbol("5"))
knopka_5.grid(row=2, column=1, padx=2, pady=0, sticky="nsew")


knopka_6 = CTkButton(window, fg_color="orange", text="6", text_color="white", corner_radius=15, command=lambda: add_symbol("6"))
knopka_6.grid(row=2, column=2, padx=2, pady=0, sticky="nsew")


knopka_7 = CTkButton(window, fg_color="orange", text="7", text_color="white", corner_radius=15, command=lambda: add_symbol("7"))
knopka_7.grid(row=3, column=0, padx=2, pady=0, sticky="nsew")


knopka_8 = CTkButton(window, fg_color="orange", text="8", text_color="white", corner_radius=15, command=lambda: add_symbol("8"))
knopka_8.grid(row=3, column=1, padx=2, pady=0, sticky="nsew")



knopka_9 = CTkButton(window, fg_color="orange", text="9", text_color="white", corner_radius=15, command=lambda: add_symbol("9"))
knopka_9.grid(row=3, column=2, padx=2, pady=0, sticky="nsew")


knopka_10 = CTkButton(window, fg_color="orange", text="10", text_color="white", corner_radius=15, command=lambda: add_symbol("10"))
knopka_10.grid(row=4, column=0, padx=2, pady=0, sticky="nsew")

knopka_11 = CTkButton(window, fg_color="orange", text="11", text_color="white", corner_radius=15, command=lambda: add_symbol("11"))
knopka_11.grid(row=4, column=1, padx=2, pady=0, sticky="nsew")

knopka_12 = CTkButton(window, fg_color="orange", text="12", text_color="white", corner_radius=15, command=lambda: add_symbol("12"))
knopka_12.grid(row=4, column=2, padx=2, pady=0, sticky="nsew")

knopka_13 = CTkButton(window, fg_color="orange", text="13", text_color="white", corner_radius=15, command=lambda: add_symbol("13"))
knopka_13.grid(row=5, column=0, padx=2, pady=0, sticky="nsew")


knopka_14 = CTkButton(window, fg_color="orange", text="14", text_color="white", corner_radius=15, command=lambda: add_symbol("14"))
knopka_14.grid(row=5, column=1, padx=2, pady=0, sticky="nsew")


knopka_15 = CTkButton(window, fg_color="orange", text="15", text_color="white", corner_radius=15, command=lambda: add_symbol("15"))
knopka_15.grid(row=5, column=2, padx=2, pady=0, sticky="nsew")


knopka_16 = CTkButton(window, fg_color="orange", text="16", text_color="white", corner_radius=15, command=lambda: add_symbol("16"))
knopka_16.grid(row=6, column=0, padx=2, pady=0, sticky="nsew")


knopka_17 = CTkButton(window, fg_color="orange", text="17", text_color="white", corner_radius=15, command=lambda: add_symbol("17"))
knopka_17.grid(row=6, column=1, padx=2, pady=0, sticky="nsew")



knopka_18 = CTkButton(window, fg_color="orange", text="18", text_color="white", corner_radius=15, command=lambda: add_symbol("18"))
knopka_18.grid(row=6, column=2, padx=2, pady=0, sticky="nsew")


knopka_19 = CTkButton(window, fg_color="orange", text="19", text_color="white", corner_radius=15, command=lambda: add_symbol("19"))
knopka_19.grid(row=7, column=0, padx=2, pady=0, sticky="nsew")


knopka_20 = CTkButton(window, fg_color="orange", text="20", text_color="white", corner_radius=15, command=lambda: add_symbol("20"))
knopka_20.grid(row=7, column=1, padx=2, pady=0, sticky="nsew")


knopka_0 = CTkButton(window, fg_color="orange", text="0", text_color="white", corner_radius=15, command=lambda: add_symbol("0"))
knopka_0.grid(row=7, column=2, padx=2, pady=0, sticky="nsew")










############################################
#####BUTTONS_FUNCTIONS######################
############################################

knopka_plus = CTkButton(window, fg_color="orange", text="+", text_color="white", corner_radius=15, command=lambda: add_symbol("+"))
knopka_plus.grid(row=1, column=3, padx=2, pady=0, sticky="nsew")

knopka_minus = CTkButton(window, fg_color="orange", text="-", text_color="white", corner_radius=15, command=lambda: add_symbol("-"))
knopka_minus.grid(row=2, column=3, padx=2, pady=0, sticky="nsew")


knopka_multiplication = CTkButton(window, fg_color="orange", text="*", text_color="white", corner_radius=15, command=lambda: add_symbol("*"))
knopka_multiplication.grid(row=3, column=3, padx=2, pady=0, sticky="nsew")


knopka_division = CTkButton(window, fg_color="orange", text="/", text_color="white", corner_radius=15, command=lambda: add_symbol("/"))
knopka_division.grid(row=4, column=3, padx=2, pady=0, sticky="nsew")

knopka_power = CTkButton(window, fg_color="orange", text="x²", text_color="white", corner_radius=15, command=lambda: add_symbol("**"))
knopka_power.grid(row=5, column=3, padx=2, pady=0, sticky="nsew")








def open_game():
    win_4 = CTkToplevel(window)
    win_4.title("It is the mathematical game")
    win_4.configure(fg_color="black")
    win_4.geometry("500x500")

    frame_1 = CTkFrame(win_4, fg_color="white")
    frame_1.pack(side="top", fill="both", expand=True)


    frame_2 = CTkFrame(win_4, fg_color="black")
    frame_2.pack(side="bottom", fill="both", expand=True)





button_opengame = CTkButton(window, fg_color="orange", text="open game", text_color="white", command=open_game)
button_opengame.grid(row=6, column=4)


























def ask_trigonometry():
    msg = CTkMessagebox(title="Trigonometry section", message="Що відкриваємо?", icon="question", option_1="Відкриємо тригонометричний відділ", option_2="чи підемо відпочинемо")
    response = msg.get()

    if response == "Відкриємо тригонометричний відділ":
        open_second_window_forsincostan()

    else:
        CTkMessagebox(title="recovery", message="Okeylets do some rest", icon="info")













#3-4



def open_window_with_questions():
    msg = CTkMessagebox(title="It is a mini-wikipedia about calculator", message="What will we do?", icon="question", option_1="We go to learn some interest information?", option_2="or go for the rest?")

    response = msg.get()


    if response == "We go to learn some interest information?":
        open_third_window_with_information_forwegotolearnsomeinformation()








    elif response == "or go for the rest?":
        open_windowifwechoosegototherest()
















def open_third_window_with_information_forwegotolearnsomeinformation():
    win_3 = CTkToplevel(window)
    win_3.configure(fg_color="orange")
    win_3.geometry("500x500")
    win_3.title("There we prepared some interest information about first calculator")









    label = CTkLabel(win_3, text="📜 Історія калькулятора")
    label.grid(row=0, column=0)

    label_2 = CTkLabel(win_3, text="Перший механічний калькулятор створив у 1642 році французький математик Блез Паскаль.")
    label_2.grid(row=1, column=0)

    label_3 = CTkLabel(win_3, text="Його пристрій називався «Паскаліна» і міг виконувати додавання та віднімання.")
    label_3.grid(row=2, column=0)

    label_4 = CTkLabel(win_3, text="Пізніше з’явилися більш складні механічні машини, а у ХХ столітті були створені електронні калькулятори.")
    label_4.grid(row=3, column=0)

    label_5 = CTkLabel(win_3,text="У 1970-х роках компанія Texas Instruments почала масове виробництво кишенькових калькуляторів.")
    label_5.grid(row=4, column=0)

    label_4 = CTkLabel(win_3,text="🔢 Види калькуляторів")
    label_4.grid(row=5, column=0)

    label_4 = CTkLabel(win_3, text="Простий (базовий) — для звичайних обчислень.")
    label_4.grid(row=6, column=0)


    label_4 = CTkLabel(win_3,text="Інженерний (науковий) — має функції sin, cos, tan, log тощо.")
    label_4.grid(row=7, column=0)

    label_4 = CTkLabel(win_3, text="Графічний — будує графіки функцій")
    label_4.grid(row=8, column=0)

    label_4 = CTkLabel(win_3, text="Програмний — вбудований у комп’ютер або смартфон.")
    label_4.grid(row=9, column=0)

    label_4 = CTkLabel(win_3, text="⚙️ Як працює калькулятор?")
    label_4.grid(row=10, column=0)



    label_4 = CTkLabel(win_3, text="Всередині калькулятора є:")
    label_4.grid(row=11, column=0)

    label_4 = CTkLabel(win_3, text="процесор (який виконує обчислення),")
    label_4.grid(row=12, column=0)

    label_4 = CTkLabel(win_3, text="пам’ять (зберігає числа),")
    label_4.grid(row=13, column=0)

    label_4 = CTkLabel(win_3, text="дисплей (показує результат),")
    label_4.grid(row=14, column=0)

    label_4 = CTkLabel(win_3, text="кнопки для введення даних.")
    label_4.grid(row=15, column=0)

    label_4 = CTkLabel(win_3, text="Коли ти натискаєш кнопку, пристрій перетворює це на цифровий код і")
    label_4.grid(row=16, column=0)

    label_4 = CTkLabel(win_3, text="виконує потрібну математичну операцію.")
    label_4.grid(row=17, column=0)


















def open_windowifwechoosegototherest():
    win_joke = CTkToplevel(window)
    win_joke.configure(bg_color="black")
    win_joke.geometry("500x500")
    win_joke.title("Rest")



    image = Image.open("images.photo.jpeg")
    img_ctk = CTkImage(dark_image = image, size=(500, 500))


    label_img = CTkLabel(win_joke, image=img_ctk, text="enough resting ,go to work lazy cow!!!!!!!")
    label_img.pack()








def open_second_window_forsincostan():
    win_2 = CTkToplevel(window)
    win_2.title("Trigonometrical section")
    win_2.geometry("500x500")
    win_2.configure(fg_color="black")

    entry_2 = CTkEntry(win_2, width=300, height=50, justify="left")
    entry_2.grid(row=7, column=1, columnspan=10, sticky="we")

    def clearss():
        msg  = CTkMessagebox(title="Стерти все чи тільки щось одне", message="Що ви хочете зробити?", icon="question", option_1="-1 символ", option_2="Стерти все")
        response = msg.get()
        if response == "-1 символ":
            text = entry_2.get()
            if text:
                entry_2.delete(len(text)-1, "end")

        elif response == "Стерти все":
            entry_2.delete(0, "end")


    def add_symbol_2(symbol):
        entry_2.insert("end", symbol)



    def calculate_2():
        try:
            result = eval(entry_2.get())
            entry_2.delete(0, "end")
            entry_2.insert(0, result)




        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")




    def sin_number():
        try:
            value = float(entry_2.get())
            result = math.sin(math.radians(value))
            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))

        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def cos_number():
        try:
            value = float(entry_2.get())
            result = math.cos(math.radians(value))
            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))



        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def tan_number():
        try:
            value = float(entry_2.get())
            result = math.tan(math.radians(value))
            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))



        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def ctg_number():
        try:
            value = float(entry_2.get())
            result = math.ctg(math.radians(value))
            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))




        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def cos_exact():
        try:
            value = entry_2.get()
            deg = float(value)

            rad = deg * pi / 180

            result = simplify(cos(rad))

            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))




        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def sin_exact():
        try:
            value = entry_2.get()
            deg = float(value)

            rad = deg * pi / 180

            result = simplify(sin(rad))

            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))



        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")

    def tan_exact():
        try:
            value = entry_2.get()
            deg = float(value)
            rad = deg * pi / 180

            result = simplify(tan(rad))

            entry_2.delete(0, "end")
            entry_2.insert(0, str(result))




        except:
            entry_2.delete(0, "end")
            entry_2.insert(0, "Error")





    #######################################################################################################################
    #####################BUTTONS THAT ARE AROUND(DIGITS FOR TRIGONOMETRIC FUNCTIONS OF SOME CORNERS)#######################
    #######################################################################################################################

    knopka_21 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_21.grid(row=8, column=0, padx=3, pady=3, sticky="nsew")

    knopka_22 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_22.grid(row=8, column=1, padx=3, pady=3, sticky="nsew")

    knopka_23 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_23.grid(row=8, column=2, padx=3, pady=3, sticky="nsew")

    knopka_24 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_24.grid(row=8, column=3, padx=3, pady=3, sticky="nsew")

    knopka_25 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_25.grid(row=8, column=4, padx=3, pady=3, sticky="nsew")

    knopka_26 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_26.grid(row=8, column=5, padx=3, pady=3, sticky="nsew")

    knopka_27 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_27.grid(row=9, column=0, padx=3, pady=3, sticky="nsew")

    knopka_28 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_28.grid(row=10, column=0, padx=3, pady=3, sticky="nsew")

    knopka_29 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_29.grid(row=11, column=0, padx=3, pady=3, sticky="nsew")

    knopka_30t = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_30t.grid(row=12, column=0, padx=3, pady=3, sticky="nsew")

    knopka_30t = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_30t.grid(row=13, column=0, padx=3, pady=3, sticky="nsew")


    knopka_31t = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_31t.grid(row=13, column=1, padx=3, pady=3, sticky="nsew")

    knopka_34 = CTkButton(win_2, fg_color="blue", text="----", corner_radius=0, text_color="white")
    knopka_34.grid(row=13, column=2, padx=3, pady=3, sticky="nsew")

    knopka_35 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_35.grid(row=13, column=3, padx=3, pady=3, sticky="nsew")

    knopka_36 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_36.grid(row=12, column=3, padx=3, pady=3, sticky="nsew")

    knopka_37 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_37.grid(row=11, column=3, padx=3, pady=3, sticky="nsew")

    knopka_38 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_38.grid(row=10, column=3, padx=3, pady=3, sticky="nsew")

    knopka_39 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_39.grid(row=9, column=3, padx=3, pady=3, sticky="nsew")

    knopka_40 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    knopka_40.grid(row=8, column=3, padx=3, pady=3, sticky="nsew")




    #######################################################################################################################
    #############################DIGITS FOR TRIGONOMETRIC FUNCTIONS OF SOME CORNERS########################################
    #######################################################################################################################

    #######################
    ###DEGREES#############
    #######################

    # 9-1, 9-2,  10-1, ,10-2,, 11-1, ,11-2, 12-1, 12-2





# 13-1
    knopka_30 = CTkButton(win_2, fg_color="orange", text="30", text_color="white", corner_radius=15, command=lambda: add_symbol_2("30"))
    knopka_30.grid(row=9, column=1, padx=3, pady=3, sticky="nsew")

    knopka_45 = CTkButton(win_2, fg_color="orange", text="45", text_color="white", corner_radius=15, command=lambda: add_symbol_2("45"))
    knopka_45.grid(row=9, column=2, padx=3, pady=3, sticky="nsew")

    knopka_60 = CTkButton(win_2, fg_color="orange", text="60", text_color="white", corner_radius=15, command=lambda: add_symbol_2("60"))
    knopka_60.grid(row=10, column=1, padx=3, pady=3, sticky="nsew")

    knopka_90 = CTkButton(win_2, fg_color="orange", text="90", text_color="white" ,corner_radius=15, command=lambda: add_symbol_2("90"))
    knopka_90.grid(row=10, column=2, padx=3, pady=3, sticky="nsew")

    knopka_180 = CTkButton(win_2, fg_color="orange", text="180", text_color="white", corner_radius=15, command=lambda: add_symbol_2("180"))
    knopka_180.grid(row=11, column=1, padx=3, pady=3, sticky="nsew")

    knopka_270 = CTkButton(win_2, fg_color="orange", text="270", text_color="white", corner_radius=15, command=lambda: add_symbol_2("270"))
    knopka_270.grid(row=11, column=2, padx=3, pady=3, sticky="nsew")

    knopka_360 = CTkButton(win_2, fg_color="orange", text="360", text_color="white", corner_radius=15, command=lambda: add_symbol_2("360"))
    knopka_360.grid(row=12, column=1, padx=3, pady=3, sticky="nsew")

    knopka_0 = CTkButton(win_2, fg_color="orange", text="0", text_color="white", corner_radius=15, command=lambda: add_symbol_2("0"))
    knopka_0.grid(row=12, column=2, padx=3, pady=3, sticky="nsew")

    #######################################################################################################################

    ##########Buttons that are around cos, sin, tan, ctg that shows result in radians#########

    tyk_sth1 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth1.grid(row=8, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth2 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth2.grid(row=9, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth3 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth3.grid(row=10, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth4 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth4.grid(row=11, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth5 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth5.grid(row=12, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth6 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth6.grid(row=13, column=4, padx=3, pady=3, sticky="nsew")

    tyk_sth7 = CTkButton(win_2, fg_color="blue", text="-----", corner_radius=0, text_color="white")
    tyk_sth7.grid(row=13, column=5, padx=3, pady=3, sticky="nsew")

    tyk_sth8 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth8.grid(row=13, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth9 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth9.grid(row=12, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth10 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth10.grid(row=11, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth11 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth11.grid(row=10, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth12 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth12.grid(row=9, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth13 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tyk_sth13.grid(row=8, column=6, padx=3, pady=3, sticky="nsew")

    tyk_sth14 = CTkButton(win_2, fg_color="blue", text="-----", corner_radius=0, text_color="white")
    tyk_sth14.grid(row=8, column=5, padx=3, pady=3, sticky="nsew")

    # 4-5    5-5   6-5       7-5

    ###############SINUS,  COS,   TAN, CTG###########
    # that show result in radians#######################
    ####################################################

    knopka_sinus = CTkButton(win_2, fg_color="orange", text="sin", text_color="white", corner_radius=15, command=sin_number)
    knopka_sinus.grid(row=9, column=5, padx=3, pady=3, sticky="nsew")

    knopka_cosunus = CTkButton(win_2, fg_color="orange", text="cos", text_color="white", corner_radius=15, command=cos_number)
    knopka_cosunus.grid(row=10, column=5, padx=3, pady=3, sticky="nsew")

    knopka_tangens = CTkButton(win_2, fg_color="orange", text="tan", text_color="white", corner_radius=15, command=tan_number)
    knopka_tangens.grid(row=11, column=5, padx=3, pady=3, sticky="nsew")

    knopka_cotangens = CTkButton(win_2, fg_color="orange", text="ctg", text_color="white", corner_radius=15, command=ctg_number)
    knopka_cotangens.grid(row=12, column=5, padx=3, pady=3, sticky="nsew")

    ##########################################################################################################
    ######################Buttons that are around cos, sin, tan, ctg that shows result in digits########
    ##########################################################################################################



    tykflyk_2 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_2.grid(row=8, column=7, padx=3, pady=3, sticky="nsew")

    tykflyk_3 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_3.grid(row=9, column=7, padx=3, pady=3, sticky="nsew")

    tykflyk_4 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_4.grid(row=10, column=7, padx=3, pady=3, sticky="nsew")

    tykflyk_5 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_5.grid(row=11, column=7, padx=3, pady=3, sticky="nsew")

    tykflyk_6 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_6.grid(row=12, column=7, padx=3, pady=3, sticky="nsew")

    tykflyk_7 = CTkButton(win_2, fg_color="blue", text="-----", corner_radius=0, text_color="white")
    tykflyk_7.grid(row=12, column=8, padx=3, pady=3, sticky="nsew")

    tykflyk_8 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_8.grid(row=12, column=9, padx=3, pady=3, sticky="nsew")

    tykflyk_9 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_9.grid(row=11, column=9, padx=3, pady=3, sticky="nsew")

    tykflyk_10 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_10.grid(row=10, column=9, padx=3, pady=3, sticky="nsew")

    tykflyk_12 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_12.grid(row=9, column=9, padx=3, pady=3, sticky="nsew")

    tykflyk_13 = CTkButton(win_2, fg_color="blue", text="|", corner_radius=0, text_color="white")
    tykflyk_13.grid(row=8, column=9, padx=3, pady=3, sticky="nsew")

    tykflyk_14 = CTkButton(win_2, fg_color="blue", text="-----", corner_radius=0, text_color="white")
    tykflyk_14.grid(row=8, column=8, padx=3, pady=3, sticky="nsew")



#7-8

########


#8-7




#12-9



#9, 10, 11-8
    ##################################################
    #######Buttons cos, tan, sin #####################
    #####that shows result in digits##################
    ##################################################

    sin_exactbutton = CTkButton(win_2, fg_color="orange", text="sin", text_color="white", corner_radius=15, command=sin_exact)
    sin_exactbutton.grid(row=9, column=8, padx=3, pady=3, sticky="nsew")

    cos_exactbutton = CTkButton(win_2, fg_color="orange", text="cos", text_color="white", corner_radius=15, command=cos_exact)
    cos_exactbutton.grid(row=10, column=8, padx=3, pady=3, sticky="nsew")

    tan_exactbutton = CTkButton(win_2, fg_color="orange", text="tan", text_color="white", corner_radius=15, command=tan_exact)
    tan_exactbutton.grid(row=11, column=8, padx=3, pady=3, sticky="nsew")


####################Buttons in the second window.Functions#################
    btn_clearss = CTkButton(win_2, fg_color="orange", text="C", text_color="white", corner_radius=15, command=clearss)
    btn_clearss.grid(row=8, column=10, padx=3, pady=3, sticky="nsew")


    btn_calculate_2 = CTkButton(win_2, fg_color="orange", text="==", text_color="white", corner_radius=15, command=calculate_2)
    btn_calculate_2.grid(row=9, column=10, padx=3, pady=3, sticky="nsew")



    button_back = CTkButton(win_2, text="back", command=win_2.destroy)
    button_back.grid(row=10, column=10)


    entry_2 = CTkEntry(win_2, width=300, height=50, justify="left")
    entry_2.grid(row=7, column=1, columnspan=10, sticky="ew")





########################################################################################################################
#############BUTTONS FOR OPENING THE SECOND OT THIRD OT FOURTH WINDOW###################################################
########################################################################################################################


#2-4


#3-4

button_open_trigonometrical_section = CTkButton(window, fg_color="orange", text="trigonometric section", text_color="white", corner_radius=15, command=open_second_window_forsincostan)
button_open_trigonometrical_section.grid(row=3, column=4, padx=2, pady=0, sticky="nsew")



button_learnsomeinformation = CTkButton(window, bg_color="orange", text="some_information", text_color="white", corner_radius=15, command=open_window_with_questions)
button_learnsomeinformation.grid(row=5, column=4, padx=3, pady=3, sticky="nsew")





some_button = CTkButton(window, fg_color="orange", hover_color="darkorange",  text="tronometrical section_with joke", text_color="white", corner_radius=15, command=ask_trigonometry)
some_button.grid(row=4, column=4, padx=3, pady=3, sticky="nsew")















window.mainloop()





