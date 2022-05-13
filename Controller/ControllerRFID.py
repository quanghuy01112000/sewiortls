import requests
import json
from Models.Anchor import Anchor
from Models.Tag import Tag


class ControllerRFID:
    def getAllAnchorData():
        # url = "https://demo.sewio.net/sensmapserver/api/anchors"
        url = "http://demo.sewio.net/sensmapserver/api/anchors"

        headers = {
            "X-ApiKey": "171555a8fe71148a165392904",
        }

        response = requests.request("GET", url, headers=headers)
        output=json.loads(response.text)
        print(response.text)
        print(output['results'])
        array = output['results']
        listAnchor = []
        for item in array:
            # print(item)
            id = item['id']
            title = item['title']
            datastreams = item['datastreams']
            current_value_posX, current_value_posY = '',''
            master = False
            for l in datastreams:
                print("id = ", l['id'])
                if l['id'] == 'posX':
                    current_value_posX = l['current_value']
                if l['id'] == 'posY':
                    current_value_posY = l['current_value']
                if l['id'] == 'master':
                    master = True
            anchor = Anchor(id,title,current_value_posX,current_value_posY,master)
            listAnchor.append(anchor)
        return listAnchor

    def getAllTagData():
        url = "http://demo.sewio.net/sensmapserver/api/tags"

        headers = {
            "X-ApiKey": "171555a8fe71148a165392904",
        }

        response = requests.request("GET", url, headers=headers)
        output=json.loads(response.text)
        print(response.text)
        print(output['results'])
        array = output['results']
        listTag = []
        for item in array:
            # print(item)
            id = item['id']
            title = item['title']
            des = item['description']
            location = item['location']
            print(location['ele'])
            if location['ele'].isalpha():
                tag = Tag(id,title,des)
                tag.setCheck(True)
                listTag.append(tag)
        return listTag



    # listAnchor = getAllAnchorData()
    # for anchor in listAnchor:
    #     anchor.printData()

    # listTag = getAllTagData()
    # for tag in listTag:
    #     tag.printData()

