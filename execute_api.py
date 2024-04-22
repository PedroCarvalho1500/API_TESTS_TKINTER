import os
import subprocess
from threading import Thread
from tkinter import *
import menu

buttons_list = []

folders_created = []

folders = ["BOOK", "MOVIE", "CHARACTER", "QUOTE", "CHAPTER", "Execute All"]

commands_to_execute_tests = {
"BOOK": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"BOOK\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc",
"MOVIE": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"MOVIE\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc",
"CHARACTER": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"CHARACTER\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc",
"QUOTE": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"QUOTE\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc",
"CHAPTER": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"CHAPTER\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc",
"Execute All": "newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"CHAPTER\" --delay-request 200 --env-var api_key=eMvGyiKj9aQDNEB14psc"
}

stop_thread = False
callId = ""


class ScreenFunctions():
    def openMainMenu(self):
        self.execute_api_screen.destroy()
        main_menu = Tk()
        main_menu = menu.Application(main_menu)

    def clock(self):
        global callId
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
    
        self.text.insert(END, os.popen("cat current_test.txt").read()+"\n\n")
        self.text.see("end")
        self.text.config(state=DISABLED)
        if (os.popen('ps aux | grep "newman run" | grep -v grep').read() == ''): 
            print(f"FINISHED")

            for button in buttons_list: 
                button["state"] = "normal"

            self.text.config(state=NORMAL)
            self.text.delete('1.0', END)
            self.text.insert(END, os.popen("cat current_test.txt").read()+"\n\n\n")
            self.text.see("end")
            self.text.config(state=DISABLED)
            self.text.after_cancel(callId)

            callId = None
            

        else:
            callId = self.text.after(1300,self.clock)

    def run_thread(self):
        subprocess.call(self.command+"> current_test.txt", shell=True)

    def dircall(self, command):
        global stop_thread
        stop_thread = False

        #CHANGED HERE TO DISABLE BUTTONS WHILE EXECUTING TESTS
        for button in buttons_list: 
            button["state"] = "disabled"

        os.system("clear")
        self.command = command

        new_thread = Thread(target = self.run_thread)
        new_thread.start()
        self.clock()

    def create_button(self,name, screen, text, border, bg, font, activebackground ,activeforeground, command, x, y):
        name = Button(screen, text=text, border=border, bg=bg, font=font, activebackground=activebackground ,activeforeground=activeforeground, command=lambda: self.dircall(command))
        name.place(relx=x, rely=y, relwidth=0.1144, relheight=0.0289999)
        #DELETE TWO LINES BELOW IF SOME PROBLEM APPEARS
        buttons_list.append(name)
        #input(f'{buttons_list}')
        return name




class Application(ScreenFunctions):
    def __init__(self, execute_api_screen):
        self.execute_api_screen = execute_api_screen
        self.x = 6
        self.y = 8
        self.screen()
        self.buttons()
        self.text_area()
        self.scroll_bar_screen()
        self.execute_api_screen.mainloop()

    def screen(self):
        self.execute_api_screen.title("API_TESTS_TERMINAL_NEWMAN")
        
        self.execute_api_screen.configure(background="black")
        
        self.execute_api_screen.geometry("1500x970")
        
        self.execute_api_screen.resizable(False, False)
        

        self.execute_api_screen.maxsize(width=1720, height=1300)
        
        self.execute_api_screen.minsize(width=900, height=900)


    def buttons(self):
        x = 0.003
        y = 0.009
        index = 0
        
        for folder in folders:
            folders_created.append(folder)
            
            self.create_button(folder, self.execute_api_screen, folder, 2, "#9ac7d2", ('verdana', 6, 'bold'), '#108ecb' ,'white', commands_to_execute_tests[folder],x,y)
            y+=0.029
            if(y >= 0.98):
                x+=0.12
                if(x >= 0.5 or x<=0.75): x=0.89
                y = 0.01
            index+=1

        self.bt_back = Button(self.execute_api_screen, text="Back", border=2, bg="#9ac7d2", font=('verdana', 6, 'bold'), activebackground='#108ecb' ,activeforeground='white', command=self.openMainMenu)
        self.bt_back.place(relx=x,rely=y, relwidth=0.1144, relheight=0.0289999)
        
        buttons_list.append(self.bt_back)


    def text_area(self):
        self.text = Text(self.execute_api_screen, fg='white', background='black')
        self.text.place(relx=0.11905, rely=0.01, relheight=1, relwidth=0.75998)
        self.text.insert(END, "SEE THE EXECUTION HERE")
        self.text.config(state=DISABLED)


    def scroll_bar_screen(self):
        S = Scrollbar(self.execute_api_screen, highlightbackground='green', background='white', troughcolor='gray')
        S.place(relx=0.87787, rely=0.01, relwidth=0.012, relheight=0.99)


        H = Scrollbar(self.execute_api_screen, orient="horizontal", highlightbackground='green', background='white', troughcolor='gray')
        H.place(relx=0.12066, rely=0.9822, relwidth=0.7572, relheight=0.0178)
        

        self.text.config(wrap = NONE)
        self.text.config(yscrollcommand=S.set, xscrollcommand = H.set)
        H.config(command=self.text.xview)
        S.config(command=self.text.yview)


if __name__ == "__main__":
    execute_api_screen = Tk()
    Application(execute_api_screen)



#newman run DEMO_LOTR_API.postman_collection.json --environment LOTR_API_ENVIRONMENT.postman_environment.json --folder \"BOOK\" --delay-request 200
# AUTH_KEY=eMvGyiKj9aQDNEB14psc