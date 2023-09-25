import pandas as pd
import re

df = pd.read_csv('/content/CC Application Lifecycle.csv')

# Function to extract status and date from the text
def extract_status_and_date(text):
    #Find one or more chars before ] then find one or more chars before pipe
    status_date_pairs = re.findall(r'([^|\]]+)\]([^|]+)', text)
    status_dict = {}
    status_count = {}

    #loop through dict
    for status, date in status_date_pairs:

      #if the status exists, then increment the count by 1
        if status in status_dict:
            status_count[status] += 1
            status_name = f'{status}{status_count[status]}'

      #if not, just set the status as status
        else:
            status_count[status] = 0
            status_name = status
        status_dict[status_name] = date

    return pd.Series(status_dict)

# Apply the function to each row and fill missing values with NaN
result_df = df['string_agg'].apply(extract_status_and_date).fillna('')

# Combine the original DataFrame with the parsed status and date columns
final_df = pd.concat([df, result_df], axis=1)

final_df[['UniqueID', 'REGISTERED', 'ACKNOWLEDGED', 'APPROVED', 'REACKNOWLEDGED', 'CLOSED', 'APPOINTMENT_SCHEDULED', 'REJECTED', 'ON_HOLD', 'BLOCKED', 'TERMINATE', 'INITIATED', 'APPROVED1', 'ON_HOLD1', 'INITIATED1', 'REGISTERED1', 'CLOSED1', 'APPROVED2']]

