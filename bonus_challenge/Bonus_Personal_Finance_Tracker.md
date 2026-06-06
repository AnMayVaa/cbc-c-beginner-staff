# Bonus Challenge: ระบบจัดการรายรับ-รายจ่ายส่วนตัว (Personal Finance Tracker)

โจทย์นี้ถูกออกแบบให้เป็นโจทย์ปิดท้ายค่าย ที่ครอบคลุมทุกเรื่องที่เรียนมา (ตัวแปร, ชนิดข้อมูล, if-else, ลูป, Array, ฟังก์ชัน) และเป็นโปรแกรมที่สามารถนำไปประยุกต์ใช้จัดการเงินในชีวิตจริงได้

---

## ส่วนที่ 1: บทพูดสำหรับผู้สอน (Speaker Notes)

### เกริ่นนำ (ใช้เวลาประมาณ 3-5 นาที)

> เอาล่ะครับ ข้อสุดท้ายนี้จะเป็นโจทย์ใหญ่ที่รวมทุกอย่างที่เราเรียนมาทั้งวันเลย
> 
> ลองนึกภาพดูนะครับ สมมติว่าเราอยากรู้ว่าในแต่ละวันเราใช้เงินไปกับอะไรบ้าง ใช้ไปเท่าไหร่ แล้วเหลือเงินกี่บาท ถ้าเราจดใส่กระดาษมันก็ได้ แต่ถ้าเราเขียนโปรแกรมให้มันคิดให้เราล่ะ? 
> 
> โจทย์นี้เราจะเขียน "ระบบจัดการรายรับ-รายจ่ายส่วนตัว" โดยเราจะต้องใช้ทุกสิ่งที่เรียนมา:
> - **ตัวแปร** เก็บยอดเงินคงเหลือ
> - **Array** เก็บรายจ่ายแต่ละรายการ
> - **ฟังก์ชัน** แยกการทำงานให้เป็นระเบียบ
> - **if-else** ตรวจสอบว่าเงินพอจ่ายไหม
> - **ลูป** ทำให้ระบบวนรับคำสั่งจากผู้ใช้ได้เรื่อยๆ
> 
> ข้อนี้ค่อนข้างยาวนะครับ ไม่ต้องรีบ ค่อยๆ ทำไป ถ้าติดตรงไหนยกมือถามได้เลย

### จุดที่ควรเน้นย้ำระหว่างเด็กทำ

> - ถ้าเด็กเริ่มไม่ถูก ให้แนะนำว่า "ลองเริ่มจากสร้างเมนูก่อนเลย ใช้ while loop ครอบ แล้ว if-else เช็คว่าผู้ใช้เลือกเมนูอะไร"
> - ถ้าเด็กถามว่า "จะเก็บชื่อหมวดหมู่ยังไง" ให้ตอบว่า "ใช้ตัวเลขแทนก็ได้ครับ เช่น 1 = อาหาร, 2 = เดินทาง ไม่ต้องเก็บเป็นตัวอักษรก็ได้"
> - ถ้าเด็กทำฟังก์ชันไม่เป็น ให้แนะนำ "ลองเขียนทุกอย่างไว้ใน main ก่อนให้มันทำงานได้ แล้วค่อยแยกออกมาเป็นฟังก์ชันทีหลัง"

---

## ส่วนที่ 2: ไกด์สไลด์ (Slide Guide)

### สไลด์ที่ 1: แนะนำโจทย์
**หัวข้อ:** Bonus Challenge: Personal Finance Tracker  
**เนื้อหาบนสไลด์:**
- เขียนโปรแกรมจัดการรายรับ-รายจ่ายส่วนตัว
- ผู้ใช้สามารถ: เพิ่มรายจ่าย / ดูสรุปรายจ่ายทั้งหมด / ดูยอดเงินคงเหลือ / ออกจากโปรแกรม

### สไลด์ที่ 2: ฟีเจอร์ที่ต้องมี
**เนื้อหาบนสไลด์:**
1. ตั้งเงินเริ่มต้น (Budget) ตอนเริ่มโปรแกรม
2. เพิ่มรายจ่าย โดยเลือกหมวดหมู่ (1=อาหาร, 2=เดินทาง, 3=อื่นๆ) และป้อนจำนวนเงิน
3. ดูสรุป: แสดงรายจ่ายทั้งหมดที่บันทึกไว้ พร้อมยอดรวม
4. ดูยอดคงเหลือ: เงินเริ่มต้น - รายจ่ายทั้งหมด
5. ถ้าเงินไม่พอจ่าย ให้เตือนผู้ใช้

### สไลด์ที่ 3: ตัวอย่าง Output
```text
Enter your budget: 500

=== Personal Finance Tracker ===
1. Add Expense
2. View Summary
3. Check Balance
0. Exit
Select: 1

Category (1=Food, 2=Transport, 3=Other): 1
Amount: 120
Expense added!

Select: 1
Category (1=Food, 2=Transport, 3=Other): 2
Amount: 45
Expense added!

Select: 2
--- Expense Summary ---
#1 [Food]      120 Baht
#2 [Transport]  45 Baht
Total Expenses: 165 Baht

Select: 3
Remaining Balance: 335 Baht

Select: 0
Goodbye!
```

### สไลด์ที่ 4: คำใบ้ (Hints)
**เนื้อหาบนสไลด์:**
- ใช้ Array 2 ชุด: `int amounts[20]` เก็บจำนวนเงิน, `int categories[20]` เก็บหมวดหมู่
- ใช้ตัวแปร `int count = 0` ไว้นับว่าตอนนี้มีรายจ่ายกี่รายการแล้ว
- สร้างฟังก์ชันแยกอย่างน้อย 2 ตัว (เช่น `add_expense`, `view_summary`)
- ใช้ `while` ลูปในการสร้างเมนูหลัก

