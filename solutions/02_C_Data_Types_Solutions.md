# เฉลยแบบฝึกหัด บทที่ 2: ชนิดข้อมูล (Data Types)

## 🎯 แบบฝึกหัด 2.1: เครื่องคิดเลขคูณเลข
```c
#include <stdio.h>

int main() {
    int num1, num2;
    
    printf("Enter number 1: ");
    scanf("%d", &num1);
    
    printf("Enter number 2: ");
    scanf("%d", &num2);
    
    int result = num1 * num2;
    printf("Result: %d\n", result);
    return 0;
}
```

## 🎯 แบบฝึกหัด 2.2: หาพื้นที่สี่เหลี่ยมผืนผ้า
```c
#include <stdio.h>

int main() {
    float width, length;
    
    printf("Enter width: ");
    scanf("%f", &width);
    
    printf("Enter length: ");
    scanf("%f", &length);
    
    float area = width * length;
    printf("Area = %.2f\n", area);
    return 0;
}
```

## 🎯 แบบฝึกหัด 2.3: แม่ค้าทอนเงิน
```c
#include <stdio.h>

int main() {
    int price = 35;
    int pay = 100;
    
    int change = pay - price;
    printf("Change: %d Baht\n", change);
    return 0;
}
```
