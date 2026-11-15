import json
from pathlib import Path

source = Path("data_awal.json")
target = Path("data_awal_utf8.json")

raw = source.read_bytes()

try:
    content = raw.decode("utf-8")
    print("Encoding awal: UTF-8")
except UnicodeDecodeError:
    content = raw.decode("cp1252")
    print("Encoding awal: Windows-1252")

data = json.loads(content)

target.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print("JSON valid!")
print("Jumlah data:", len(data))
print("File hasil:", target)
print("Ukuran:", target.stat().st_size, "byte")
