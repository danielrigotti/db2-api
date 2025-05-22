from flask import Flask, jsonify, request
import ibm_db
import os

app = Flask(__name__)

DB_CONN_STR = os.environ.get("DB_CONN_STR")

@app.route("/query", methods=["POST"])
def run_query():
    query = request.json.get("sql")
    if not query:
        return jsonify({"error": "SQL query is required"}), 400

    try:
        conn = ibm_db.connect(DB_CONN_STR, '', '')
        stmt = ibm_db.exec_immediate(conn, query)

        result = []
        row = ibm_db.fetch_assoc(stmt)
        while row:
            result.append(row)
            row = ibm_db.fetch_assoc(stmt)

        ibm_db.close(conn)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
