// № Задача 1
// new Promise(function(resolve, reject) {

//   setTimeout(() => resolve(1), 1000); // (*)

// }).then(function(result) { // (**)

//   alert(result); // 1
//   return result * 2;

// }).then(function(result) { // (***)

//   alert(result); // 2
//   return result * 5;

// }).then(function(result) {

//   alert(result); // 4
//   return result * 5;

// });

// № Задача 2
// function generateRandomNumber() {
//     return new Promise((resolve, reject) => {
//         const randomNumber = Math.floor(Math.random() * 10) + 1; 
//         if (randomNumber < 5) {
//             reject(new Error("Число слишком маленькое")); 
//         } else {
//             resolve(randomNumber); 
//         }
//     });
// }
// // Цепочка промиссов
// generateRandomNumber()
//     .then(randomNumber => {
//         console.log(`Сгенерированное число: ${randomNumber}`);
//         return randomNumber * 2; 
//     })
//     .then(doubledNumber => {
//         console.log(`Удвоенное число: ${doubledNumber}`);
//         return doubledNumber + 5; 
//     })
//     .then(finalResult => {
//         console.log(`Финальный результат: ${finalResult}`);
//     })
//     .catch(error => {
//         console.error('Произошла ошибка:', error.message);
//     });

// № Задача 3
// Функция для генерации случайного числа от 1 до 10
// function generateRandomNumber() {
//     return new Promise((resolve, reject) => {
//         const randomNumber = Math.floor(Math.random() * 10) + 1;
//         if (randomNumber < 5) {
//             reject(new Error("Число слишком маленькое")); 
//         } else {
//             resolve(randomNumber);
//         }
//     });
// }
// // Цепочка промиссов
// generateRandomNumber()
//     .then(randomNumber => {
//         console.log(`Сгенерированное число: ${randomNumber}`);
//         return randomNumber * 2; 
//     })
//     .then(doubledNumber => {
//         console.log(`Удвоенное число: ${doubledNumber}`); 
//     })
//     .catch(error => {
//         console.error('Произошла ошибка:', error.message); 
//     });