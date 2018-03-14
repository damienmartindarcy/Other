# Break up dates and times

# Load library
import pandas as pd
 
# Create data frame
df = pd.DataFrame()

# Create five dates
df['date'] = pd.date_range('1/1/2001', periods=150, freq='W')
 

# Create features for year, month, day, hour, and minute
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute

# Show three rows
df.head(3)