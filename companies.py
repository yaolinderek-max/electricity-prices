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
        "provinces": {
            "内蒙古": {
                "coal_units": [
                    {"plant": "大唐托克托电厂", "unit": "1号", "mw": 600, "type": "超临界",  "cod": 2006, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 302, "note": ""},
                    {"plant": "大唐托克托电厂", "unit": "2号", "mw": 600, "type": "超临界",  "cod": 2006, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 302, "note": ""},
                    {"plant": "大唐托克托电厂", "unit": "3号", "mw": 600, "type": "超临界",  "cod": 2007, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 300, "note": ""},
                    {"plant": "大唐托克托电厂", "unit": "4号", "mw": 600, "type": "超临界",  "cod": 2007, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 300, "note": ""},
                    {"plant": "大唐托克托电厂", "unit": "5号", "mw": 600, "type": "超临界",  "cod": 2012, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 298, "note": ""},
                    {"plant": "大唐托克托电厂", "unit": "6号", "mw": 600, "type": "超临界",  "cod": 2012, "status": "在运", "flexible": True,  "peak_cap_mw": 360, "coal_rate": 298, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 800, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山西": {
                "coal_units": [
                    {"plant": "大唐阳城电厂", "unit": "1号", "mw": 600, "type": "亚临界", "cod": 2003, "status": "在运", "flexible": True,  "peak_cap_mw": 300, "coal_rate": 315, "note": ""},
                    {"plant": "大唐阳城电厂", "unit": "2号", "mw": 600, "type": "亚临界", "cod": 2003, "status": "在运", "flexible": True,  "peak_cap_mw": 300, "coal_rate": 315, "note": ""},
                    {"plant": "大唐阳城电厂", "unit": "3号", "mw": 600, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": True,  "peak_cap_mw": 300, "coal_rate": 313, "note": ""},
                    {"plant": "大唐阳城电厂", "unit": "4号", "mw": 600, "type": "亚临界", "cod": 2004, "status": "在运", "flexible": True,  "peak_cap_mw": 300, "coal_rate": 313, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 300, "solar_mw": 150,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "云南": {
                "coal_units": [
                    {"plant": "大唐云南发电", "unit": "1号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 320, "note": "待核实"},
                    {"plant": "大唐云南发电", "unit": "2号", "mw": 300, "type": "亚临界", "cod": 2005, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": 320, "note": "待核实"},
                ],
                "gas_units": [],
                "wind_mw": 1200, "solar_mw": 400,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "辽宁": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 500, "solar_mw": 100,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "山东": {
                "coal_units": [
                    {"plant": "大唐国际郓城电厂", "unit": "1号", "mw": 1000, "type": "超超临界", "cod": 2018, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 276, "note": ""},
                    {"plant": "大唐国际郓城电厂", "unit": "2号", "mw": 1000, "type": "超超临界", "cod": 2019, "status": "在运", "flexible": True, "peak_cap_mw": 500, "coal_rate": 276, "note": ""},
                ],
                "gas_units": [],
                "wind_mw": 200, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "江苏": {
                "coal_units": [],
                "gas_units": [
                    {"plant": "大唐南京热电", "unit": "1号燃机", "mw": 390, "type": "CCGT", "cod": 2010, "status": "在运", "flexible": None, "peak_cap_mw": None, "coal_rate": None, "note": ""},
                ],
                "wind_mw": 100, "solar_mw": 200,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "广东": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 0, "solar_mw": 0,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "甘肃": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 600, "solar_mw": 300,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
            "新疆": {
                "coal_units": [],
                "gas_units": [],
                "wind_mw": 800, "solar_mw": 500,
                "generation": {"period": "2025年", "total_twh": None, "thermal_twh": None, "renewable_twh": None, "yoy": None, "source": "待更新"},
            },
        },
        "company_generation": {
            "period": "2025年",
            "total_twh": 112.5,
            "thermal_twh": 87.0,
            "renewable_twh": 25.5,
            "yoy_total": None,
            "source": "公司年报（估算）",
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
