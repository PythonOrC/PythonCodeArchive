#encoding=utf8
from wox import Wox, WoxAPI
import os

class Main(Wox):
    def query(self, query):
        self.query = query
        results = [{
                "Title": 'Open Minecraft',
                'Subtitle': None,
                "IcoPath":"Images/minecraft.png",
                "JsonRPCAction":{'method': 'change_query',
                                 'parameters': None,
                                 'dontHideAfterAction': True}
                
            }]
        with open('query.txt', 'a') as f:
            f.write(self.query)
        return results

    def change_query(query):
        os.popen('E:\Personal\Minecraft\Minecraft.exe')

if __name__ == '__main__':
    Main()