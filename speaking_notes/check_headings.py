with open("headings_check.txt", "w", encoding="utf-8") as out:
    for f in ["Speaker_Notes_Lesson1.md", "Speaker_Notes_Lesson2.md", "Speaker_Notes_Lesson3.md"]:
        out.write(f"\n--- {f} ---\n")
        with open(f, "r", encoding="utf-8") as file:
            for line in file:
                if "หน้าที่" in line:
                    out.write(line)
