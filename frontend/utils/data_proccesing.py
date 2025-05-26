import pandas as pd

def load_and_preprocess_data(data):
    df = pd.DataFrame(data)
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'])
    return df

def filter_by_date_range(df, start_date, end_date):
    return df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)].copy()

def calculate_metrics(df):
    metrics = {}
    if not df.empty:
        metrics['total_dispersed'] = df['amount'].sum()
        metrics['total_transactions'] = df.shape[0]
        metrics['average_amount'] = df['amount'].mean()
        metrics['min_amount'] = df['amount'].min()
        metrics['max_amount'] = df['amount'].max()
    else:
        metrics = {'total_dispersed': 0, 'total_transactions': 0, 'average_amount': 0, 'min_amount': 0, 'max_amount': 0}
    return metrics

