import os
import re

CFG_DIR = r"CFG"
OUTPUT_DIR = r"psx_rom_index"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(title):
    """
    Keep titles readable, only remove truly unsafe filesystem characters.
    Avoid over-normalizing (ScreenScraper prefers readable names).
    """

    # Remove only characters illegal in Windows/Linux filenames
    title = re.sub(r'[\/:*?"<>|]', '', title)

    # Normalize whitespace (keep words intact)
    title = re.sub(r'\s+', ' ', title).strip()

    return title

count = 0

for file in os.listdir(CFG_DIR):
    if not file.endswith(".cfg"):
        continue

    cfg_path = os.path.join(CFG_DIR, file)

    title = None

    with open(cfg_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Title="):
                title = line.split("=", 1)[1].strip()
                break

    if not title:
        continue

    safe_title = sanitize_filename(title)

    cue_path = os.path.join(OUTPUT_DIR, f"{safe_title}.cue")

    # Avoid overwriting duplicates
    if os.path.exists(cue_path):
        continue

    with open(cue_path, "w", encoding="utf-8") as f:
        # fake minimal PS1 cue structure
        f.write(f'FILE "{safe_title}.bin" BINARY\n')
        f.write("  TRACK 01 MODE2/2352\n")
        f.write("    INDEX 01 00:00:00\n")

    print("Created:", cue_path)
    count += 1

print(f"\nDone. Created {count} .cue files.")
