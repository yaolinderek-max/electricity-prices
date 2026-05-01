"""
各省电力基础数据：电网分区、燃煤基准价、机制电价、现货市场状态
数据来源：国家发改委、各省电力交易中心，截至2026年3月
"""

# 省份基础数据：(省份名, 电网分区, 燃煤基准价元/kWh, 是否开通现货市场)
PROVINCES = [
    # 华北
    {"name": "北京",   "grid": "华北",  "coal_benchmark": 0.3753, "spot": False},
    {"name": "天津",   "grid": "华北",  "coal_benchmark": 0.3825, "spot": False},
    {"name": "河北南", "grid": "华北",  "coal_benchmark": 0.3762, "spot": False},
    {"name": "河北北", "grid": "华北",  "coal_benchmark": 0.3722, "spot": False},
    {"name": "山西",   "grid": "华北",  "coal_benchmark": 0.3219, "spot": True},
    {"name": "蒙西",   "grid": "华北",  "coal_benchmark": 0.2677, "spot": True},

    # 东北
    {"name": "辽宁",   "grid": "东北",  "coal_benchmark": 0.3794, "spot": True},
    {"name": "吉林",   "grid": "东北",  "coal_benchmark": 0.3472, "spot": False},
    {"name": "黑龙江", "grid": "东北",  "coal_benchmark": 0.3626, "spot": False},
    {"name": "蒙东",   "grid": "东北",  "coal_benchmark": 0.2945, "spot": False},

    # 华东
    {"name": "上海",   "grid": "华东",  "coal_benchmark": 0.4155, "spot": False},
    {"name": "江苏",   "grid": "华东",  "coal_benchmark": 0.3911, "spot": True},
    {"name": "浙江",   "grid": "华东",  "coal_benchmark": 0.4153, "spot": True},
    {"name": "安徽",   "grid": "华东",  "coal_benchmark": 0.3844, "spot": True},
    {"name": "福建",   "grid": "华东",  "coal_benchmark": 0.3932, "spot": False},

    # 华中
    {"name": "河南",   "grid": "华中",  "coal_benchmark": 0.3779, "spot": False},
    {"name": "湖北",   "grid": "华中",  "coal_benchmark": 0.4234, "spot": True},
    {"name": "湖南",   "grid": "华中",  "coal_benchmark": 0.4532, "spot": False},
    {"name": "江西",   "grid": "华中",  "coal_benchmark": 0.4383, "spot": False},
    {"name": "重庆",   "grid": "华中",  "coal_benchmark": 0.3963, "spot": False},
    {"name": "四川",   "grid": "华中",  "coal_benchmark": 0.3595, "spot": True},

    # 华南（南方电网）
    {"name": "广东",   "grid": "南方",  "coal_benchmark": 0.4530, "spot": True},
    {"name": "广西",   "grid": "南方",  "coal_benchmark": 0.4282, "spot": False},
    {"name": "云南",   "grid": "南方",  "coal_benchmark": 0.3320, "spot": False},
    {"name": "贵州",   "grid": "南方",  "coal_benchmark": 0.3498, "spot": False},
    {"name": "海南",   "grid": "南方",  "coal_benchmark": 0.4155, "spot": False},

    # 西北
    {"name": "山东",   "grid": "山东",  "coal_benchmark": 0.3932, "spot": True},
    {"name": "陕西",   "grid": "西北",  "coal_benchmark": 0.3233, "spot": True},
    {"name": "甘肃",   "grid": "西北",  "coal_benchmark": 0.2978, "spot": True},
    {"name": "宁夏",   "grid": "西北",  "coal_benchmark": 0.2595, "spot": False},
    {"name": "青海",   "grid": "西北",  "coal_benchmark": 0.3247, "spot": False},
    {"name": "新疆",   "grid": "西北",  "coal_benchmark": 0.2500, "spot": False},

    # 西藏
    {"name": "西藏",   "grid": "西藏",  "coal_benchmark": 0.2500, "spot": False},
]

