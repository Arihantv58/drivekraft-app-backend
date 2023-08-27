url="https://api.chat-api.com/{}/sendMessage?token={}"
url_for_templates="https://api.chat-api.com/{}/sendTemplate?token={}"
api_token = "bfllgpii7xqb42zq"
api_instance = "instance294124"



nameSpace="73376c2d_a5cc_4aea_a5f8_fcde0de1be47"


def getTemplateName(name):
     switcher = {
         "otp":"otp"
    }
     return switcher.get(name, "nothing")