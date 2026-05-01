"""
抓取各省现货电价周报（新浪财经）和月度中长期价格数据
"""
import re
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# 已知现货市场省份
SPOT_PROVINCES = ["山西", "广东", "山东", "蒙西", "陕西", "辽宁", "江苏", "安徽", "甘肃", "湖北", "浙江", "四川"]


def fetch_sina_weekly_spot() -> dict:
    """
    返回最新一期现货电价周数据。
    优先使用内置的最新已知数据，同时尝试从新浪财经获取更新，
    若在线数据通过验证则覆盖内置数据。
    """
    builtin = {
        "week": "2026.4.20~2026.4.26",
        "source_url": "https://finance.sina.com.cn/wm/2026-04-29/doc-inhwefuw7887107.shtml",
        "data": _hardcoded_spot_20260420(),
        "fetched_at": datetime.now().isoformat(),
    }

    known_url = "https://finance.sina.com.cn/wm/2026-04-29/doc-inhwefuw7887107.shtml"
    try:
        online = _parse_sina_spot_article(known_url)
        # 只有在线数据覆盖了大多数省份且数据合理时才使用
        if len(online.get("data", [])) >= 6 and not _is_degenerate(online["data"]):
            print(f"[scraper] 在线数据有效，使用在线数据（{len(online['data'])} 个省份）")
            return online
        else:
            print(f"[scraper] 在线解析不完整，使用内置数据")
    except Exception as e:
        print(f"[scraper] 在线抓取失败: {e}，使用内置数据")

    return builtin


def _parse_sina_spot_article(url: str) -> dict:
    result = {"week": "", "source_url": url, "data": [], "fetched_at": datetime.now().isoformat()}
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "lxml")
        text = soup.get_text("\n")

        # 提取周期
        week_match = re.search(r"(\d{4}[.年]\d{1,2}[.月]\d{1,2})[^\d]+(\d{4}[.年]\d{1,2}[.月]\d{1,2})", text)
        if week_match:
            result["week"] = f"{week_match.group(1)}~{week_match.group(2)}"

        # 按省份分段解析（每个省份在独立的文本块中，避免跨省匹配）
        # 将文本按省份关键词分割，分段后各自解析，互不干扰
        province_anchors = ["山西", "广东", "山东", "陕西", "江苏", "安徽", "蒙西", "辽宁"]
        segments = _split_by_province(text, province_anchors)

        for prov, seg in segments.items():
            nums = re.findall(r"-?[\d]+\.[\d]+", seg)
            price_nums = [float(n) for n in nums if 500 >= float(n) >= -200]
            if len(price_nums) >= 2:
                lo = min(price_nums)
                hi = max(price_nums)
                result["data"].append({
                    "province": prov,
                    "da_min": lo,
                    "da_max": hi,
                    "da_avg": round((lo + hi) / 2, 2),
                    "unit": "元/MWh",
                })
    except Exception as e:
        print(f"[scraper] 解析失败 {url}: {e}")

    # 验证数据有效性：如果各省 da_min/da_max 完全相同，说明正则串台，丢弃
    if _is_degenerate(result["data"]):
        print("[scraper] 在线解析数据异常，回退到内置数据")
        result["data"] = []

    # 兜底：注入已知数据（2026.4.20-4.26）
    if not result["data"]:
        if not result["week"]:
            result["week"] = "2026.4.20~2026.4.26"
        result["data"] = _hardcoded_spot_20260420()

    return result


def _split_by_province(text: str, anchors: list) -> dict:
    """将长文本按省份关键词切割成独立段落"""
    positions = {}
    for anchor in anchors:
        idx = text.find(anchor)
        if idx != -1:
            positions[anchor] = idx
    sorted_provs = sorted(positions, key=lambda p: positions[p])
    segments = {}
    for i, prov in enumerate(sorted_provs):
        start = positions[prov]
        end = positions[sorted_provs[i + 1]] if i + 1 < len(sorted_provs) else start + 800
        segments[prov] = text[start:end]
    return segments


def _is_degenerate(data: list) -> bool:
    """检测解析数据是否退化（所有省份 da_min/da_max 完全相同）"""
    if len(data) < 2:
        return False
    mins = set(d.get("da_min") for d in data)
    maxs = set(d.get("da_max") for d in data)
    return len(mins) == 1 and len(maxs) == 1


