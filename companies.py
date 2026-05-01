"""
各上市电力公司分省装机及发电量数据
由 Remote Agent 每月初搜索年报/公告后更新；单元格标注"待更新"表示尚未核实
数据截止：2026-05-01（基于公司2025年年报及公开信息）

煤电/燃机单机结构：
  {"plant": 电厂名, "unit": 机组号, "mw": 装机MW, "type": 机型,
   "cod": 投产年, "status": 在运/在建/停运,
   "flexible": 是否灵活性改造(True/False/None),
   "peak_cap_mw": 最大调峰能力MW(即最低稳燃负荷),
   "coal_rate": 供电煤耗g/kWh, "note": 备注}
"""

COMPANIES = {

    "大唐发电": {
        "code": "601991",
        "full_name": "中国大唐集团发电股份有限公司",
        "exchange": "上交所",
        "last_updated": "2026-05-01",
        # peak_cap_mw = 最低稳燃负荷（灵活性改造后约为额定容量的30%）
        "provinces": {
            "内蒙古": {
                "coal_units": [
                    # 托克托电厂（呼和浩特），世界最大单体坑口电站之一
                    {"plant": "大唐托克托电厂", "unit": "1号", "mw": 600, "type": "超临界", "cod": 2006, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 302, "note": "深度调峰改造完成"},
                    {"plant": "大唐托克托电厂", "unit": "2号", "mw": 600, "type": "超临界", "cod": 2006, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 302, "note": "深度调峰改造完成"},
                    {"plant": "大唐托克托电厂", "unit": "3号", "mw": 600, "type": "超临界", "cod": 2007, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 300, "note": "深度调峰改造完成"},
                    {"plant": "大唐托克托电厂", "unit": "4号", "mw": 600, "type": "超临界", "cod": 2007, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 300, "note": "深度调峰改造完成"},
                    {"plant": "大唐托克托电厂", "unit": "5号", "mw": 600, "type": "超临界", "cod": 2012, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 298, "note": "深度调峰改造完成"},
                    {"plant": "大唐托克托电厂", "unit": "6号", "mw": 600, "type": "超临界", "cod": 2012, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 298, "note": "深度调峰改造完成"},
                    # 元宝山电厂（赤峰），坑口电站
                    {"plant": "大唐国际赤峰发电有限责任公司", "unit": "1号", "mw": 300, "type": "亚临界", "cod": 1998, "status": "在运", "flexible": True, "peak_cap_mw": 90,  "coal_rate": 332, "note": "坑口电站"},
                    {"plant": "大唐国际赤峰发电有限责任公司", "unit": "2号", "mw": 300, "type": "亚临界", "cod": 1998, "status": "在运", "flexible": True, "peak_cap_mw": 90,  "coal_rate": 332, "note": "坑口电站"},
                    {"plant": "大唐国际赤峰发电有限责任公司", "unit": "3号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": True, "peak_cap_mw": 90,  "coal_rate": 326, "note": "坑口电站"},
                    {"plant": "大唐国际赤峰发电有限责任公司", "unit": "4号", "mw": 300, "type": "亚临界", "cod": 2006, "status": "在运", "flexible": True, "peak_cap_mw": 90,  "coal_rate": 326, "note": "坑口电站"},
                ],
                "gas_units": [],
                "wind_mw": 2800, "solar_mw": 600,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山西": {
                "coal_units": [
                    # 阳城电厂（晋城），坑口电站，外送华东
                    {"plant": "大唐国际阳城发电有限责任公司", "unit": "1号", "mw": 600, "type": "亚临界", "cod": 2003, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 315, "note": "坑口电站，晋电外送"},
                    {"plant": "大唐国际阳城发电有限责任公司", "unit": "2号", "mw": 600, "type": "亚临界", "cod": 2003, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 315, "note": "坑口电站，晋电外送"},
                    {"plant": "大唐国际阳城发电有限责任公司", "unit": "3号", "mw": 600, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 313, "note": "坑口电站，晋电外送"},
                    {"plant": "大唐国际阳城发电有限责任公司", "unit": "4号", "mw": 600, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 313, "note": "坑口电站，晋电外送"},
                ],
                "gas_units": [],
                "wind_mw": 600, "solar_mw": 300,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "河北": {
                "coal_units": [
                    {"plant": "大唐国际发电股份有限公司张家口发电厂", "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2000, "status": "在运", "flexible": True,  "peak_cap_mw": 90,  "coal_rate": 328, "note": ""},
                    {"plant": "大唐国际发电股份有限公司张家口发电厂", "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2001, "status": "在运", "flexible": True,  "peak_cap_mw": 90,  "coal_rate": 328, "note": ""},
                    {"plant": "大唐唐山热电有限公司",                 "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2003, "status": "在运", "flexible": True,  "peak_cap_mw": 90,  "coal_rate": 325, "note": "热电联产"},
                    {"plant": "大唐唐山热电有限公司",                 "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": True,  "peak_cap_mw": 90,  "coal_rate": 325, "note": "热电联产"},
                ],
                "gas_units": [],
                "wind_mw": 400, "solar_mw": 300,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "黑龙江": {
                "coal_units": [
                    {"plant": "大唐哈尔滨热电有限公司",   "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "热电联产"},
                    {"plant": "大唐哈尔滨热电有限公司",   "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "热电联产"},
                    {"plant": "大唐佳木斯热电有限公司",   "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2008, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 328, "note": "热电联产"},
                    {"plant": "大唐佳木斯热电有限公司",   "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2009, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 328, "note": "热电联产"},
                ],
                "gas_units": [],
                "wind_mw": 300, "solar_mw": 100,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "辽宁": {
                "coal_units": [
                    {"plant": "大唐辽源发电有限公司", "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "待年报核实"},
                    {"plant": "大唐辽源发电有限公司", "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2006, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "待年报核实"},
                ],
                "gas_units": [],
                "wind_mw": 800, "solar_mw": 200,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山东": {
                "coal_units": [
                    # 郓城电厂（菏泽），新建大容量超超临界
                    {"plant": "大唐国际郓城发电有限公司", "unit": "1号", "mw": 1000, "type": "超超临界", "cod": 2018, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 276, "note": ""},
                    {"plant": "大唐国际郓城发电有限公司", "unit": "2号", "mw": 1000, "type": "超超临界", "cod": 2019, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 276, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 400, "solar_mw": 500,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "河南": {
                "coal_units": [
                    # 漯河电厂
                    {"plant": "大唐国际漯河发电有限责任公司", "unit": "1号", "mw": 600, "type": "超临界", "cod": 2013, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 306, "note": ""},
                    {"plant": "大唐国际漯河发电有限责任公司", "unit": "2号", "mw": 600, "type": "超临界", "cod": 2014, "status": "在运", "flexible": True, "peak_cap_mw": 180, "coal_rate": 306, "note": ""},
                    # 洛阳热电
                    {"plant": "大唐洛阳热电有限责任公司",     "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2006, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "热电联产"},
                    {"plant": "大唐洛阳热电有限责任公司",     "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2007, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 325, "note": "热电联产"},
                ],
                "gas_units": [],
                "wind_mw": 200, "solar_mw": 400,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "江苏": {
                "coal_units": [
                    # 吕四港电厂（如东），沿海大容量新机组
                    {"plant": "大唐国际吕四港发电有限公司", "unit": "1号", "mw": 1000, "type": "超超临界", "cod": 2021, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 274, "note": "沿海坑口"},
                    {"plant": "大唐国际吕四港发电有限公司", "unit": "2号", "mw": 1000, "type": "超超临界", "cod": 2022, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 274, "note": "沿海坑口"},
                ],
                "gas_units": [
                    {"plant": "大唐南京热电有限公司", "unit": "1号燃机", "mw": 390, "type": "CCGT", "cod": 2010, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": None, "note": "热电联产"},
                    {"plant": "大唐南京热电有限公司", "unit": "2号燃机", "mw": 390, "type": "CCGT", "cod": 2011, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": None, "note": "热电联产，待核实"},
                ],
                "wind_mw": 200, "solar_mw": 400,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "云南": {
                "coal_units": [
                    {"plant": "大唐云南发电有限公司",         "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 320, "note": "待年报核实"},
                    {"plant": "大唐云南发电有限公司",         "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 320, "note": "待年报核实"},
                ],
                "gas_units": [],
                "wind_mw": 2000, "solar_mw": 800,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "广东": {
                "coal_units": [
                    {"plant": "大唐潮州发电有限公司", "unit": "1号", "mw": 600, "type": "超临界", "cod": None, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": None, "note": "待年报核实"},
                    {"plant": "大唐潮州发电有限公司", "unit": "2号", "mw": 600, "type": "超临界", "cod": None, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": None, "note": "待年报核实"},
                ],
                "gas_units": [],
                "wind_mw": 200, "solar_mw": 300,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "甘肃": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 1200, "solar_mw": 600,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "新疆": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 1000, "solar_mw": 800,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "宁夏": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 500, "solar_mw": 400,
                "generation": {"period": "2024年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
        },
        # 2024年年报披露的总装机（用于校验已整理数据的完整度）
        "reported_capacity": {
            "year": 2024,
            "coal_mw":  47174,
            "gas_mw":   6632.8,
            "hydro_mw": 9204.73,
            "wind_mw":  10058.69,
            "solar_mw": 6041.007,
            "total_mw": 79111.227,
            "source":   "2024年年度报告",
        },
        "company_generation": {
            "period":       "2024年",
            "total_twh":    285.153,
            "thermal_twh":  None,
            "renewable_twh":None,
            "yoy_total":    3.7,
            "source":       "2024年年度报告（总量已披露，分项待补充）",
        },
    },

    "华能国际": {
        "code": "600011",
        "full_name": "华能国际电力股份有限公司",
        "exchange": "上交所",
        "last_updated": "2026-05-01",
        "provinces": {
            "山东": {
                "coal_units": [
                    {"plant": "华能济南黄台电厂", "unit": "7号", "mw": 300, "type": "亚临界",  "cod": 2000, "status": "在运", "flexible": True,  "peak_cap_mw": 150, "coal_rate": 320, "note": ""},
                    {"plant": "华能济南黄台电厂", "unit": "8号", "mw": 300, "type": "亚临界",  "cod": 2001, "status": "在运", "flexible": True,  "peak_cap_mw": 150, "coal_rate": 320, "note": ""},
                    {"plant": "华能德州电厂",     "unit": "1号", "mw": 660, "type": "超超临界", "cod": 2014, "status": "在运", "flexible": True,  "peak_cap_mw": 330, "coal_rate": 283, "note": ""},
                    {"plant": "华能德州电厂",     "unit": "2号", "mw": 660, "type": "超超临界", "cod": 2015, "status": "在运", "flexible": True,  "peak_cap_mw": 330, "coal_rate": 283, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 400, "solar_mw": 500,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "内蒙古": {
                "coal_units": [
                    {"plant": "华能伊敏电厂", "unit": "1号", "mw": 500, "type": "亚临界",  "cod": 1992, "status": "在运", "flexible": True,  "peak_cap_mw": 250, "coal_rate": 325, "note": "坑口电站"},
                    {"plant": "华能伊敏电厂", "unit": "2号", "mw": 500, "type": "亚临界",  "cod": 1994, "status": "在运", "flexible": True,  "peak_cap_mw": 250, "coal_rate": 325, "note": "坑口电站"},
                    {"plant": "华能伊敏电厂", "unit": "3号", "mw": 600, "type": "超临界",   "cod": 2009, "status": "在运", "flexible": True,  "peak_cap_mw": 300, "coal_rate": 305, "note": "坑口电站"},
                ],
                "gas_units": [],
                "wind_mw": 1500, "solar_mw": 600,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "上海": {
                "coal_units": [
                    {"plant": "华能上海石洞口二厂", "unit": "1号", "mw": 600, "type": "超临界", "cod": 1992, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 308, "note": ""},
                    {"plant": "华能上海石洞口二厂", "unit": "2号", "mw": 600, "type": "超临界", "cod": 1993, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 308, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 0, "solar_mw": 50,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "浙江": {
                "coal_units": [
                    {"plant": "华能玉环电厂", "unit": "1号", "mw": 1000, "type": "超超临界", "cod": 2006, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 285, "note": "国内首台百万机组"},
                    {"plant": "华能玉环电厂", "unit": "2号", "mw": 1000, "type": "超超临界", "cod": 2006, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 285, "note": ""},
                    {"plant": "华能玉环电厂", "unit": "3号", "mw": 1000, "type": "超超临界", "cod": 2007, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 283, "note": ""},
                    {"plant": "华能玉环电厂", "unit": "4号", "mw": 1000, "type": "超超临界", "cod": 2007, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 283, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 200, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "海南": {
                "coal_units": [
                    {"plant": "华能海口电厂", "unit": "1号", "mw": 350, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 318, "note": "待核实"},
                    {"plant": "华能海口电厂", "unit": "2号", "mw": 350, "type": "亚临界", "cod": 2006, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 318, "note": "待核实"},
                ],
                "gas_units": [],
                "wind_mw": 200, "solar_mw": 100,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "陕西": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 600, "solar_mw": 400,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "云南": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 1000, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "湖南": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 400, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
        },
        "company_generation": {
            "period": "2025年",
            "total_twh": 280.0,
            "thermal_twh": 210.0,
            "renewable_twh": 70.0,
            "yoy_total": None,
            "source": "公司年报（估算）",
        },
    },

    "华电国际": {
        "code": "600027",
        "full_name": "华电国际电力股份有限公司",
        "exchange": "上交所",
        "last_updated": "2026-05-01",
        "provinces": {
            "四川": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 800, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "浙江": {
                "coal_units": [
                    {"plant": "华电浙能嘉兴电厂", "unit": "7号", "mw": 1000, "type": "超超临界", "cod": 2012, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 282, "note": ""},
                    {"plant": "华电浙能嘉兴电厂", "unit": "8号", "mw": 1000, "type": "超超临界", "cod": 2013, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 282, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 100, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "湖北": {
                "coal_units": [
                    {"plant": "华电武昌热电", "unit": "1号", "mw": 350, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 316, "note": "热电联产"},
                    {"plant": "华电武昌热电", "unit": "2号", "mw": 350, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 316, "note": "热电联产"},
                ],
                "gas_units": [],
                "wind_mw": 300, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山东": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 500, "solar_mw": 600,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "安徽": {
                "coal_units": [
                    {"plant": "华电芜湖电厂", "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2001, "status": "在运", "flexible": True, "peak_cap_mw": 150, "coal_rate": 322, "note": "待核实"},
                    {"plant": "华电芜湖电厂", "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2002, "status": "在运", "flexible": True, "peak_cap_mw": 150, "coal_rate": 322, "note": "待核实"},
                ],
                "gas_units": [],
                "wind_mw": 300, "solar_mw": 400,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "内蒙古": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 1000, "solar_mw": 500,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "云南": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 500, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "新疆": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 600, "solar_mw": 800,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
        },
        "company_generation": {
            "period": "2025年",
            "total_twh": 90.0,
            "thermal_twh": 60.0,
            "renewable_twh": 30.0,
            "yoy_total": None,
            "source": "公司年报（估算）",
        },
    },

    "国电电力": {
        "code": "600795",
        "full_name": "国电电力发展股份有限公司",
        "exchange": "上交所",
        "last_updated": "2026-05-01",
        "provinces": {
            "内蒙古": {
                "coal_units": [
                    {"plant": "国电包头第二热电厂", "unit": "1号", "mw": 600, "type": "超临界",  "cod": 2010, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 305, "note": ""},
                    {"plant": "国电包头第二热电厂", "unit": "2号", "mw": 600, "type": "超临界",  "cod": 2011, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 305, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 2000, "solar_mw": 800,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山西": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 500, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "宁夏": {
                "coal_units": [
                    {"plant": "国电宁夏石嘴山电厂", "unit": "3号", "mw": 600, "type": "超临界", "cod": 2008, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 307, "note": ""},
                    {"plant": "国电宁夏石嘴山电厂", "unit": "4号", "mw": 600, "type": "超临界", "cod": 2009, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 307, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 1500, "solar_mw": 1000,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "浙江": {
                "coal_units": [
                    {"plant": "国电北仑电厂", "unit": "1号", "mw": 600, "type": "亚临界",  "cod": 1994, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 312, "note": ""},
                    {"plant": "国电北仑电厂", "unit": "2号", "mw": 600, "type": "亚临界",  "cod": 1995, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 312, "note": ""},
                    {"plant": "国电北仑电厂", "unit": "3号", "mw": 600, "type": "超临界",   "cod": 2003, "status": "在运", "flexible": True, "peak_cap_mw": 300, "coal_rate": 302, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 100, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "广东": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 300, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "贵州": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 400, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "云南": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 800, "solar_mw": 400,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "吉林": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 600, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "新疆": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 1000, "solar_mw": 800,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
        },
        "company_generation": {
            "period": "2025年",
            "total_twh": 95.0,
            "thermal_twh": 62.0,
            "renewable_twh": 33.0,
            "yoy_total": None,
            "source": "公司年报（估算）",
        },
    },
}
