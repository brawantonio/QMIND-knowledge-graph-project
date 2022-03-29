import json
import pandas as pd

df = pd.read_csv("Development\query_results.csv")
result = df.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))