import fdk
import json
import requests


def handler(ctx, data=None, loop=None):
    package = {
        "destination":"hongkong",
        "source":"Munich",
        "name":"balls",
        "id":"",
        "history":""

    }
    
    #For testing multiple locations.
    # destination = "" 
    # count = 0
    # for i in addresses['destinations']:
    #     if(count > 0) :
    #         destination += "|"
    #     destination += i
    #     count +=1
    
    req = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + package['source'][0] + '&destinations=' + package['destinations'][0] + '&key=AIzaSyD27N9mxT47VEQ3MX80dZZJa4_HdczBd_4&mode=transit')
    json_response = json.loads(req.content)['rows'][0]['elements'][0]

    if(json_response['status']=="\"ZERO_RESULTS\"" or json_response['distance']['value'] <50000):
        req = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + package['source'][0] + '&destinations=' + package['destinations'][0] + '&key=AIzaSyD27N9mxT47VEQ3MX80dZZJa4_HdczBd_4&mode=driving')
        json_response = json.loads(req.content)

    # json_response = json.dumps(json_response['rows'][0]['elements'][0]['status'])
    
    if(json_response=="ZERO_RESULTS" or json_response=="\"ZERO_RESULTS\""):
        return (json_response)

if __name__ == "__main__":
    fdk.handle(handler)



def findMin(output):
    elements = output['rows'][0]['elements']
    countInc = 0
    mindex = 0
    minDurVal = elements[0]['duration']['value']
    minDistVal = elements[0]['distance']['value']
    for i in elements:
        if(countInc==0):
            next
        if(i['duration']['value'] < minDurVal or i['distance']['value'] < minDistVal and i['duration']['value'] == minDurVal):
            mindex = countInc
            minDurVal = i['duration']['value']
        countInc+=1