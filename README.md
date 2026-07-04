# 🔐 Password Generator CLI

A simple, secure, command-line password generator built in Python — created as a **practice/learning project** to explore cryptographically secure randomness, terminal styling, and clean CLI UX design.

> 🧪 **Status:** Practice Project — built for learning purposes, not a production security tool.

---

## 📸 Preview

```
Welcome! to password generator.
You can generate any type of password of any length.
You can use symbols, numbers, letters.
You can choose any of the following, and combination, or all of them.

Select a password strength level.
1 : Weak(only letters)
2 : Medium(letters + numbers)
3 : Strong(letters + numbers + symbols)

Enter the length of the password(integer): 16
Enter your choice: 3

Here is your password : G7$kLp!qR2@zXwYm

Press 'C' to copy to clipboard and exit.
Press anything to generate a new password.
Please give a command : c

Copied to clipboard.
Thanks for using...
```

*(Colors render in green, blue, red, and bold in an actual terminal — the block above shows the plain text flow.)*

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 **3 Strength Levels** | Weak (letters only), Medium (letters + digits), Strong (letters + digits + symbols) |
| 📏 **Custom Length** | Choose any password length between `1` and `64` characters |
| 🎲 **Cryptographically Secure** | Uses Python's `secrets` module instead of `random` for true security-grade randomness |
| 🎨 **Colorful Terminal UI** | ANSI escape codes highlight prompts, results, and errors in blue, green, red, and bold |
| 📋 **Clipboard Support** | Instantly copy your generated password using `pyperclip` |
| 🔁 **Regenerate Loop** | Keep generating new passwords until you're happy — press any key to retry, `C` to copy & exit |
| ✅ **Input Validation** | Gracefully handles invalid lengths, non-integer inputs, and out-of-range menu choices |

---

## 🛠️ How It Works

The program flows through four main stages:

```
┌─────────────────┐     ┌───────────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│  Display Menu    │ ──▶ │  Get User Choice   │ ──▶ │ Generate Password    │ ──▶ │  Copy / Repeat   │
│  (strength info)  │     │ (length + level)   │     │ (secrets.choice loop)│     │  (pyperclip)     │
└─────────────────┘     └───────────────────┘     └──────────────────────┘     └─────────────────┘
```

### 1. `display_menu()`
Prints a styled welcome message and explains the three strength options available to the user.

### 2. `get_user_choice()`
- Asks for a desired password **length** (validated to be an integer between `1` and `64`).
- Asks for a **strength level** (`1`, `2`, or `3`).
- Uses nested `while` loops with `try/except ValueError` to keep re-prompting until valid input is given — no crashes on bad input.

### 3. `password_generator(user_choice, length)`
- Selects a character pool based on strength:
  - **Weak** → `string.ascii_lowercase + string.ascii_uppercase`
  - **Medium** → adds `string.digits`
  - **Strong** → adds `string.punctuation`
- Uses `secrets.choice()` — **not** `random.choice()` — to pick each character. This matters because `secrets` draws from a cryptographically secure random number generator, making the output unpredictable and safe for real-world credentials (unlike Python's standard `random`, which is deterministic and exploitable).
- Joins the selected characters into the final password string.

### 4. `display_password()`
- Orchestrates the whole flow in a loop.
- Displays the generated password with colored/bold formatting.
- Prompts the user: press `C`/`c` to copy the password to the clipboard (via `pyperclip.copy()`) and exit, or press anything else to loop back and generate a brand-new password.

---

## 📦 Requirements

- Python 3.6+
- [`pyperclip`](https://pypi.org/project/pyperclip/) (for clipboard support)

Install the dependency:

```bash
pip install pyperclip
```

> 💡 On Linux, `pyperclip` may also require a clipboard utility like `xclip` or `xsel` to be installed at the OS level.

---

## 🚀 Usage

```bash
python password_generator.py
```

Then just follow the on-screen prompts:
1. Enter a desired password length (1–64)
2. Choose a strength level (1, 2, or 3)
3. Get your password instantly
4. Press `C` to copy it, or any other key to generate a new one

---

## 🧠 What This Project Demonstrates (Learning Goals)

This project was built to practice:
- ✅ Using the `secrets` module for cryptographically secure randomness (vs. `random`)
- ✅ Structuring a CLI app into clean, single-responsibility functions
- ✅ Robust input validation with nested loops and exception handling
- ✅ Terminal styling using raw ANSI escape codes
- ✅ Integrating third-party libraries (`pyperclip`) for real-world utility (clipboard access)
- ✅ Building a simple interactive loop-based program flow

---

## ⚠️ Disclaimer

This is a **practice/educational project**. While it does use secure randomness under the hood, it hasn't been audited or hardened for production use. Don't build a password manager on top of this without additional review — but it's a great sandbox for learning Python fundamentals and secure coding habits!

---

## 📄 License

Free to use for learning and practice purposes.
