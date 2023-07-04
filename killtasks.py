import subprocess ,os ,re ,signal


def get_all():

    output = subprocess.Popen(
        "tasklist /v /fo csv | findstr /i main.exe",
        stdout=subprocess.PIPE,
        shell=True
    )
    (std, err) = output.communicate()
    p_status = output.wait()

    text = re.sub(r'"', '', std.decode("utf-8"))
    items = re.split(r'\r\n', text)

    clean_items = []

    for item in items:
        clean_items.append(item.split(','))

    list_process = []

    for row in clean_items:
        if not len(row[0]):
            continue
        object_list = {
             "process": row[0],
            "pid": int(row[1]),
            "state": row[6]
        }
        list_process.append(object_list)

    return list_process
 
 
# pids = get_all()
# print(pids)
# for pid in pids :
#    os.kill(pid["pid"], signal.SIGTERM)
#    print(f"pid:{pid['pid']} ✅")
 
 
 
