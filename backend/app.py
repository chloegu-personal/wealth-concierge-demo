import os
import uuid
import time
from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- MOCK DATA / CACHE ---
# In a real app, this would be in SQLite/PostgreSQL
currency_cache = {
    "rates": {"SGD": 1.34, "EUR": 0.92, "GBP": 0.79, "JPY": 150.5},
    "timestamp": time.time()
}

def get_cached_rates():
    global currency_cache
    # 1-hour cache logic (as requested)
    if time.time() - currency_cache["timestamp"] > 3600:
        # Simulate API refresh
        currency_cache["timestamp"] = time.time()
        print("Currency cache refreshed via Mock API.")
    return currency_cache["rates"]

def generate_dashboard_data():
    user_id = str(uuid.uuid4())
    
    portfolio = [
        {"id": str(uuid.uuid4()), "category": "Real Estate", "amount": 5000000, "color": "#1e3a8a"},
        {"id": str(uuid.uuid4()), "category": "Equities", "amount": 3500000, "color": "#d4af37"},
        {"id": str(uuid.uuid4()), "category": "Fixed Income", "amount": 2500000, "color": "#10b981"},
        {"id": str(uuid.uuid4()), "category": "Private Equity", "amount": 1000000, "color": "#6366f1"},
        {"id": str(uuid.uuid4()), "category": "Cash", "amount": 540890, "color": "#94a3b8"}
    ]
    
    descriptions = ["Capital Gain", "Asset Maintenance", "Portfolio Dividend", "Concierge Fee", "Real Estate Rental"]
    transactions = []
    for i in range(5):
        transactions.append({
            "id": str(uuid.uuid4()),
            "date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
            "description": descriptions[i % len(descriptions)],
            "category": portfolio[i % len(portfolio)]["category"],
            "amount": 5000 * (i + 1),
            "type": "Income" if i % 2 == 0 else "Expense"
        })
        
    return {
        "summary": {
            "totalBalance": 12540890,
            "monthlyIncome": 450000,
            "monthlyExpenses": 120000,
            "netGrowth": "4.2%"
        },
        "portfolio": portfolio,
        "transactions": transactions,
        "exchangeRates": get_cached_rates()
    }

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    return jsonify({
        "success": True,
        "data": generate_dashboard_data()
    })

@app.route('/api/currency', methods=['GET'])
def get_currency():
    return jsonify({
        "success": True,
        "rates": get_cached_rates()
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "WealthConcierge-API"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
