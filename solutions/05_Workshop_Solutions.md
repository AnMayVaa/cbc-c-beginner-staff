# เฉลยโจทย์ Workshop ทั้ง 10 ข้อ

## 🟢 หมวด A: ใช้ความรู้พื้นฐาน

### 1. เครื่องคิดเลขจิ๋ว
```c
#include <stdio.h>

int main() {
    int a, b;
    char op;
    
    printf("Enter math expression (ex. 5 + 4): ");
    scanf("%d %c %d", &a, &op, &b); // รับเลข 2 ตัวและเครื่องหมายพร้อมกัน
    
    if(op == '+') {
        int result = a + b;
        printf("Result: %d\n", result);
    } else if(op == '-') {
        int result = a - b;
        printf("Result: %d\n", result);
    } else if(op == '*') {
        int result = a * b;
        printf("Result: %d\n", result);
    } else if(op == '/') {
        int result = a / b;
        printf("Result: %d\n", result);
    } else {
        printf("Error: Invalid Operator\n");
    }
    
    return 0;
}
```

### 2. ตู้กดน้ำอัตโนมัติ
```c
#include <stdio.h>

int main() {
    int money, choice;
    
    printf("Menu: 1=Water(10), 2=Cola(15)\n");
    printf("Insert money: ");
    scanf("%d", &money);
    
    printf("Select menu (1 or 2): ");
    scanf("%d", &choice);
    
    int price = 0;
    if(choice == 1) {
        price = 10;
    } else if(choice == 2) {
        price = 15;
    }
    
    if(money >= price) {
        int change = money - price;
        printf("Change: %d Baht\n", change);
    } else {
        int need = price - money;
        printf("Not enough money! Need %d more.\n", need);
    }
    
    return 0;
}
```

### 3. เกมทายใจตัวเลขปริศนา
```c
#include <stdio.h>

int main() {
    int secret = 42; // ล็อคเลขไว้ที่ 42
    int guess = 0;
    
    while(guess != secret) {
        printf("Guess the number: ");
        scanf("%d", &guess);
        
        if(guess > secret) {
            printf("Too high!\n");
        } else if(guess < secret) {
            printf("Too low!\n");
        }
    }
    
    printf("Correct! You win!\n");
    return 0;
}
```

### 4. พีระมิดดวงดาว
```c
#include <stdio.h>

int main() {
    int n;
    printf("Enter N: ");
    scanf("%d", &n);
    
    // ลูป i สำหรับจัดการจำนวนบรรทัด
    for(int i = 1; i <= n; i++) {
        // ลูป j สำหรับจัดการจำนวนดาวในแต่ละบรรทัด (อิงตามค่า i)
        for(int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n"); // ขึ้นบรรทัดใหม่เมื่อจบบรรทัด
    }
    
    return 0;
}
```

### 5. ค้นหาผู้ทำคะแนนสูงสุด
```c
#include <stdio.h>

int main() {
    int max = 0;
    int num = 0;
    
    while(num != -1) {
        printf("Enter score (-1 to stop): ");
        scanf("%d", &num);
        
        if(num > max) {
            max = num; // ถ้าเจอเลขที่มากกว่า max เดิม ให้เซฟทับทันที
        }
    }
    
    printf("Max score is %d\n", max);
    return 0;
}
```

---

## 🔴 หมวด B: จัดเต็มความรู้ (อาร์เรย์ และ ฟังก์ชัน)

### 6. เครื่องคิดเงินซุปเปอร์มาร์เก็ต
```c
#include <stdio.h>

float calc_total(int arr[]) {
    int sum = 0;
    for(int i = 0; i < 5; i++) {
        sum += arr[i];
    }
    return sum * 1.07; // บวก VAT 7%
}

int main() {
    int items[5] = {10, 20, 30, 40, 50};
    printf("Total + VAT: %.2f Baht\n", calc_total(items));
    return 0;
}
```

### 7. ค้นหาคนสอบผ่าน
```c
#include <stdio.h>

void check_pass_fail(int arr[]) {
    int pass_count = 0;
    int fail_count = 0;
    
    for(int i = 0; i < 10; i++) {
        if(arr[i] >= 50) {
            pass_count++;
        } else {
            fail_count++;
        }
    }
    
    printf("Pass: %d, Fail: %d\n", pass_count, fail_count);
}

int main() {
    int scores[10] = {10, 60, 80, 40, 50, 90, 100, 20, 30, 70};
    check_pass_fail(scores);
    return 0;
}
```

### 8. คาถากลับคำ
```c
#include <stdio.h>
#include <string.h> // ต้องอิมพอร์ตเพื่อใช้ฟังก์ชัน strlen()

int main() {
    char word[20];
    
    printf("Enter word: ");
    scanf("%s", word); // รับข้อความเก็บลง Array (ไม่ต้องมี &)
    
    int length = strlen(word); // หาความยาวของคำ
    
    // วนลูปถอยหลังจากตัวอักษรสุดท้าย
    for(int i = length - 1; i >= 0; i--) {
        printf("%c", word[i]);
    }
    
    printf("\n");
    return 0;
}
```

### 9. ตู้เอทีเอ็มส่วนตัว
```c
#include <stdio.h>

int deposit(int balance, int amount) {
    return balance + amount;
}

int withdraw(int balance, int amount) {
    if(balance >= amount) {
        return balance - amount;
    } else {
        printf("Error: Not enough balance!\n");
        return balance;
    }
}

void check_balance(int balance) {
    printf("Current Balance: %d Baht\n", balance);
}

int main() {
    int balance = 1000;
    int choice = -1;
    int amount;
    
    while(choice != 0) {
        printf("\nMenu: 1=Deposit, 2=Withdraw, 3=Check, 0=Exit\n");
        printf("Select menu: ");
        scanf("%d", &choice);
        
        if(choice == 1) {
            printf("Enter amount to deposit: ");
            scanf("%d", &amount);
            balance = deposit(balance, amount);
        } else if(choice == 2) {
            printf("Enter amount to withdraw: ");
            scanf("%d", &amount);
            balance = withdraw(balance, amount);
        } else if(choice == 3) {
            check_balance(balance);
        }
    }
    
    return 0;
}
```

### 10. ระบบสุ่มผู้โชคดี
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // เซ็ตระบบสุ่มตัวเลขตามเวลาปัจจุบัน (เพื่อให้เลขไม่ซ้ำกันทุกรอบ)
    srand(time(NULL));
    
    // รายชื่อผู้โชคดี (สมมติเก็บเป็นรหัสพนักงาน)
    int lucky_names[5] = {101, 102, 103, 104, 105};
    
    int index = rand() % 5; // สุ่มเลขตั้งแต่ 0 ถึง 4
    
    printf("The Winner is... ID: %d!\n", lucky_names[index]);
    
    return 0;
}
```
