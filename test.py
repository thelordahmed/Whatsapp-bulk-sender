import os
import requests

dbFile_id = '1Fx3D4bucVK8_rqXqJJAzJlKnkAMy8aLV'


def download_dbFile(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    res = requests.get(url)
    home = os.path.expanduser("~")
    print(home)
    with open(f"{home}/Library/" + output + "/data.db", "wb") as f:
        f.write(res.content)
        f.close()


download_dbFile(dbFile_id, "WhatsappSenderData/Data")