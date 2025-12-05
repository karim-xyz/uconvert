# UConvert

A simple command-line unit converter built with Python, Typer, and Rich.
Convert between the most useful units with ease, directly from your Terminal.

---

## Requirements

Python 3.8+

Typer

Rich

### Install dependencies:
```bash
pip3 install typer
```

---

## Usage

### Run the app
```bash
python3 convert.py [command] [value] [unit] [result-unit]
```

### Examples:

```bash
python3 convert.py length 5 in cm
```
Output:
```
12.7
```

```bash
python3 convert.py mass 5 kg lb
```
Output:
```
11.023
```

### Check help 
```bash
python3 convert.py --help
```

### Supported Units
```bash
python3 convert.py units
```

---

I built this app because I often get confused by American units like feet, inches, and gallons. Now I can quickly convert them to units I actually understand.
Hope it helps you.

---


