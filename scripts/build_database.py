from pathlib import Path
import csv

print("=" * 50)
print("English Knowledge Base")
print("=" * 50)

# 项目根目录
project_root = Path(__file__).parent.parent

# 词库文件
csv_file = project_root / "data" / "vocab" / "vocab_master.csv"

print(f"Reading: {csv_file}")

# 判断文件是否存在
if not csv_file.exists():
    print("❌ vocab_master.csv 不存在！")
    exit()

# 读取 CSV
with open(csv_file, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    words = list(reader)

print(f"\n✅ Successfully loaded {len(words)} words.\n")

# 打印前5个单词
print("Preview:")
for word in words[:5]:
    print(f"{word['id']} | {word['word']} | {word['meaning']}")