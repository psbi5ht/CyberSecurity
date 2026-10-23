import pandas as pd

# 1. Create a DataFrame from a dictionary (wrapped in lists)
data = {"a": ["b", "c"], "d": ["e", "f"]}
df = pd.DataFrame(data)

# 2. Use df.head() to view the top rows
print("--- Using head() ---")
print(df.head())

# 3. Print basic information about the columns and data types
print("\n--- Dataset Summary ---")
print(df.info())