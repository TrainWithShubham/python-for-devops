## Script Selected
**Day-02 – API Data Fetcher**

---

## What problem am I solving?
- Manually API se data check karna slow aur error-prone hota hai
- DevOps tools mostly APIs ke through data exchange karte hain
- Is script ka goal hai:
  - API se data automatically fetch karna
  - JSON response ko samajhna
  - Useful information extract karna
  - Data ko file mein store karna

---

## What input does my script need?
- Public API URL (example: JSONPlaceholder API)
- Script run karne ke liye koi authentication ya API key ki need nahi
- User sirf script run karega

---

## What output should my script give?

### Terminal Output:
- API call successful ya failed
- Extracted data (ID, title, userId)

### File Output:
- JSON file (`output.json`)
- Structured aur processed API data

---

## What are the main steps?
1. API endpoint define karna
2. `requests` library use karke API call karna
3. Response ko JSON format mein convert karna
4. Required fields extract karna
5. Data terminal par print karna
6. Processed data JSON file mein save karna
7. Error aaye to script crash na ho

---

