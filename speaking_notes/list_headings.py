import os

files = [
    r"C:\Antigravity\cbc-c-beginner-staff\speaking_notes\Speaker_Notes_Lesson1.md",
    r"C:\Antigravity\cbc-c-beginner-staff\speaking_notes\Speaker_Notes_Lesson2.md",
    r"C:\Antigravity\cbc-c-beginner-staff\speaking_notes\Speaker_Notes_Lesson3.md",
    r"C:\Antigravity\cbc-c-beginner-staff\speaking_notes\Speaker_Notes_Lesson4.md"
]

with open("headings.txt", "w", encoding="utf-8") as out:
    for f in files:
        if os.path.exists(f):
            out.write(f"--- {os.path.basename(f)} ---\n")
            with open(f, "r", encoding="utf-8") as file:
                for line_no, line in enumerate(file, 1):
                    if line.startswith("## 📄") or line.startswith("### 📄") or "แบบฝึกหัด" in line and line.startswith("###"):
                        out.write(f"{line_no}: {line.strip()}\n")
