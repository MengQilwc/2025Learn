import config
from src.data_loader import WeatherClient  # 注意：这次导入的是类名
from src import utils


def run():
    print("欢迎使用面向对象版天气工具！")

    # === 关键变化点 START ===
    # 1. 实例化 (Instantiation)：根据图纸制造出一台具体的仪器
    # 我们把配置传给它，它以后就记住了，不用再传了。
    my_client = WeatherClient(api_url=config.WEATHER_API_URL, lang=config.LANG)
    # === 关键变化点 END ===

    while True:
        city = input("\n请输入城市拼音 (直接回车退出): ").strip()
        if not city:
            break

        # 2. 调用方法：使用这台仪器特定的功能
        # 注意：我们不再需要传 URL 等配置信息了，仪器自己知道。
        weather_data = my_client.fetch_weather(city)

        print(utils.make_pretty_output(weather_data))


if __name__ == '__main__':
    run()