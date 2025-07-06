# Install Python 3.11

1. Visit <https://www.python.org/downloads/> and download the installer for version **3.11**.
2. Run the installer and ensure **"Add Python to PATH"** is selected.
3. Open a new terminal and verify the installation:

```powershell
python --version
```

You should see output similar to `Python 3.11.x`.

## Install via winget

On Windows systems you can also install Python with:

```powershell
winget install -e --id Python.Python.3.11
```
