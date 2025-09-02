import time
import my_threads

#number of images
img_count = 40

def image_url(count):
    if count<=0:
        print("Invalid Number")
        return
    
    for i in range(count):
        url = f"https://picsum.photos/id/{i}/100/200"
        yield url

#calculate process time
start = time.time_ns()

full_url_list = [i for i in image_url(img_count)]
urls_list = []

#slicing size of url list
thread_count = 10

for i in range(0,len(full_url_list),thread_count):
    li = full_url_list[i: (i+thread_count)]
    urls_list.append(li)

#print(len(urls_list))

#get the list of all the created threads
thread_list = []

for i,url in enumerate(urls_list):
    thread = my_threads.ThreadsClass(i, url)
    thread.start()
    thread_list.append(thread)

#thread list join together to stops parallel process .join()
for th in thread_list:
    th.join()

#print end time
print("Second: ", (time.time_ns() - start) / 1_000_000_000)