# Wallet API

> A FastAPI-based digital wallet service: users, wallet balance, cards, peer-to-peer transfers, and friends.

## What This Application Does

This application implements a **digital wallet** with the following capabilities:

- **User accounts & authentication**: register, sign in, get current profile.

- **Wallet balance**: view current balance, top up, send money.

- **Cards**: link one or more cards to a user, list and manage them.

- **Transactions**: send money to other users (by username), view history and details.

- **Friends**: add friends by username and list your contacts.

## How to Explore the API (Swagger Only)

- Start the server (see below) and open **Swagger UI** at: `http://localhost:8000/swagger`.

- Use the **Authorize** button in Swagger (if security is configured) to add your access token.

## Getting Started

### 1) Create a virtual environment (uv) and add dependencies
```bash
uv venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
uv sync
```


### 2) Run the server
```bash
python run_server.py
```
Then open Swagger: http://localhost:8000/swagger

## API Endpoints (Catalog & Purpose)

Main endpoint groups are:

- **/auth** – User registration and login.

- **/users** – Managing user profiles.

- **/wallet** – Query and manipulate wallet balance.

- **/cards** – Manage payment cards.

- **/transactions** – Create and list money transfers between users.

- **/friends** – Manage your friends list.

Each group is available and documented in **Swagger UI** (`/docs`).

## Typical Flows (How It Works)

1. **Register & Login** in Swagger.

2. **Add a Card** to your profile (in `Cards` section).

3. **Top-Up** your wallet (in `Wallet` section).

4. **Add a Friend** by username (in `Friends` section).

5. **Send a Transaction** to that friend (in `Transactions` section).

6. **Check Balance** and **Transaction History** any time.


---
