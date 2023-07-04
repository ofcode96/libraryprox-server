import os 

main_path = os.getcwd() + "\killtasks.exe"

os.system(f"""cmd /k powershell -Command "Start-Process '{main_path}' -Verb runAs" -WindowStyle Hidden """)

os.sys.exit()