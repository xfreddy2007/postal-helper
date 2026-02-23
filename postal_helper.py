#!/usr/bin/env python3
"""Taiwan Postal Helper - Look up 6-digit postal codes by address."""

import sys
import urllib.parse
import urllib.request
import json


API_URL = "http://zip5.5432.tw/zip5json.py"


def lookup_postal_code(address: str) -> dict:
    """Query the zip5.5432.tw API and return the result."""
    params = urllib.parse.urlencode({"adrs": address})
    url = f"{API_URL}?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "PostalHelper/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw = resp.read().decode("utf-8")

    return json.loads(raw)


def print_result(address: str, data: dict) -> None:
    zipcode6 = data.get("zipcode6", "").strip()
    zipcode5 = data.get("zipcode", "").strip()

    print(f"\n地址：{address}")
    if zipcode6:
        print(f"郵遞區號（6碼）：{zipcode6}")
    elif zipcode5:
        print(f"郵遞區號（5碼）：{zipcode5}  （查無6碼）")
    else:
        print("查無對應郵遞區號，請確認地址是否正確。")

    detail = data.get("detail_url", "")
    if detail:
        print(f"詳細資訊：{detail}")


def interactive_mode() -> None:
    print("=== 台灣郵遞區號查詢 ===")
    print("輸入地址查詢6碼郵遞區號，輸入 q 或按 Ctrl+C 離開。\n")
    while True:
        try:
            address = input("請輸入地址：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已離開。")
            break

        if not address:
            continue
        if address.lower() in ("q", "quit", "exit"):
            print("已離開。")
            break

        try:
            data = lookup_postal_code(address)
            print_result(address, data)
        except Exception as e:
            print(f"查詢失敗：{e}")
        print()


def batch_mode(addresses: list[str]) -> None:
    for address in addresses:
        address = address.strip()
        if not address:
            continue
        try:
            data = lookup_postal_code(address)
            print_result(address, data)
        except Exception as e:
            print(f"\n地址：{address}\n查詢失敗：{e}")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        interactive_mode()
    else:
        batch_mode(args)


if __name__ == "__main__":
    main()
