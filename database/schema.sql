-- Wealth Concierge Backend Schema (SQLite/PostgreSQL compatible)

-- 1. Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id TEXT PRIMARY KEY, -- Using UUIDs
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. Accounts table
CREATE TABLE IF NOT EXISTS Accounts (
    account_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    account_type TEXT NOT NULL, -- e.g., 'Real Estate', 'Equities'
    balance DECIMAL(18, 2) DEFAULT 0.00,
    currency TEXT DEFAULT 'USD',
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 3. Transactions table
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id TEXT PRIMARY KEY,
    account_id TEXT NOT NULL,
    description TEXT,
    category TEXT,
    amount DECIMAL(18, 2) NOT NULL,
    type TEXT CHECK(type IN ('Income', 'Expense')) NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amount CHECK(amount > 0),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

-- 4. Currencies table (for caching exchange rates)
CREATE TABLE IF NOT EXISTS Currencies (
    currency_code TEXT PRIMARY KEY,
    rate_to_usd DECIMAL(10, 6),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 5. Logs table (for audit trail)
CREATE TABLE IF NOT EXISTS Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL,
    description TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
