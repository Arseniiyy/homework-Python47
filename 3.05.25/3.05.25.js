
//  Задание 1.
// function factorial(n) {
//     if (n < 0) {
//         return -1;
//     }
//     if (n === 0) {
//         return 1;
//     }
//     return n * factorial(n - 1);
// }
// console.log(factorial(5)); 
// console.log(factorial(0)); 
// console.log(factorial(-3)); 

//  Задание 2.
// function sumOfDigits(n) {
//     n = Math.abs(n);
//     if (n === 0) {
//         return 0;
//     }

//     return (n % 10) + sumOfDigits(Math.floor(n / 10));
// }
// console.log(sumOfDigits(1234)); 
// console.log(sumOfDigits(-567));  
// console.log(sumOfDigits(0)); 

//  Задание 3.
// function printNumbers(n) {
//     if (n <= 0) {
//         return;
//     }
//     console.log(n);
//     printNumbers(n - 1);
//     console.log(n);
// }
// printNumbers(3); 

// Задание 4
// function isPalindrome(str) {
//     str = str.replace(/\s+/g, '').toLowerCase();
//     if (str.length <= 1) {
//         return true;
//     }
//     if (str[0] !== str[str.length - 1]) {
//         return false; 
//     }
//     return isPalindrome(str.slice(1, str.length - 1));
// }

// console.log(isPalindrome("A man a plan a canal Panama")); 
// console.log(isPalindrome("Was it a car or a cat I saw"));
// console.log(isPalindrome("Hello")); 

// Задание 5
// function fastExponentiation(a, n) {

//     if (n === 0) {
//         return 1;
//     }
//     if (n % 2 === 0) {
//         const half = fastExponentiation(a, n / 2);
//         return half * half; // a^n = (a^(n/2))^2
//     } else {
//         return a * fastExponentiation(a, n - 1); // a^n = a * a^(n-1)
//     }
// }
// console.log(fastExponentiation(2, 10)); 
// console.log(fastExponentiation(3, 5));  
// console.log(fastExponentiation(5, 0));  
// console.log(fastExponentiation(7, 3));  