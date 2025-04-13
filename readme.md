# Cron Expression Parser

A simple yet powerful Cron Expression Parser built with Python. This parser supports standard cron expressions with support for wildcards (`*`), ranges (`-`), steps (`/`), and lists (`,`).

## Features

- Parse cron expressions into actual time values.
- Support for:
  - `*` (wildcard)
  - `a-b` (ranges)
  - `*/n` (step values)
  - `a,b,c` (lists)
- Unit tests for all valid and invalid cases using `parameterized`.

---

## 🧰 Dependencies

This project requires Python 3.7 or higher.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Running the Parser
```
python3 -m src.main "*/10 0 1,1 * 1-5 /usr/bin/find"
```
## Example Output

```
minute        0 15 30 45
hour          9 10 11 12 13 14 15 16 17
day of month  1 2 3 ... 31
month         1 2 3 ... 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```