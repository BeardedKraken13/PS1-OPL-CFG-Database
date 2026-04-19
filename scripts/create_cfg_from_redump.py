import xml.etree.ElementTree as ET
import os
import re

# =========================
# CONFIG
# =========================
INPUT_XML = r"psx_redump.xml"
OUTPUT_DIR = r"CFG"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# HELPERS
# =========================
def normalize_serial(serial):
    """
    SLUS-01323 → SLUS_013.23
    """
    match = re.match(r"([A-Z]+)-(\d+)", serial)
    if not match:
        return None

    prefix, number = match.groups()
    number = number.zfill(5)

    return f"{prefix}_{number[:3]}.{number[3:]}"

def clean_title(title):
    """
    Clean Redump-style names:
    - remove region tags
    - normalize whitespace
    """
    if not title:
        return "Unknown"

    title = re.sub(
        r"\((USA|Europe|Japan|Germany|France|Spain|Italy|Australia).*?\)",
        "",
        title
    )

    title = re.sub(r"\s+", " ", title).strip()
    return title

def get_serial(game):
    """
    Your DAT structure:
    <game>
        <serial>SLUS-01323</serial>
    </game>
    """
    return game.findtext("serial")

# =========================
# LOAD XML
# =========================
tree = ET.parse(INPUT_XML)
root = tree.getroot()

count = 0
skipped = 0

# =========================
# MAIN LOOP
# =========================
for game in root.findall(".//game"):

    title = clean_title(game.get("name"))

    serial = get_serial(game)
    if not serial:
        skipped += 1
        continue

    serial = serial.strip()

    normalized = normalize_serial(serial)
    if not normalized:
        skipped += 1
        continue

    filepath = os.path.join(OUTPUT_DIR, f"{normalized}.cfg")

    # Avoid duplicates
    if os.path.exists(filepath):
        continue

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("CfgVersion=8\n")
        f.write(f"Title={title}\n")

    count += 1

# =========================
# SUMMARY
# =========================
print("Done!")
print(f"Generated CFG files: {count}")
print(f"Skipped entries: {skipped}")
