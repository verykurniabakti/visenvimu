import sys
import importlib
import subprocess
import os
from platform import python_version
from pathlib import Path

# ✅ Modul yang dibutuhkan
modules = [
    'numpy', 'pandas', 'matplotlib', 'seaborn', 'scipy', 'jinja2',
    'scikit-learn', 'imblearn', 'pyswarms', 'plotly', 'kaleido', 'openpyxl', 'ipykernel'
]

print("🔍 Validasi Environment untuk Workflow IMU")
print(f"📌 Python Path     : {sys.executable}")
print(f"🐍 Python Version  : {python_version()}")
print(f"📦 Working Directory: {Path.cwd()}")

missing = []

# ✅ Cek setiap modul
for module in modules:
    try:
        importlib.import_module(module)
        print(f"✅ {module}")
    except ImportError:
        print(f"❌ {module} (akan diinstal)")
        missing.append(module)

# ✅ Install modul yang belum ada
if missing:
    print("\n📦 Menginstal modul yang belum tersedia...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
else:
    print("\n🎉 Semua modul sudah tersedia!")

# ✅ Registrasi kernel Jupyter
try:
    env_name = Path(sys.executable).parent.parent.name
    display_name = f"IMU Env ({python_version()})"
    subprocess.check_call([
        sys.executable, "-m", "ipykernel", "install", "--user",
        "--name", env_name, "--display-name", display_name
    ])
    print(f"\n🔗 Kernel Jupyter '{display_name}' sudah terdaftar!")
except Exception as e:
    print(f"\n⚠️ Gagal registrasi kernel: {e}")
