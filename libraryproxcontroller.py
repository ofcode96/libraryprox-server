import subprocess
import time
import requests
import asyncio
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from constants.api import Api
import socket as sk
server_process = None


def start_server():
    global server_process
    # Start the server script as a separate process
    server_process = subprocess.Popen(r"main.exe")


def stop_server():
    global server_process
    if server_process:
        # Terminate the server process
        server_process.terminate()
        server_process.wait()
        server_process = subprocess.Popen(r"killtasks.exe")


def main():
    root = ttk.Window(themename="darkly")
    root.title("LibraryProX Server Controller")
    root.iconbitmap("logo.ico")
    style = ttk.Style("darkly")

    app_width = 220
    app_height = 100
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = (width / 2) - (app_width / 2)
    y = (height / 2) - (app_height / 2)

    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    root.resizable(False, False)

    state_input = tk.StringVar(value="danger")

    def start():

        # Create a new process for the server if it is not already running
        if not server_process or server_process.poll() is not None:

            start_server()

         
    def stop():
        stop_server()
       
        fram.config(bootstyle="danger")

    start_button = ttk.Button(
        root, text="Start Server", command=start, bootstyle=SUCCESS)
    start_button.pack(side=LEFT, padx=5, pady=10)

    fram = ttk.Frame(root, bootstyle="danger", height=10, width=10)
    fram.pack(
        side=LEFT, padx=12, pady=10,)

    stop_button = ttk.Button(root, text="Stop Server",
                             command=stop, bootstyle=DANGER)
    stop_button.pack(side=RIGHT, padx=5, pady=10)
    
    
    url = f"http://{sk.gethostname()}:9000/api"
    try:
      response = requests.get(url)
       
      if response.status_code == 200:
         fram.config(bootstyle="success")
      else : 
         fram.config(bootstyle="danger")
          
    except OSError as e:
      pass
    
    

    root.mainloop()


if __name__ == "__main__":
    main()
