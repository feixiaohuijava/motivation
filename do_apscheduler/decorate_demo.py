import time
try:
    current_time = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
    print type(current_time)
    file_object = open('insert_data','w+')
    file_object.write(current_time)
except Exception,e:
    print e
finally:
    file_object.close()