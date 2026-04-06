#!/usr/bin/env python3
"""Taiwan Postal Helper - Web version (Flask backend)."""

from flask import Flask, jsonify, render_template, request

from postal_helper import lookup_postal_code

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/lookup", methods=["POST"])
def lookup():
    data = request.get_json()
    address = (data or {}).get("address", "").strip()
    if not address:
        return jsonify({"error": "請輸入地址"}), 400
    try:
        result = lookup_postal_code(address)
        return jsonify({
            "zipcode6": result.get("zipcode6", "").strip(),
            "zipcode": result.get("zipcode", "").strip(),
            "detail_url": result.get("detail_url", ""),
        })
    except Exception as e:
        return jsonify({"error": f"查詢失敗：{e}"}), 502


if __name__ == "__main__":
    app.run(debug=True)
