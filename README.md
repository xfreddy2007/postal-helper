# Taiwan Postal Helper

A terminal-based tool for looking up Taiwan 6-digit (3+3) postal codes by address.

> 100% built with [Claude Code](https://claude.ai/claude-code) — from initial implementation to testing and Git setup, every line of code and configuration was generated through conversation with Claude Code CLI.

---

## Overview

Taiwan upgraded its postal code system from 5-digit (3+2) to 6-digit (3+3) format in 2020. This tool lets you quickly query the correct postal code for any Taiwan address directly from your terminal, without needing to visit a website manually.

It queries the community-maintained [zip5.5432.tw](http://zip5.5432.tw) API, which is built on data from Chunghwa Post (中華郵政). Results include:

- **6-digit postal code** (3+3 format) when available
- **5-digit postal code** (3+2 format) as a fallback
- A link to the detailed lookup page for verification

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| HTTP client | `urllib` (stdlib, no dependencies) |
| JSON parsing | `json` (stdlib) |
| Postal code API | [zip5.5432.tw](http://zip5.5432.tw/zip5json.py) |

No third-party packages required — runs on a clean Python installation.

---

## How to Run

### Requirements

- Python 3.9 or later
- Internet connection

### Interactive Mode

Run without arguments to enter addresses one at a time:

```bash
python3 postal_helper.py
```

```
=== 台灣郵遞區號查詢 ===
輸入地址查詢6碼郵遞區號，輸入 q 或按 Ctrl+C 離開。

請輸入地址：台北市信義區市府路1號

地址：台北市信義區市府路1號
郵遞區號（6碼）：110204
詳細資訊：https://zip5.5432.tw/zip/台北市信義區市府路1號
```

Type `q` or press `Ctrl+C` to exit.

### Batch Mode

Pass one or more addresses as command-line arguments:

```bash
python3 postal_helper.py "台北市信義區市府路1號" "高雄市苓雅區四維三路2號"
```

```
地址：台北市信義區市府路1號
郵遞區號（6碼）：110204
詳細資訊：https://zip5.5432.tw/zip/台北市信義區市府路1號

地址：高雄市苓雅區四維三路2號
郵遞區號（6碼）：802721
詳細資訊：https://zip5.5432.tw/zip/高雄市苓雅區四維三路2號
```

---

## API Reference

This tool uses the free, community-maintained API at:

```
http://zip5.5432.tw/zip5json.py?adrs=<address>
```

Key response fields:

| Field | Description |
|---|---|
| `zipcode6` | 6-digit postal code (3+3 format) |
| `zipcode` | 5-digit postal code (3+2 format) |
| `detail_url` | Link to detailed address info |

> Please avoid sending rapid consecutive requests to be respectful of the free service.

---

## License

MIT
