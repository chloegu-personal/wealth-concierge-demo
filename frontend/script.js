// JavaScript for Wealth Concierge Dashboard
const API_BASE_URL = 'http://localhost:5000/api';

async function fetchDashboardData() {
    try {
        const response = await fetch(`${API_BASE_URL}/dashboard`);
        const result = await response.json();
        if (result.success) {
            updateDashboardUI(result.data);
        }
    } catch (error) {
        console.error('Error fetching dashboard data:', error);
        // Fallback to mock data
        const mockData = {
            summary: {
                totalBalance: 12540890.50,
                monthlyIncome: 450000.00,
                monthlyExpenses: 120000.00,
                netGrowth: "4.2%"
            },
            portfolio: [
                { category: "Real Estate", amount: 5000000, color: "#1e3a8a" },
                { category: "Equities", amount: 3500000, color: "#d4af37" },
                { category: "Fixed Income", amount: 2500000, color: "#10b981" },
                { category: "Private Equity", amount: 1000000, color: "#6366f1" },
                { category: "Cash", amount: 540890, color: "#94a3b8" }
            ],
            transactions: [
                { id: "uuid-1", date: "2026-03-05", description: "Real Estate Income", category: "Real Estate", amount: 25000, type: "Income" },
                { id: "uuid-2", date: "2026-03-04", description: "Venture Exit", category: "Private Equity", amount: 450000, type: "Income" },
                { id: "uuid-3", date: "2026-03-02", description: "Luxury Residence Maint.", category: "Real Estate", amount: 15000, type: "Expense" },
            ]
        };
        updateDashboardUI(mockData);
    }
}

function updateDashboardUI(data) {
    document.getElementById('total-balance').textContent = formatCurrency(data.summary.totalBalance);
    document.getElementById('monthly-income').textContent = formatCurrency(data.summary.monthlyIncome);
    document.getElementById('monthly-expenses').textContent = formatCurrency(data.summary.monthlyExpenses);
    document.getElementById('net-growth').textContent = data.summary.netGrowth;

    const tbody = document.getElementById('transactions-body');
    tbody.innerHTML = '';
    data.transactions.forEach(tx => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${tx.date}</td>
            <td>${tx.description}</td>
            <td>${tx.category}</td>
            <td class="${tx.type === 'Income' ? 'type-income' : 'type-expense'}">${tx.type === 'Income' ? '+' : '-'}${formatCurrency(tx.amount)}</td>
            <td>${tx.type}</td>
        `;
        tbody.appendChild(row);
    });

    renderChart(data.portfolio);
}

let portfolioChartInstance = null;
function renderChart(portfolio) {
    const ctx = document.getElementById('portfolioChart').getContext('2d');
    
    if (portfolioChartInstance) {
        portfolioChartInstance.destroy();
    }

    portfolioChartInstance = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: portfolio.map(p => p.category),
            datasets: [{
                data: portfolio.map(p => p.amount),
                backgroundColor: portfolio.map(p => p.color),
                borderColor: 'rgba(212, 175, 55, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#94a3b8',
                        padding: 20,
                        font: { size: 12, family: 'Inter' }
                    }
                }
            }
        }
    });
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0
    }).format(amount);
}

function showDashboard() {
    document.getElementById('landing').style.display = 'none';
    document.getElementById('dashboard').style.display = 'block';
    document.getElementById('date-display').textContent = new Date().toLocaleDateString('en-US', {
        weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
    fetchDashboardData();
}
