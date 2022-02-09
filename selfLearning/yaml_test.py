import yaml

class readYml:
    def __init__(self,fileName):
       self.fileName = fileName

    def readFile(self):
        with open(self.fileName,encoding='utf-8') as f:
            yam_data=yaml.load(stream=f.read(),Loader=yaml.FullLoader)

    def writeFile(self):
        with open(self.fileName,encoding='utf-8',mode='w') as f:
            data=[{"test1": {"project":2,"test":3}},{"test2": {"project":4,"test":5}}]
            yaml.dump(data,stream=f,allow_unicode=True)

if __name__=='__main__':
    rc = readYml("yaml_data.yml")
    rc.readFile()
    rc.writeFile()