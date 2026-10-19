# Nerd Jokes CLI 🤓

A minimal command-line program in Python that tells random programmer/computer nerd jokes, one at a time, and ends with a laughing emoji rain animation when you quit.

---

## ⚡ Don't have Python installed? (Install in 30 seconds)

If you don't have Python on Windows, open **PowerShell** and run:

```powershell
winget install Python.Python.3.12
```

> ⚠️ **Important:** After the installation finishes, close PowerShell and open a new PowerShell window so `python` and `pip` are ready to use.

---

## Installation

### From GitHub (No Git required)
You can install directly from GitHub using `pip` (works even without Git installed):
```bash
pip install https://github.com/madheshiyaraj562-cmyk/nerd-jokes-cli/archive/refs/heads/main.zip
```

Or using Git:
```bash
pip install git+https://github.com/madheshiyaraj562-cmyk/nerd-jokes-cli.git
```

### From PyPI (once published)
```bash
pip install nerd-jokes-cli
```

### For Local Development
Clone the repo and run in editable mode:
```bash
cd nerd-jokes-cli
pip install -e .
```

---

## How to Run

After installing, simply run the command in any terminal:
```bash
nerd-jokes
```

- Press **Enter** to see the setup and reveal the punchline.
- Type **`q`** or press **Ctrl+C** to quit and enjoy the laughing emoji rain!

> 💡 **Tip for Windows CMD users:** Run `chcp 65001` first if you want emojis to display in full color in `cmd.exe`.

---

## How to Uninstall

### 1. Uninstall `nerd-jokes`
To remove the jokes CLI from your system:
```bash
pip uninstall nerd-jokes-cli -y
```

### 2. Uninstall Python (Optional)
If you installed Python just for this and want to remove it completely from Windows:
```powershell
winget uninstall Python.Python.3.12
```

---

## Author

Made by **Raj Madheshiya@2026**

## License

MIT License
