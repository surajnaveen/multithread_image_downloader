import requests
import time

img_count = 40

def image_url(count):
    if count<=0:
        print("Invalid Number")
        return
    
    for i in range(count):
        url = f"https://picsum.photos/id/{i}/100/200"
        yield url

def Image_downloader(i, url):
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

#calculate process time
start = time.time_ns()

for i,url in enumerate(image_url(img_count)):
    Image_downloader(i,url)

#print end time
print("Second: ",(time.time_ns()-start)/1_000_000_000)