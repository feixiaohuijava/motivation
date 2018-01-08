
import datetime
import random

class  middleware_record_req_rsp(object):

    def __init__(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0,1000)
        uniqueNum = str(nowTime) + str(randomNum)
        self.flag = uniqueNum

    def process_request(self,request):
        if request.method == 'POST':
            x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
            request_ip = x_forward_for.split(',')[0] if x_forward_for else request.META.get('REMOTE_ADDR')
            request_user = request.META.get('USER')
            re_request_body = getattr(request,'_body',request.body)
            flag = self.flag
        return None

    def process_response(self,request,response):
        if request.method == 'POST':
            flag = self.flag
            response_status_code = response.status_code
        return response
