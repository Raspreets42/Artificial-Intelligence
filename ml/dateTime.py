import pandas as pd
import numpy as np
from datetime import datetime

# Sample data
df = pd.DataFrame({
    'ticket_id': [1, 2, 3, 4, 5],
    'created_at': [
        '2024-03-15 14:30:00',  # Friday 2:30 PM
        '2024-03-16 09:15:00',  # Saturday 9:15 AM
        '2024-03-18 22:45:00',  # Monday 10:45 PM
        '2024-03-20 08:00:00',  # Wednesday 8:00 AM
        '2024-12-25 12:00:00'   # Christmas 12:00 PM
    ],
    'resolved_at': [
        '2024-03-16 10:00:00',
        '2024-03-16 14:30:00',
        '2024-03-19 09:30:00',
        '2024-03-20 17:00:00',
        '2024-12-27 15:00:00'
    ]
})

# Convert to datetime
df['created_at'] = pd.to_datetime(df['created_at'])
df['resolved_at'] = pd.to_datetime(df['resolved_at'])

# ============================================
# 1. BASIC TIME COMPONENTS (from created_at)
# ============================================
df['year'] = df['created_at'].dt.year
df['month'] = df['created_at'].dt.month
df['day'] = df['created_at'].dt.day
df['hour'] = df['created_at'].dt.hour
df['minute'] = df['created_at'].dt.minute
df['dayofweek'] = df['created_at'].dt.dayofweek  # Monday=0, Sunday=6
df['dayofyear'] = df['created_at'].dt.dayofyear
df['weekofyear'] = df['created_at'].dt.isocalendar().week
df['quarter'] = df['created_at'].dt.quarter

# ============================================
# 2. CYCLICAL ENCODING (for hours, days, months)
# ============================================
# Why? Because hour 23 and hour 0 are similar (both late night)
# Linear encoding (0,1,2...23) loses this circular relationship

df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)

df['dayofweek_sin'] = np.sin(2 * np.pi * df['dayofweek'] / 7)
df['dayofweek_cos'] = np.cos(2 * np.pi * df['dayofweek'] / 7)

df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

# ============================================
# 3. BUSINESS LOGIC FLAGS
# ============================================
df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)  # Sat=5, Sun=6
df['is_business_hours'] = df['hour'].between(9, 17).astype(int)
df['is_lunch_hour'] = df['hour'].between(12, 13).astype(int)
df['is_morning_rush'] = df['hour'].between(7, 9).astype(int)
df['is_evening_rush'] = df['hour'].between(17, 19).astype(int)
df['is_night'] = df['hour'].between(22, 5).astype(int)

# ============================================
# 4. HOLIDAY / SPECIAL DAY FLAGS
# ============================================
# Define holidays (simplified)
holidays = ['2024-01-01', '2024-12-25']  # New Year, Christmas
df['is_holiday'] = df['created_at'].dt.date.astype(str).isin(holidays).astype(int)

# ============================================
# 5. TIME DIFFERENCES (Target variable & features)
# ============================================
# Target: resolution time in hours
df['resolution_hours'] = (df['resolved_at'] - df['created_at']).dt.total_seconds() / 3600

# Features: time since last ticket (for sequential data)
df = df.sort_values('created_at')
df['hours_since_last_ticket'] = df['created_at'].diff().dt.total_seconds() / 3600

# Time to end of day (if created at 2:30 PM, 3.5 hours until 6 PM)
df['hours_until_eod'] = (df['created_at'].dt.normalize() + pd.Timedelta(days=1) - df['created_at']).dt.total_seconds() / 3600

# ============================================
# 6. SEASONALITY
# ============================================
def get_season(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'fall'

df['season'] = df['month'].apply(get_season)
# df = pd.get_dummies(df, columns=['season'], prefix='season')  # One-hot encode

# ============================================
# 7. CUSTOM BINS (based on domain knowledge)
# ============================================
df['time_of_day_category'] = pd.cut(df['hour'],
                                     bins=[0, 6, 12, 18, 24],
                                     labels=['night', 'morning', 'afternoon', 'evening'])

# ============================================
# 8. WINDOW AGGREGATIONS (for time series)
# ============================================
# Rolling average of resolution time for last 3 tickets
df['rolling_3hr_avg_resolution'] = df['resolution_hours'].rolling(window=3, min_periods=1).mean()

# ============================================
# 9. TIME SINCE SPECIFIC EVENT
# ============================================
# Days since start of month
df['days_since_month_start'] = df['created_at'].dt.day - 1

# Days until month end
df['days_until_month_end'] = (df['created_at'].dt.days_in_month - df['created_at'].dt.day)

# ============================================
# VIEW RESULTS
# ============================================
print("Final features created:")

print("1. BASIC TIME COMPONENTS (from created_at)")
print(df[['ticket_id', 'created_at', 'year', 'month', 'day', 'hour', 'minute', 'dayofweek', 'dayofyear', 'weekofyear', 'quarter']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("2. CYCLICAL ENCODING (for hours, days, months)")
print(df[['ticket_id', 'created_at', 'hour_sin', 'hour_cos', 'dayofweek_sin', 'dayofweek_cos', 'month_sin', 'month_cos']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("3. BUSINESS LOGIC FLAGS & 4. HOLIDAY / SPECIAL DAY FLAGS")
print(df[['ticket_id', 'created_at', 'is_weekend', 'is_holiday', 'is_business_hours', 'is_lunch_hour', 'is_morning_rush', 'is_evening_rush', 'is_night']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("5. TIME DIFFERENCES (Target variable & features)")
print(df[['ticket_id', 'created_at', 'resolution_hours', 'hours_since_last_ticket', 'hours_until_eod']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("6. SEASONALITY")
print(df[['ticket_id', 'created_at', 'season']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("7. CUSTOM BINS (based on domain knowledge)")
print(df[['ticket_id', 'created_at', 'time_of_day_category']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("8. WINDOW AGGREGATIONS (for time series)")
print(df[['ticket_id', 'created_at', 'rolling_3hr_avg_resolution']].head())
print('--------------------------------------------------------------------------------------------------------------------------------------------------------')

print("9. TIME SINCE SPECIFIC EVENT")
print(df[['ticket_id', 'created_at', 'days_since_month_start', 'days_until_month_end']].head())