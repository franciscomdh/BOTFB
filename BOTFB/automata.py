from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from tkinter import *
import glob
import os

US1 = None

class User:
    def __init__(self, user, password):
        self.__userFB = user
        self.__passFB = password

    # getters
    def get_user(self):
        return self.__userFB

    def get_password(self):
        return self.__passFB

def Enviar():
    global US1
    userFB = username.get()
    passFB = password.get()
    US1 = User(userFB, passFB)
    
    if US1 is not None:
        username_entry = US1.get_user()
        password_entry = US1.get_password()
        login(username_entry, password_entry)
        
        caption = textPub.get("1.0", "end-1c")
        
        image_folder = "IMAGENES"  # Carpeta que contiene las imágenes
        image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))  # Obtener rutas de archivo de las imágenes
        
        for img_path in image_paths:
            upload_image(img_path, caption)
            
    else:
        print("El objeto US1 no ha sido creado aún")
        
def login(username, password):
    try:
        url = 'https://facebook.com'
        driver.get(url)
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        user.send_keys(username)
        pas = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'pass')))
        pas.send_keys(password)
        login_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'login')))
        login_btn.click()
    except:
        print("Algo anduvo mal en el proceso de logueo")

def upload_image(img_path, caption):
    try:
        btn1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div/i')))
        btn1.click()
        btn2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]')))
        btn2.click()
        
        btn3 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/span/div/div/div/div/div[1]/i')))
        btn3.click()
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(img_path)
        sleep(2)
        
        cap = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')))
        cap.send_keys(caption)
        
        btn_post = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]/div/span/span')))
        ActionChains(driver).move_to_element(btn_post).click().perform()
    except:
        print("Algo anduvo mal en el proceso de subida de archivos")
 # Asegúrate de tener el archivo del driver de Chrome en el mismo directorio
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(options=chrome_options)

raiz = Tk()

raiz.title("Autopublish")
raiz.iconbitmap("fb.ico")
raiz.config(bg="lightblue")
raiz.resizable(0, 0)

miFrame = Frame(raiz, width=650, height=400, bg="lightblue")
miFrame.pack()

# USER
usuarioLabel = Label(miFrame, text="Usuario fb:", font=20)
usuarioLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

username = StringVar()
userEntry = Entry(miFrame, font=20, width=30, textvariable=username)
userEntry.grid(row=0, column=1, padx=5, pady=10)
userEntry.config(justify="center")

# PASSWORD
passLabel = Label(miFrame, text="Password fb:", font=20)
passLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

password = StringVar()
passEntry = Entry(miFrame, font=20, width=30, textvariable=password)
passEntry.grid(row=2, column=1, padx=5, pady=10)
passEntry.config(justify="center", show="*")

# DESCRIPTION
textLabel = Label(miFrame, text="Texto:", font=20)
textLabel.grid(row=4, column=0, sticky="", pady=10)

textPub = Text(miFrame, width=30, height=10, font=20)
textPub.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textPub.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
textPub.config(yscrollcommand=scrollVert.set)

# BUSCADOR DE ARCHIVOS
Lblimg = Label(miFrame, text="Seleccione Imagen:", font=20)
Lblimg.grid(row=5, column=0, sticky="", pady=10)

btnSearchImg = Button(miFrame, text="Buscar..")
btnSearchImg.grid(row=5, column=1)

# BUTTON
BotonEnv = Button(miFrame, text="Enviar", padx=10, pady=5, command=Enviar)
BotonEnv.grid(row=6, columnspan=5, padx=5, pady=5)



raiz.mainloop()

    
    
    
    