# 各省机制电价（新能源"136号文"落地，按光伏/风电分，元/kWh，2025-2026年）
MECHANISM_PRICES = {
    "上海":   {"wind": 0.4155, "solar": 0.4155, "note": ""},
    "浙江":   {"wind": 0.4100, "solar": 0.3800, "note": "约值，竞价区间"},
    "安徽":   {"wind": 0.3900, "solar": 0.3700, "note": "约值，竞价区间"},
    "福建":   {"wind": 0.3932, "solar": 0.3500, "note": "参考值"},
    "江苏":   {"wind": 0.3800, "solar": 0.3600, "note": "参考值"},
    "广东":   {"wind": 0.4530, "solar": 0.4530, "note": "存量参考燃煤基准价"},
    "海南":   {"wind": 0.4155, "solar": 0.4155, "note": ""},
    "湖南":   {"wind": 0.4500, "solar": 0.4200, "note": "机制电量约值"},
    "湖北":   {"wind": 0.3870, "solar": 0.3330, "note": ""},
    "江西":   {"wind": 0.3750, "solar": 0.3300, "note": ""},
    "河南":   {"wind": 0.3779, "solar": 0.3500, "note": "参考值"},
    "重庆":   {"wind": 0.3963, "solar": 0.3963, "note": "竞价出清"},
    "四川":   {"wind": 0.3595, "solar": 0.3200, "note": "参考值"},
    "山东":   {"wind": 0.3190, "solar": 0.2250, "note": ""},
    "山西":   {"wind": 0.3219, "solar": 0.3000, "note": "参考值"},
    "陕西":   {"wind": 0.3233, "solar": 0.2800, "note": "参考值"},
    "甘肃":   {"wind": 0.1954, "solar": 0.1954, "note": "风光同场"},
    "宁夏":   {"wind": 0.2595, "solar": 0.2200, "note": "参考值"},
    "青海":   {"wind": 0.2400, "solar": 0.2277, "note": ""},
    "新疆":   {"wind": 0.2100, "solar": 0.1500, "note": ""},
    "云南":   {"wind": 0.3320, "solar": 0.3300, "note": ""},
    "贵州":   {"wind": 0.3498, "solar": 0.3200, "note": "参考值"},
    "辽宁":   {"wind": 0.3794, "solar": 0.3400, "note": "参考值"},
    "吉林":   {"wind": 0.3472, "solar": 0.3000, "note": "参考值"},
    "黑龙江": {"wind": 0.3626, "solar": 0.3200, "note": "参考值"},
    "蒙西":   {"wind": 0.2677, "solar": 0.2400, "note": "参考值"},
    "蒙东":   {"wind": 0.2945, "solar": 0.2600, "note": "参考值"},
    "北京":   {"wind": 0.3753, "solar": 0.3500, "note": "参考值"},
    "天津":   {"wind": 0.3825, "solar": 0.3600, "note": "参考值"},
    "河北南": {"wind": 0.3762, "solar": 0.3400, "note": "参考值"},
    "河北北": {"wind": 0.3722, "solar": 0.3300, "note": "参考值"},
    "广西":   {"wind": 0.4282, "solar": 0.3800, "note": "参考值"},
    "西藏":   {"wind": 0.2500, "solar": 0.1500, "note": "分类标杆电价"},
}

# 各省中长期月度成交均价（元/kWh）
# 由 Remote Agent 每月初自动更新；标注"估算"表示非官方数据
MONTHLY_CONTRACT_PRICES = {
    # 省份: {"price": 均价, "period": "YYYY-MM", "source": "来源", "note": ""}
    "广东":  {"price": 0.4650, "period": "2026-05", "source": "广东电力交易中心", "note": "估算"},
    "山东":  {"price": 0.3800, "period": "2026-05", "source": "山东电力交易中心", "note": "估算"},
    "浙江":  {"price": 0.4100, "period": "2026-05", "source": "浙江电力交易中心", "note": "估算"},
    "江苏":  {"price": 0.3950, "period": "2026-05", "source": "江苏电力交易中心", "note": "估算"},
    "安徽":  {"price": 0.3750, "period": "2026-05", "source": "安徽电力交易中心", "note": "估算"},
    "湖北":  {"price": 0.4050, "period": "2026-05", "source": "湖北电力交易中心", "note": "估算"},
    "湖南":  {"price": 0.4300, "period": "2026-05", "source": "湖南电力交易中心", "note": "估算"},
    "山西":  {"price": 0.3000, "period": "2026-05", "source": "山西电力交易中心", "note": "估算"},
    "陕西":  {"price": 0.3050, "period": "2026-05", "source": "陕西电力交易中心", "note": "估算"},
    "蒙西":  {"price": 0.2500, "period": "2026-05", "source": "蒙西电力交易中心", "note": "估算"},
    "辽宁":  {"price": 0.3600, "period": "2026-05", "source": "辽宁电力交易中心", "note": "估算"},
    "四川":  {"price": 0.3200, "period": "2026-05", "source": "四川电力交易中心", "note": "估算"},
    "重庆":  {"price": 0.3700, "period": "2026-05", "source": "重庆电力交易中心", "note": "估算"},
    "云南":  {"price": 0.2800, "period": "2026-05", "source": "云南电力交易中心", "note": "估算"},
    "广西":  {"price": 0.4000, "period": "2026-05", "source": "广西电力交易中心", "note": "估算"},
    "甘肃":  {"price": 0.2600, "period": "2026-05", "source": "甘肃电力交易中心", "note": "估算"},
    "宁夏":  {"price": 0.2400, "period": "2026-05", "source": "宁夏电力交易中心", "note": "估算"},
    "新疆":  {"price": 0.2200, "period": "2026-05", "source": "新疆电力交易中心", "note": "估算"},
}

