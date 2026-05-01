"""
每日生成各电力公司研究 Excel，保存至 output/电力/公司/[公司名]/
"""
import os
from datetime import datetime
from company_excel import generate_company_excel
from companies import COMPANIES

OUTPUT_BASE = os.path.join(os.path.dirname(__file__), "output", "电力", "公司")


def main():
    now = datetime.now()
    month = now.strftime("%Y-%m")
    results = []

    for name in COMPANIES:
        out_dir = os.path.join(OUTPUT_BASE, name, month)
        try:
            path = generate_company_excel(name, out_dir)
            results.append((name, "✅", path))
        except Exception as e:
            print(f"[company] {name} 生成失败：{e}")
            results.append((name, "❌", str(e)))

    print(f"\n{'─'*60}")
    for name, status, path in results:
        print(f"  {status} {name}：{os.path.basename(path)}")
    print(f"{'─'*60}")
    return results


if __name__ == "__main__":
    main()
