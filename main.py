import requests

def image_url(count):
    if count<=0:
        print("Invalid Number")
        return
    
    for i in range(count):
        url = f"https://picsum.photos/id/{i}/200/300"
        yield url

for url in image_url(10):
    respond = requests.get(url)
    print(respond)