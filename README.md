# Funds Disburment Data Engineering Project

## Objective

This full-stack application is designed for data engineering analysis of funds disburment. The platform enables users to visualize transaction data both at an aggregate level and by individual user, providing comprehensive insights into financial transaction patterns and fund distribution.

## Technologies Used

- **Database**: PostgreSQL
- **Backend**: Flask (Python)
- **Frontend**: Streamlit
- **Containerization**: Docker
- **Development Environment**: Docker Compose

## Database Structure

The database follows a normalized design with three main tables:

- **Users Table**: Stores user information (ID, name)
- **Payment Methods Table**: Contains payment method details (ID, name)
- **Transactions Table**: Records transaction data linking user IDs, payment method IDs, transaction dates, and amounts

This normalized structure ensures data integrity and enables efficient querying for analytics purposes.

### Database Schema

```sql
CREATE TABLE IF NOT EXISTS clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    client_id INT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    payment_method_id INT NOT NULL,
    CONSTRAINT fk_transactions_client FOREIGN KEY (client_id) REFERENCES clients(client_id),
    CONSTRAINT fk_transactions_payment_method FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id)
);
```

### Entity Relationship Diagram

```
┌─────────────────┐         ┌─────────────────────┐         ┌─────────────────────┐
│     clients     │         │    transactions     │         │  payment_methods    │
├─────────────────┤         ├─────────────────────┤         ├─────────────────────┤
│ client_id (PK)  │────────▶│ client_id (FK)      │◀────────│ payment_method_id   │
│ name            │         │ id (PK)             │         │ (PK)                │
└─────────────────┘         │ date                │         │ name                │
                            │ amount              │         └─────────────────────┘
                            │ payment_method_id   │
                            │ (FK)                │
                            └─────────────────────┘
```

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── db/              # Database connection management
│   │   ├── routes/          # API endpoints
│   │   └── services/        # Database query execution
│   ├── dockerfile
│   ├── requirements.txt
│   └── run.py
├── database/
│   └── init/                # Database initialization scripts
└── frontend/
    ├── app/
    │   ├── api.py           # API communication layer
    │   └── config.py        # Configuration settings
    ├── components/          # Reusable UI components
    ├── pages/              # Application pages
    ├── utils/              # Data processing utilities
    ├── dockerfile
    ├── main.py
    └── requirements.txt
```

## Architecture Overview

### Backend
- **Database Layer** (`db/`): Manages PostgreSQL connections and database interactions
- **API Routes** (`routes/`): Defines REST endpoints for data access
- **Services** (`services/`): SQL query execution

### Frontend
- **Components** (`components/`): Shared UI widgets used across multiple pages
- **Pages** (`pages/`): Individual application views and dashboards
- **Utils** (`utils/`): Data processing and transformation functions
- **API Layer** (`api.py`): Handles communication with the backend services

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

The application will be available with the frontend accessible through Streamlit and the backend API ready to serve data requests.

## Features

- **Transaction Visualization**: Comprehensive views of transaction data
- **User Analytics**: Individual user transaction patterns and insights
- **Data Engineering**: Robust data processing and analysis capabilities
- **Scalable Architecture**: Containerized deployment for easy scaling and maintenance