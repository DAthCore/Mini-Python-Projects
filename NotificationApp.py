#pip install plyer
import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Python: Notification",
            message = "This a Message From App In Python",
            timeout = 110 
        )
        time.sleep(15)
