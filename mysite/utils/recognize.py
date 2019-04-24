from aip import AipOcr


class Character_View():
    def __init__(self):
        """ 你的 APPID AK SK """
        APP_ID = '16040536'
        API_KEY = 'aCiGQ7gP7GceRREckMgy7S5K'
        SECRET_KEY = 'TpUXmvH3K7rTXkjKjvTuDT6qbkOguEUp'

        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def char(self,filepath=None):
        # 前端传递文件进来执行识别
        image = self.get_file_content(filepath)

        # """ 调用通用文字识别, 图片参数为本地图片 """
        # self.client.basicGeneral(image)

        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        resp = self.client.basicGeneral(image, options)
        # print(resp)
        list = []
        for i in resp['words_result']:
            word = i['words']
            list.append(word)
        with open('./test.txt', 'w') as f:
            for i in list:
                f.writelines(i + "\n")
        with open('./test.txt', 'r') as f:
            content = f.read()
            print('识别到的内容是：%s' % f.read())
        return content
