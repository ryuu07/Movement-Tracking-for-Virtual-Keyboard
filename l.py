import tkinter
import tkinter.messagebox
import customtkinter
import cv2
import customtkinter as tk
import subprocess
import signal
import os
import psutil

#from PIL import ImageTk, ImageV

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Movement Tracking for Virtual Keyboard")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, height=100,width=1000, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=10, rowspan=100, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="VirtualMachine", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event1, text= "Virtual Calculator")
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=10,)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event2, text= "Hand Keyboard")
        self.sidebar_button_2.grid(row=2, column=0, padx=10, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event3, text= "Gaze KeyBoard")
        self.sidebar_button_3.grid(row=3, column=0, padx=10, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event4, text= "TheSnakeGAME")
        self.sidebar_button_4.grid(row=4, column=0, padx=10, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event5, text= "Stop")
        self.sidebar_button_5.grid(row=5, column=0, padx=10, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", ],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

       

       



        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
       
       

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event1(self):
        subprocess.Popen(["C:/Users/prana/Desktop/hand_keyboard/HCI_final/Scripts/python.exe", "D:/HCI_final/calculator.py"])
        print("sidebar_button click")

    def sidebar_button_event2(self):

        self.process1=subprocess.Popen(["C:/Users/prana/Desktop/hand_keyboard/HCI_final/HCI_final/hand/Scripts/python.exe", "D:/HCI_final/hand_main.py"])
        #if not hasattr(self, 'hand_keyboard_process'):
        #    self.hand_keyboard_process = subprocess.Popen(["C:/Users/prana/Desktop/hand_keyboard/HCI_final/HCI_final/hand/Scripts/python.exe", "D:/HCI_final/hand_main.py"], preexec_fn=os.setsid)
        #self.process1.send_signal(signal.SIGTERM)
        print("sidebar_button click")

    def sidebar_button_event5(self):
        # kill the current process
        for p in psutil.process_iter():
            try:
                if p.name() in ["python.exe", "pythonw.exe"]:
                    cmdline = " ".join(p.cmdline())
                    if "hand_main.py" in cmdline or "eyemain.py" in cmdline or "calculator.py" in cmdline or "snakegame.py" in cmdline:
                        p.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        print("sidebar_button click")

    def sidebar_button_event3(self):
        subprocess.Popen(["C:/Users/prana/Desktop/hand_keyboard/HCI_final/eyegaze/Scripts/python.exe", "D:/HCI_final/eyemain.py"])
        print("sidebar_button click")

    def sidebar_button_event4(self):
        subprocess.Popen(["C:/Users/prana/Desktop/hand_keyboard/HCI_final/Scripts/python.exe", "D:/HCI_final/snakegame.py"])
        print("sidebar_button click")

    #def sidebar_button_event5(self):



if __name__ == "__main__":
    app = App()
    app.mainloop()