import requests
from threading import Thread

#thread class
class ThreadsClass(Thread):
    def __init__(self, id, urls):
        super(ThreadsClass, self).__init__()
        self.id = id
        self.urls = urls

    def run(self):
        for num,li in enumerate(self.urls):
            self.Image_downloader(f"{self.id}_{num}",li)
    
    #image download function
    def Image_downloader(self, i, url):
        try:
            filename = f"Images/image_{i}.jpg"

            respond = requests.get(url, stream=True)
            if respond.status_code == 200:
                respond.raw.decode_content = True
                with open(filename,"wb") as file:
                    file.write(respond.content)
                
                print("image downloaded: ", filename)
            else:
                print("Image download error", filename)
        except requests.exceptions.ConnectionError:
            print("Make sure you connected to internet")
