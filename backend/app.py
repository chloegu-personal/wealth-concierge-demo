from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Mock Data Generator
def generate_mock_data():
    categories = ['Real Estate', 'Equities', 'Private Equity', 'Fixed Income', 'Cash', 'Commodities']
    balance = 12540890.50
    monthly_income = 450000.00
    monthly_expenses = 120000.00
    
    # Portfolio breakdown
    portfolio = [
        {"category": "Real Estate", "amount": 5000000, "color": "#1e3a8a"},
        {"category": "Equities", "amount": 3500000, "color": "#f59e0b"},
        {"category": "Fixed Income", "amount": 2500000, "color": "#10b981"},
        {"category": "Private Equity", "amount": 1000000, "color": "#6366f1"},
        {"category": "Cash", "amount": 540890, "color": "#94a3b8"}
    ]
    
    # Recent Transactions
    transactions = []
    descriptions = ["Stock Dividend", "Property Rental Income", "Consultancy Fee", "Equity Investment", "Travel Expense", "Luxury Goods Purchase"]
    for i in range(10):
        date = (datetime.now() - timedelta(days=i*2)).strftime("%Y-%m-%d")
        transactions.append({
            "id": i + 1,
            "date": date,
            "description": random.choice(descriptions),
            "category": random.choice(categories),
            "amount": random.randint(1000, 50000),
            "type": "Income" if i % 3 == 0 else "Expense"
        })
        
    return {
        "summary": {
            "totalBalance": balance,
            "monthlyIncome": monthly_income,
            "monthlyExpenses": monthly_expenses,
            "netGrowth": "4.2%"
        },
        "portfolio": portfolio,
        "transactions": transactions
    }

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    return jsonify({
        "success": True,
        "data": generate_mock_data()
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
