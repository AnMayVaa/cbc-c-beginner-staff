# เฉลยแบบฝึกหัด บทที่ 3: การควบคุมทิศทางโปรแกรม

## 🎯 แบบฝึกหัด 3.1: เครื่องตัดเกรด
```c
#include <stdio.h>

int main() {
    int score;
    printf("Enter score: ");
    scanf("%d", &score);
    
    if(score > 100) {
        printf("Cheating!\n");
    } else if(score >= 80) {
        printf("Grade: A\n");
    } else if(score >= 70) {
        printf("Grade: B\n");
    } else if(score >= 60) {
        printf("Grade: C\n");
    } else if(score >= 50) {
        printf("Grade: D\n");
    } else {
        printf("Grade: F\n");
    }
    
    return 0;
}
```

## 🎯 แบบฝึกหัด 3.2: สแกนเนอร์เลขคู่เลขคี่
```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter number: ");
    scanf("%d", &num);
    
    if(num % 2 == 0) {
        printf("Even\n");
    } else {
        printf("Odd\n");
    }
    return 0;
}
```

## 🎯 แบบฝึกหัด 3.3: ลูปสูตรคูณ
```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter number: ");
    scanf("%d", &num);
    
    for(int i = 1; i <= 12; i++) {
        int result = num * i;
        printf("%d x %d = %d\n", num, i, result);
    }
    return 0;
}
```

## 🎯 แบบฝึกหัด 3.4: พิมพ์ดาวตามสั่ง
```c
#include <stdio.h>

int main() {
    int n;
    printf("Enter N: ");
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        printf("*");
    }
    printf("\n");
    
    return 0;
}
```
