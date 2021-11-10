from datetime import datetime

class Abstract:

    def getCurrentTime(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
