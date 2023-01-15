#!bin/python3


from datetime import date
import subprocess

date = date.today()
print(date)

source_path = '/home/saran/f1'
dest_path = '/home/saran/backupfolder' + '-backup_items'
def backup():
    subprocess.run(['rsync -avzh source_path ,dest_path'],shell=True,capture_output=True)
    print(date)

if __name__=='__main__':
    backup()

