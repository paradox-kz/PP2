import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract prices
prices = re.findall(r"\d+[.,]\d{2}", text)

# Convert prices to float
clean_prices = [float(price.replace(",", ".")) for price in prices]                            

# 2️⃣ Extract product names
products = re.findall(r"\d+\.\n(.+?)\n\d", text)

# 3️⃣ Extract total
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)
total = None
if total_match:
    total = float(total_match.group(1).replace(" ", "").replace(",", "."))

# 4️⃣ Extract date and time
datetime_match = re.search(r"Время:\s([\d\.]+\s[\d:]+)", text)
datetime_value = datetime_match.group(1) if datetime_match else None

# 5️⃣ Extract payment method
payment_match = re.search(r"(Банковская карта|Наличные):", text)
payment_method = payment_match.group(1) if payment_match else None

# 6️⃣ Create structured output
result = {
    "products": products,
    "prices": clean_prices,
    "total": total,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(result, indent=4, ensure_ascii=False))