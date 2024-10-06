
import pandas as pd

# Data to save
data = {
    "client_id": ["1101112645"],
    "access_token": ["tu"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
file_name = "dhan.xlsx"
df.to_excel(file_name, index=False)

print(f"Data saved to {file_name}")



from dhanhq import dhanhq

client_id = "1101112645"
access_token = "b"
dhan = dhanhq(client_id, access_token)
