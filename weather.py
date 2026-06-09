import random

weather_data = {
    "北京": {"温度": "22°C", "天气": "晴", "湿度": "45%"},
    "上海": {"温度": "28°C", "天气": "多云", "湿度": "65%"},
    "广州": {"温度": "31°C", "天气": "雷阵雨", "湿度": "80%"},
}

GOOD_WEATHER = {"晴", "多云"}
BAD_WEATHER = {"雷阵雨", "雨", "雪", "阴"}

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

city, info = random.choice(list(weather_data.items()))
weather = info["天气"]

if weather in GOOD_WEATHER:
    color = GREEN
elif weather in BAD_WEATHER:
    color = RED
else:
    color = YELLOW

line = f"{city}: {info['天气']}，{info['温度']}，湿度 {info['湿度']}"
print(f"{color}{line}{RESET}")
