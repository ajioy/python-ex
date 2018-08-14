import time
import threading

# 共享变量实现通信
detail_url_list = []

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop() # 非线程安全操作
            print(url)
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")



def get_detail_url(detail_url_list):
    # 爬取文章列表页
    while True:
       print("get detail url started")
       time.sleep(4)
       for i in range(20):
           detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
       print("get detail url end")

if __name__ == "__main__":
    start_time = time.time()
    thread1 = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(5):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
        #html_thread.join()


    thread1.start()
    #thread1.join()

    print("last time:%f" % (time.time() - start_time))
