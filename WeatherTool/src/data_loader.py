import requests


class WeatherClient:
    """
    一个专门用于查询天气的客户端仪器。
    它会记住自己的配置（URL和语言），不用每次都重复告诉它。
    """

    def __init__(self, api_url, lang='zh'):
        """
        __init__ 是'构造函数'，在仪器出厂时执行一次，用来进行初始化设置。
        """
        self.api_url = api_url  # 记住：我的API地址是这个
        self.lang = lang  # 记住：我的默认语言是这个
        print(f"🔧 天气客户端已初始化 [URL: {self.api_url}, 语言: {self.lang}]")

    def fetch_weather(self, city_name):
        """
        这是仪器的一个功能（方法）。
        注意：它现在使用 'self.api_url'，而不是依赖外部的全局变量。
        """
        print(f"📡 正在通过 {self.api_url} 查询 {city_name}...")
        try:
            # 使用自己保存的配置来拼接 URL
            url = f"{self.api_url}/{city_name}?format=3&lang={self.lang}"

            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
            else:
                return f"查询失败 (状态码: {response.status_code})"
        except Exception as e:
            return f"网络错误: {e}"