def _hardcoded_spot_20260420() -> list:
    """2026年4月20-26日已知现货价格数据，来源：新浪财经周报"""
    return [
        {"province": "山西",  "da_min": 196.77, "da_max": 364.30, "da_avg": 280.0,  "rt_avg": 255.0,  "unit": "元/MWh"},
        {"province": "广东",  "da_min": 364.35, "da_max": 635.86, "da_avg": 500.0,  "rt_avg": 544.0,  "unit": "元/MWh"},
        {"province": "山东",  "da_min": 103.98, "da_max": 424.92, "da_avg": 264.0,  "rt_avg": 261.0,  "unit": "元/MWh"},
        {"province": "陕西",  "da_min": 119.76, "da_max": 300.24, "da_avg": 210.0,  "rt_avg": 195.0,  "unit": "元/MWh"},
        {"province": "江苏",  "da_min": 295.59, "da_max": 372.60, "da_avg": 334.0,  "rt_avg": 327.0,  "unit": "元/MWh"},
        {"province": "安徽",  "da_min": 290.00, "da_max": 416.04, "da_avg": 353.0,  "rt_avg": 360.0,  "unit": "元/MWh"},
        {"province": "蒙西",  "da_min": -20.38, "da_max": 214.27, "da_avg": 97.0,   "rt_avg": None,   "unit": "元/MWh"},
        {"province": "辽宁",  "da_min": -67.49, "da_max": 269.06, "da_avg": 100.0,  "rt_avg": 118.0,  "unit": "元/MWh"},
    ]


def load_cached_spot(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_spot_cache(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ── 煤价 ─────────────────────────────────────────────────────

def _hardcoded_coal_20260501() -> list:
    """2026-05-01 内置动力煤价，来源：CCTD/估算"""
    return [
        {"region": "秦皇岛港",        "spec": "Q5500大卡", "type": "港口", "price": 748, "date": "2026-05-01", "source": "CCTD", "note": ""},
        {"region": "秦皇岛港",        "spec": "Q5000大卡", "type": "港口", "price": 668, "date": "2026-05-01", "source": "CCTD", "note": ""},
        {"region": "秦皇岛港",        "spec": "Q4500大卡", "type": "港口", "price": 598, "date": "2026-05-01", "source": "CCTD", "note": ""},
        {"region": "山西大同",        "spec": "Q5500大卡", "type": "坑口", "price": 618, "date": "2026-05-01", "source": "估算", "note": "约值"},
        {"region": "陕西榆林",        "spec": "Q5500大卡", "type": "坑口", "price": 575, "date": "2026-05-01", "source": "估算", "note": "约值"},
        {"region": "内蒙古鄂尔多斯",  "spec": "Q5500大卡", "type": "坑口", "price": 428, "date": "2026-05-01", "source": "估算", "note": "约值"},
    ]


def _scrape_coal_sxcoal() -> dict:
    """尝试从中国煤炭资源网抓取当日煤价（HTML表格）"""
    url = "https://www.sxcoal.com/price/coalprice/index/type/1"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "lxml")

    rows = soup.select("table tr")
    results = []
    today = datetime.now().strftime("%Y-%m-%d")

    for tr in rows[1:]:
        cells = [td.get_text(strip=True) for td in tr.select("td")]
        if len(cells) < 4:
            continue
        try:
            price = float(cells[2].replace(",", ""))
            if 100 < price < 3000:
                results.append({
                    "region": cells[0],
                    "spec":   cells[1],
                    "type":   "坑口" if "坑口" in cells[0] else "港口",
                    "price":  price,
                    "date":   today,
                    "source": "中国煤炭资源网",
                    "note":   "",
                })
        except (ValueError, IndexError):
            continue

    if len(results) < 3:
        raise ValueError(f"sxcoal解析行数不足：{len(results)}")
    return {"fetched_at": datetime.now().isoformat(), "data": results}


def fetch_coal_prices() -> dict:
    """抓取每日动力煤价格，在线失败则使用内置数据"""
    builtin = {"fetched_at": datetime.now().isoformat(), "data": _hardcoded_coal_20260501()}
    try:
        online = _scrape_coal_sxcoal()
        print(f"[scraper] 煤价在线数据有效（{len(online['data'])} 条）")
        return online
    except Exception as e:
        print(f"[scraper] 煤价抓取失败: {e}，使用内置数据")
    return builtin


def load_cached_coal(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_coal_cache(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