---

## ส่วนที่ 3: เฉลย (Solution)

```c
#include <stdio.h>

// ตัวแปร Global เพื่อให้ทุกฟังก์ชันเข้าถึงข้อมูลได้
int amounts[20];     // เก็บจำนวนเงินแต่ละรายการ (รองรับสูงสุด 20 รายการ)
int categories[20];  // เก็บหมวดหมู่ของแต่ละรายการ
int count = 0;       // จำนวนรายจ่ายที่บันทึกไว้ในตอนนี้

// ฟังก์ชันเพิ่มรายจ่าย
// รับค่ายอดเงินคงเหลือ (balance) เข้ามา เพื่อตรวจสอบว่าเงินพอจ่ายหรือไม่
// return: ยอดเงินคงเหลือหลังหักค่าใช้จ่าย (หากเงินพอ)
int add_expense(int balance) {
    int cat, amt;

    printf("\nCategory (1=Food, 2=Transport, 3=Other): ");
    scanf("%d", &cat);

    printf("Amount: ");
    scanf("%d", &amt);

    // ตรวจสอบว่ายอดเงินคงเหลือเพียงพอหรือไม่
    if (amt > balance) {
        printf("Warning: Not enough balance! You only have %d Baht.\n", balance);
        return balance; // ไม่หักเงิน คืนยอดเดิมกลับไป
    }

    // บันทึกข้อมูลลงใน Array
    amounts[count] = amt;
    categories[count] = cat;
    count++;

    int new_balance = balance - amt;
    printf("Expense added! Remaining: %d Baht\n", new_balance);
    return new_balance; // คืนยอดเงินใหม่กลับไป
}

// ฟังก์ชันแสดงสรุปรายจ่ายทั้งหมด
void view_summary() {
    if (count == 0) {
        printf("\nNo expenses recorded yet.\n");
        return;
    }

    printf("\n--- Expense Summary ---\n");
    int total = 0;

    for (int i = 0; i < count; i++) {
        // แปลงตัวเลขหมวดหมู่ให้เป็นข้อความที่อ่านเข้าใจ
        if (categories[i] == 1) {
            printf("#%d [Food]      %d Baht\n", i + 1, amounts[i]);
        } else if (categories[i] == 2) {
            printf("#%d [Transport] %d Baht\n", i + 1, amounts[i]);
        } else {
            printf("#%d [Other]     %d Baht\n", i + 1, amounts[i]);
        }
        total = total + amounts[i];
    }

    printf("Total Expenses: %d Baht\n", total);
}

int main() {
    int budget;
    printf("Enter your budget: ");
    scanf("%d", &budget);

    int balance = budget;
    int choice = -1;

    while (choice != 0) {
        printf("\n=== Personal Finance Tracker ===\n");
        printf("1. Add Expense\n");
        printf("2. View Summary\n");
        printf("3. Check Balance\n");
        printf("0. Exit\n");
        printf("Select: ");
        scanf("%d", &choice);

        if (choice == 1) {
            balance = add_expense(balance);
        } else if (choice == 2) {
            view_summary();
        } else if (choice == 3) {
            printf("\nRemaining Balance: %d Baht\n", balance);
        } else if (choice == 0) {
            printf("\nGoodbye!\n");
        }
    }

    return 0;
}
```

### อธิบายโค้ดเฉลย (สำหรับสตาฟฟ์อ่านทำความเข้าใจ)

**ภาพรวม:**
โปรแกรมนี้ทำงานเหมือนแอปจดรายจ่ายง่ายๆ ผู้ใช้ตั้งงบประมาณเริ่มต้น จากนั้นสามารถเพิ่มรายจ่าย ดูสรุป หรือเช็คยอดเงินคงเหลือได้เรื่อยๆ ผ่านระบบเมนู

**ความรู้ที่ใช้ (ครบทุกบท):**

| บทที่ | หัวข้อ | ตรงส่วนไหนของโค้ด |
| --- | --- | --- |
| 1 | `printf` / `scanf` | รับค่า Budget, แสดงเมนู, แสดงผลสรุป |
| 2 | ตัวแปร, การคำนวณ | `budget`, `balance`, `total`, การคำนวณ `balance - amt` |
| 3 | `if-else` | ตรวจสอบเมนู, ตรวจสอบเงินพอจ่ายไหม, แปลง Category เป็นข้อความ |
| 3 | `while` ลูป | ระบบเมนูหลักที่วนรับคำสั่งไปเรื่อยๆ |
| 4 | Array | `amounts[]` และ `categories[]` เก็บข้อมูลหลายรายการ |
| 4 | ฟังก์ชัน | `add_expense()` และ `view_summary()` แยกการทำงานออกจาก `main` |

**จุดที่อาจทำให้เด็กติด (สตาฟฟ์เตรียมตัวช่วยไว้):**
1. **การ return ค่า balance กลับมา** — เด็กมักจะลืมว่าตัวแปรในฟังก์ชันเป็นคนละตัวกับใน `main` ต้อง return กลับมาอัปเดต
2. **ตัวแปร count ที่ทำหน้าที่ชี้ตำแหน่ง** — เด็กอาจจะไม่เข้าใจว่า `count` ทำหน้าที่ "ตำแหน่งว่างถัดไป" ใน Array 
3. **การแปลงเลข Category เป็นข้อความ** — ส่วนนี้ถ้าเด็กทำไม่ได้ ให้แนะนำว่า "พิมพ์แค่เลข Category ออกมาก่อนก็ได้ ไม่ต้องแปลงเป็นข้อความ"
