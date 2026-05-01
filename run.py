"""
入口脚本：抓取最新电价数据并生成 Excel 报告
用法：
  python3 run.py              # 尝试联网抓取 + 生成 Excel
  python3 run.py --offline    # 仅使用缓存/内置数据，不联网
"""
import sys
import os
import json
from datetime import datetime

from scraper import fetch_sina_weekly_spot, load_cached_spot, save_spot_cache
from excel_gen import generate_excel

DATA_DIR   = os.path.join(os.path.dirname(__file__), "data")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
CACHE_FILE = os.path.join(DATA_DIR, "spot_latest.json")


def main():
    offline = "--offline" in sys.argv
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if offline:
        print("[run] 离线模式：加载本地缓存数据")
        spot_data = load_cached_spot(CACHE_FILE)
        if not spot_data:
            print("[run] 无缓存数据，使用内置兜底数据")
            from scraper import _hardcoded_spot_20260420
            spot_data = {
                "week": "2026.4.20~2026.4.26",
                "source_url": "内置数据",
                "data": _hardcoded_spot_20260420(),
                "fetched_at": datetime.now().isoformat(),
            }
    else:
        print("[run] 联网抓取现货电价周报...")
        spot_data = fetch_sina_weekly_spot()
        save_spot_cache(spot_data, CACHE_FILE)
        print(f"[run] 已缓存至 {CACHE_FILE}")

    # 生成文件名（按当前年月）
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"electricity_prices_{ts}.xlsx"
    output_path = os.path.join(OUTPUT_DIR, filename)

    generate_excel(spot_data, output_path)
    print(f"\n✅ 报告已生成：{output_path}")
    print(f"   现货数据周期：{spot_data.get('week', '—')}")
    print(f"   现货省份数量：{len(spot_data.get('data', []))} 个")
    return output_path


if __name__ == "__main__":
    main()
