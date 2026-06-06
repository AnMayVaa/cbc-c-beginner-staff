# เฉลยแบบฝึกหัด บทที่ 1: โครงสร้างพื้นฐานของภาษา C

## 🎯 แบบฝึกหัด 1.1: ทักทายโลกกว้าง
```c
#include <stdio.h>

int main() {
    printf("Hello CBC Boost Camp!\n");
    printf("My name is Antigravity\n"); // เปลี่ยนเป็นชื่อตัวเอง
    printf("I love Pizza!\n"); // ของกินที่ชอบ
    return 0;
}
```

## 🎯 แบบฝึกหัด 1.2: เครื่องคิดเลขคำนวณปีเกิด
```c
#include <stdio.h>

int main() {
    int birth_year;
    
    printf("Enter birth year (CE): ");
    scanf("%d", &birth_year);
    
    printf("You are %d years old!\n", 2026 - birth_year);
    return 0;
}
```

## 🎯 แบบฝึกหัด 1.3: แฟ้มประวัติส่วนตัว
```c
#include <stdio.h>

int main() {
    int age, weight;
    
    printf("Enter your age: ");
    scanf("%d", &age);
    
    printf("Enter your weight: ");
    scanf("%d", &weight);
    
    printf("You are %d years old and your weight is %d!\n", age, weight);
    return 0;
}
```
