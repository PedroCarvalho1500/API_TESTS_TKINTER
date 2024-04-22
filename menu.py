from tkinter import *
import execute_api

class ScreenFunctions():
    def openExecuteAPI(self):
        self.main_screen.destroy()
        execute_api_screen = Tk()
        new_screen = execute_api.Application(execute_api_screen)


class Application(ScreenFunctions):
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.screen()
        self.screen_buttons()
        self.main_screen.wait_window()

    def screen(self):
        self.main_screen.title("API_MAIN_MENU")
        
        self.main_screen.configure(background="gray6")
        
        self.main_screen.geometry("1400x800")
        
        self.main_screen.resizable(True, True)

        self.main_screen.maxsize(width=1720, height=1300)
        
        self.main_screen.minsize(width=900, height=900)


    def screen_buttons(self):    
        self.bt_execute_api_tests = Button(self.main_screen,text="Execute API Tests", border=2, bg="#9ac7d2", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white', command=self.openExecuteAPI)
        self.bt_execute_api_tests.place(relx=0.11, rely=0.22, relwidth=0.2, relheight=0.06)
        
        self.bt_quit = Button(self.main_screen,text="Quit Menu", border=2, bg="#9ac7d2", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white', command=self.main_screen.destroy)
        self.bt_quit.place(relx=0.11, rely=0.52, relwidth=0.2, relheight=0.06)


if __name__ == "__main__":
    main_screen = Tk()
    Application(main_screen)