# เฉลยแบบฝึกหัด บทที่ 4: อาร์เรย์ และ ฟังก์ชัน

## 🎯 แบบฝึกหัด 4.1: เครื่องคิดเงินรวม
```c
#include <stdio.h>

int main() {
    int arr[5];
    int sum = 0;
    
    for(int i = 0; i < 5; i++) {
        printf("Enter price %d: ", i + 1);
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    printf("Total: %d\n", sum);
    return 0;
}
```

## 🎯 แบบฝึกหัด 4.2: หาค่าเฉลี่ย
```c
#include <stdio.h>

int main() {
    int arr[5];
    int sum = 0;
    
    for(int i = 0; i < 5; i++) {
        printf("Enter price %d: ", i + 1);
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    // ต้องหารด้วย 5.0 เพื่อให้ผลลัพธ์เป็นทศนิยม (float)
    printf("Average: %.2f\n", sum / 5.0); 
    return 0;
}
```

## 🎯 แบบฝึกหัด 4.3: ฟังก์ชันทวีคูณ (Double It!)
```c
#include <stdio.h>

int double_number(int x) {
    return x * 2;
}

int main() {
    int result = double_number(5);
    printf("Double of 5 is %d\n", result);
    return 0;
}
```

## 🎯 แบบฝึกหัด 4.4: ฟังก์ชันเช็คผ่าน/ตก
```c
#include <stdio.h>

int check_pass(int score) {
    if(score >= 50) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    printf("Score 60: %d\n", check_pass(60));
    printf("Score 40: %d\n", check_pass(40));
    return 0;
}
```
