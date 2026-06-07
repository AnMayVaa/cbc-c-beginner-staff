import os
import re

dir_path = r"C:\Antigravity\cbc-c-beginner-staff\speaking_notes"

content = ""
for f in ["Speaker_Notes_Lesson1.md", "Speaker_Notes_Lesson2.md", "Speaker_Notes_Lesson3.md"]:
    with open(os.path.join(dir_path, f), "r", encoding="utf-8") as file:
        content += "\n" + file.read()

def extract_blocks(text):
    pattern = r"(^(?:##|###) 📄 หน้าที่ [\d\.]+(?:.*)$|^(?:##|###) 🏋️ แบบฝึกหัด .*$)"
    parts = re.split(pattern, text, flags=re.MULTILINE)
    
    blocks = []
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i+1].strip()
        blocks.append({"heading": heading, "body": body})
    return parts[0], blocks

pre_text, blocks = extract_blocks(content)

normal_slides = []
exercises = {}

for b in blocks:
    if "🏋️ แบบฝึกหัด" in b['heading']:
        match = re.search(r"แบบฝึกหัด (\d+\.\d+)", b['heading'])
        if match:
            ex_num = match.group(1)
            exercises[ex_num] = b
    else:
        match = re.search(r"หน้าที่ ([\d\.]+)", b['heading'])
        if match:
            old_num = float(match.group(1))
            
            # Fix anomalies in the original text
            if old_num == 3 and "switch-case" in b['heading']:
                old_num = 35.0  # Force it to its real old number
            
            normal_slides.append((old_num, b))

# Sort to process sequentially
normal_slides.sort(key=lambda x: x[0])

old_to_new = {
    1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
    19:20, 20:21, 21:22, 22:23, 23:24, 24:25, 
    25.1:26.1, 25.2:26.2, 25.3:26.3, 25.4:26.4,
    26:27,
    27.1:28.1, 27.2:28.2, 27.3:28.3,
    28.1:29.1, 28.2:29.2,
    29.1:30.1, 29.2:30.2, 29.3:30.3,
    
    30:33, 31:34, 32:35,
    33:39, 34:40, 35:41, 36:42, 37:43,
    38:46, 39:47, 40:48,
    
    41:51, 42:52, 43:53, 44:54,
    45:57, 46:58, 47:59, 48:60, 49:61, 50:62, 51:63, 53:63.5
}

ex_mapping = {
    "1.1": 19, "1.2": 31, "1.3": 32,
    "2.1": 36, "2.2": 37, "2.3": 38,
    "3.1": 44, "3.2": 45, "3.3": 49, "3.4": 50,
    "4.1": 55, "4.2": 56, "4.3": 64, "4.4": 65
}

new_slides = []

for old_num, b in normal_slides:
    if old_num in old_to_new:
        new_num = old_to_new[old_num]
        if new_num.is_integer() or new_num == 63.5:
            new_num_str = str(int(new_num)) if new_num.is_integer() else "63.5"
            new_heading = re.sub(r"(หน้าที่ )([\d\.]+)", rf"\g<1>{new_num_str}", b['heading'])
            
            # Ensure proper heading level
            if new_heading.startswith("###"):
                new_heading = new_heading.replace("###", "##", 1)
                
            new_slides.append((new_num, new_heading, b['body']))
        else:
            new_num_str = str(new_num)
            new_heading = re.sub(r"(หน้าที่ )([\d\.]+)", rf"\g<1>{new_num_str}", b['heading'])
            if new_heading.startswith("###"):
                new_heading = new_heading.replace("###", "##", 1)
            new_slides.append((new_num, new_heading, b['body']))
    else:
        print(f"Warning: {old_num} not in mapping")
        new_slides.append((old_num, b['heading'], b['body']))

for ex_num, page in ex_mapping.items():
    if ex_num in exercises:
        b = exercises[ex_num]
        title_stripped = re.sub(r"^(?:###|##)\s*", "", b['heading'])
        new_heading = f"## 📄 หน้าที่ {page}: {title_stripped}"
        new_slides.append((page, new_heading, b['body']))

new_slides.sort(key=lambda x: x[0])

lesson1_slides = [s for s in new_slides if s[0] <= 32]
lesson2_slides = [s for s in new_slides if 33 <= s[0] <= 50]
lesson3_slides = [s for s in new_slides if 51 <= s[0] <= 65]

def write_file(filename, title, slides):
    with open(os.path.join(dir_path, filename), "w", encoding="utf-8") as out:
        out.write(f"# {title}\n\n")
        out.write("> **วิธีใช้เอกสารนี้:** เอกสารฉบับนี้ออกแบบมาให้ผู้สอนใช้เป็น *สคริปต์แบบคำต่อคำ* สำหรับพูดประกอบสไลด์\n")
        out.write("> ในแต่ละหน้าจะมี 3 ส่วน:\n")
        out.write("> 1. 🎤 **บทพูด** — สิ่งที่ผู้สอนควร \"พูด\" ออกเสียง\n")
        out.write("> 2. 📊 **สิ่งที่ต้องแสดงในสไลด์** — เนื้อหาที่ควร \"โชว์\" บนจอ\n")
        out.write("> 3. 💡 **เทคนิคการสอน** — เคล็ดลับเฉพาะจุดสำหรับผู้สอน\n\n---\n\n")
        
        for num, heading, body in slides:
            out.write(f"{heading}\n\n{body}\n\n---\n\n")

write_file("Speaker_Notes_Lesson1.md", "🎙️ สคริปต์ผู้สอน C Beginner — บทที่ 1 (Slides 1-32)", lesson1_slides)
write_file("Speaker_Notes_Lesson2.md", "🎙️ สคริปต์ผู้สอน C Beginner — บทที่ 2 (Slides 33-50)", lesson2_slides)
write_file("Speaker_Notes_Lesson3.md", "🎙️ สคริปต์ผู้สอน C Beginner — บทที่ 3 (Slides 51-65)", lesson3_slides)

print("Done! Files have been perfectly updated.")
