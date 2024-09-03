import json

class ConfigProcessor:
    def __init__(self):
        pass


    def AddData(self, path, x1, y1, x2, y2):
        data_ = {
            "x1" : x1,
            "y1" : y1,
            "x2" : x2,
            "y2" : y2,
        }
        json_data = json.dumps(data_, indent=4)
        with open(path, "w") as file:
            file.write(json_data)
            file.close()


    def ReadData(self, path):
        with open(path, "r") as file:
            json_content = file.read()
            data_ = json.loads(json_content)
            return (data_["x1"], data_["y1"], data_["x2"], data_["y2"])