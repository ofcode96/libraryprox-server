from flet import *

from typing import Optional
import subprocess ,os , signal
import socket as sk
import requests

from killtasks import get_all


class App (UserControl):

    page: None
    server_process = None
    url = f"http://{sk.gethostname()}:9000/api"

    def __init__(self, page):

        super().__init__()

        self.page = page

    def build(self):

        self.dot = CircleAvatar(

            bgcolor=colors.WHITE,

            width=25
        )
        self.status = Text("...")
        self.start_btn = ElevatedButton(

            "Start Server",

            style=ButtonStyle(

                color=colors.GREEN

            ),

            on_click=self.start_sarver


        )

        try:
            if requests.get(self.url).status_code == 200:
                self.dot.bgcolor = colors.GREEN
                self.status.value = "ON"
                self.status.color = colors.GREEN
                self.window_center()

        except:
            pass

        return Column(

            alignment=MainAxisAlignment.CENTER,

            # horizontal_alignment=CrossAxisAlignment.CENTER,

            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Text('LibraryProX Controller', size=20),
                        IconButton(
                            icon=icons.CLOSE,
                            on_click=lambda page: self.page.window_close()
                        ),
                    ]
                ),
                Container(height=20),

                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text("Server State :"),
                        self.status,
                    ]
                ),

                Container(height=10),

                Row(

                    alignment=MainAxisAlignment.CENTER,


                    controls=[

                        self.start_btn,

                        self.dot,

                        ElevatedButton(

                            "Stop Server",

                            style=ButtonStyle(

                                color=colors.RED_ACCENT
                            ),
                            on_click=self.stop_sarver



                        ),

                    ]
                )

            ]
        )

    def start_sarver(self, e):

        if not self.server_process or self.server_process.poll() is not None:

            self.server_process = subprocess.Popen(r"main.exe")
            try:
                response = requests.get(self.url)

                if response.status_code == 200:
                    self.dot.bgcolor = colors.GREEN
                    self.status.value = "ON"
                    self.status.color = colors.GREEN
                    self.start_btn.disabled = True

                else:
                    self.dot.bgcolor = colors.YELLOW
                    self.status.value = "WAITING"
                    self.status.color = colors.YELLOW

            except OSError as e:
                pass

        self.update()

    def stop_sarver(self, e):
      # self.server_process.terminate()
      # self.server_process.wait()
      
      pids = get_all()
      for pid in pids :
         os.kill(pid["pid"], signal.SIGTERM)
         print(f"pid:{pid['pid']} ✅")
      self.dot.bgcolor = colors.RED
      self.status.value = "OFF"
      self.status.color = colors.RED
      #   if self.server_process:
      #       # Terminate the server process



      #       if response.status_code != 200:
      #           self.dot.bgcolor = colors.RED
      #           self.status.value = "OFF"
      #           self.status.color = colors.RED
      #       else:
      #           self.dot.bgcolor = colors.YELLOW
      #           self.status.value = "WAITING"
      #           self.status.color = colors.YELLOW

      self.update()
      print("stop")


def run(page: Page):

    page.title = "LibraryProX Controller"

    page.theme_mode = ThemeMode.DARK

    page.window_center()

    page.window_width = 400

    page.window_height = 210

    page.window_resizable = False
    page.window_title_bar_hidden = True

    page.add(WindowDragArea(App(page=page)))

    page.update()


app(run)
