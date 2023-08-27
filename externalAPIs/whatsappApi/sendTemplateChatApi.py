import requests
import json
import logging

from configuration.chatApi import url_for_templates,api_instance,api_token,getTemplateName,nameSpace



def sendTemplate(templateName, parameters, urlParameters, contactNumber):
    url = url_for_templates.format(api_instance, api_token)
    parametersInJson = getParametersInJson(parameters, urlParameters)

    payload = json.dumps({
        "template": getTemplateName(templateName),
        "language": {
            "policy": "deterministic",
            "code": "en"
        },
        "namespace": nameSpace,
        "params": parametersInJson,
        "phone": contactNumber
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    logging.info('Template Send to {}'.format(contactNumber, ))
    logging.info("API resposne : {}".format(response.text))
    return (response.text)
    #return True


def sendBasicTemplates(templateName,contact):
    url = url_for_templates.format(api_instance, api_token)
    payload = json.dumps({
        "template": getTemplateName(templateName),
        "language": {
            "policy": "deterministic",
            "code": "en"
        },
        "namespace": nameSpace,
        "phone": contact
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    logging.info('Template Send to {}'.format(contact, ))
    logging.info("API resposne : {}".format(response.text))
    return (response.text)
    #return True




def getParametersInJson(parameters, urlParameters):
    params = list()

    if len(parameters) != 0:
        tempDict = dict()
        tempDict['type'] = 'body'
        tempDict['parameters'] = list()

        for param in parameters:
            secondTempDict = dict()
            secondTempDict["type"] = "text"
            secondTempDict["text"] = str(param)

            tempDict["parameters"].append(secondTempDict)
        params.append(tempDict)

    if len(urlParameters) != 0:
        counter = 0
        for val in urlParameters:
            tempDict = dict()
            tempDict['type'] = 'button'
            tempDict['index'] = str(counter)
            tempDict['sub_type'] = 'url'
            tempDict['parameters'] = list()

            secondTempDict = dict()
            secondTempDict["type"] = "text"
            secondTempDict["text"] = val
            tempDict['parameters'].append(secondTempDict)

            params.append(tempDict)
            counter = counter + 1

    return params