# 分时电价（一般工商业1-10kV，峰/平/谷，元/kWh，2026年1月数据）
TIME_OF_USE_PRICES = {
    "广东":   {"peak": 1.4376, "flat": 0.7584, "valley": 0.2799, "note": "珠三角五市"},
    "海南":   {"peak": 1.5080, "flat": 0.9174, "valley": 0.3909, "note": ""},
    "湖南":   {"peak": 1.4273, "flat": 0.7644, "valley": 0.3615, "note": ""},
    "山东":   {"peak": 1.2751, "flat": 0.6876, "valley": 0.2530, "note": ""},
    "浙江":   {"peak": 1.1500, "flat": 0.7200, "valley": 0.3500, "note": "约值"},
    "上海":   {"peak": 1.0800, "flat": 0.7000, "valley": 0.3200, "note": "约值"},
    "江苏":   {"peak": 1.0500, "flat": 0.6800, "valley": 0.3100, "note": "约值"},
    "安徽":   {"peak": 0.9800, "flat": 0.6200, "valley": 0.2900, "note": "约值"},
    "湖北":   {"peak": 1.0000, "flat": 0.6500, "valley": 0.3000, "note": "约值"},
    "福建":   {"peak": 0.9500, "flat": 0.6100, "valley": 0.2800, "note": "约值"},
    "河南":   {"peak": 0.9200, "flat": 0.5900, "valley": 0.2700, "note": "约值"},
    "江西":   {"peak": 0.9500, "flat": 0.6200, "valley": 0.2900, "note": "约值"},
    "重庆":   {"peak": 0.8800, "flat": 0.5600, "valley": 0.2600, "note": "约值"},
    "四川":   {"peak": 0.8500, "flat": 0.5400, "valley": 0.2400, "note": "约值"},
    "山西":   {"peak": 0.7500, "flat": 0.4900, "valley": 0.2200, "note": "约值"},
    "河北南": {"peak": 0.9100, "flat": 0.5800, "valley": 0.2600, "note": "约值"},
    "河北北": {"peak": 0.8800, "flat": 0.5600, "valley": 0.2500, "note": "约值"},
    "北京":   {"peak": 0.9500, "flat": 0.6000, "valley": 0.3000, "note": "约值"},
    "天津":   {"peak": 0.9200, "flat": 0.5900, "valley": 0.2700, "note": "约值"},
    "辽宁":   {"peak": 0.8800, "flat": 0.5600, "valley": 0.2600, "note": "约值"},
    "吉林":   {"peak": 0.8200, "flat": 0.5200, "valley": 0.2400, "note": "约值"},
    "黑龙江": {"peak": 0.8500, "flat": 0.5400, "valley": 0.2500, "note": "约值"},
    "蒙西":   {"peak": 0.6200, "flat": 0.4000, "valley": 0.1800, "note": "约值"},
    "蒙东":   {"peak": 0.7000, "flat": 0.4500, "valley": 0.2000, "note": "约值"},
    "陕西":   {"peak": 0.7800, "flat": 0.4900, "valley": 0.2200, "note": "约值"},
    "甘肃":   {"peak": 0.6800, "flat": 0.4300, "valley": 0.1900, "note": "约值"},
    "宁夏":   {"peak": 0.5500, "flat": 0.3500, "valley": 0.1600, "note": "约值"},
    "青海":   {"peak": 0.6500, "flat": 0.4200, "valley": 0.1900, "note": "约值"},
    "新疆":   {"peak": 0.3800, "flat": 0.2500, "valley": 0.0800, "note": "约值"},
    "云南":   {"peak": 0.7000, "flat": 0.4500, "valley": 0.2100, "note": "约值"},
    "贵州":   {"peak": 0.7500, "flat": 0.4800, "valley": 0.2200, "note": "约值"},
    "广西":   {"peak": 0.9500, "flat": 0.6100, "valley": 0.2800, "note": "约值"},
    "西藏":   {"peak": 0.7000, "flat": 0.4500, "valley": 0.2000, "note": "约值"},
}
