# UConvert

A simple, fast, and extensible command-line unit converter built with Python, Typer, and Rich.
Convert between the most useful units with ease, directly from your Terminal ! 

I built this app because I often get confused by American units like feet, inches, and gallons. Now I can quickly convert them to units I actually understand.

---

## ✅ Features

Common length, area, mass, and volume units.

Simple and user-friendly.

Error handling for invalid units.

Easy to extend with new units.

---

## 📦 Requirements

Python 3.8+

Typer

Rich

Install dependencies:
```bash
pip3 install typer
```

---

## 🚀 Usage

Run the app
```bash
python3 main.py [COMMAND] [OPTIONS]
```

Examples:

Length
```bash
python3 main.py length 5 ft m
```
Output:
```
1.524
```

Mass
```bash
python3 main.py mass 5 kg lb
```
Output:
```
11.023
```

### Check help 
To see all commands: 
```bash
python3 main.py --help
```

### 🔍 Supported Units
```bash
python3 main.py units
```

---


