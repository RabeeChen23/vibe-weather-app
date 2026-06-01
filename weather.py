import random

weather_data = {
    "北京": {"温度": "22°C", "天气": "晴", "湿度": "45%"},
    "上海": {"温度": "28°C", "天气": "多云", "湿度": "65%"},
    "广州": {"温度": "31°C", "天气": "雷阵雨", "湿度": "80%"},
}

city, info = random.choice(list(weather_data.items()))
_ = 1 / 0
print(f"{city}: {info['天气']}，{info['温度']}，湿度 {info['湿度']}")
