// Zadanie №1
// Задача 1
// let student = {
//     name: "Арсений",
//     age: 16,
//     major: "Информатика"
//   };
//   let jsonStudent = JSON.stringify(student);
//   let newStudent = JSON.parse(jsonStudent);
//   console.log(newStudent);

// Задача 2
// let book = {
//     year: "1984",
//     author: "Джордж Оруэлл",
//     year: 1949,
//     genre: "Дистопия"
//   };
//   let jsonBook = JSON.stringify(book);
//   let parsedBook = JSON.parse(jsonBook);
//   console.log(parsedBook);

//Задача 3
// let employees = [
//     { name: "Алексей", position: "Разработчик", age: 30 },
//     { name: "Мария", position: "Дизайнер", age: 25 },
//     { name: "Иван", position: "Менеджер", age: 35 }
//   ];
//   let jsonEmployees = JSON.stringify(employees);
//   let newEmployees = JSON.parse(jsonEmployees);
//   console.log(newEmployees);

// // Zadanie №2
// // Задача 2
// function getMaxSalary(salaries) {
//     if (Object.keys(salaries).length === 0) {
//       return null;
//     }
//     let maxSalary = -Infinity; 
//     let maxSalaryEmployee = null; 
//     for (let employee in salaries) {
//       if (salaries[employee] > maxSalary) {
//         maxSalary = salaries[employee]; 
//         maxSalaryEmployee = employee; 
//       }
//     }
//     return maxSalaryEmployee; 
//   }
//   let salaries = {
//     "Иван": 3000,
//     "Мария": 4000,
//     "Алексей": 2500
//   };
//   let highestPaidEmployee = getMaxSalary(salaries);
//   console.log(highestPaidEmployee); 
//   let emptySalaries = {};
//   console.log(getMaxSalary(emptySalaries)); 

// Задача 1
// function countProperties(object) {
//     let Properties = 0;
    
//   for (const key in object) {
//     if (object.hascountProperties(key)){
//         Properties += key;
//     }
//   }
//     return Properties;
//   }

// Задача 3
// function averageValues(obj) {
//     let values = Object.values(obj);
//     if (values.length === 0) return 0; 
//     let sum = values.reduce((acc, val) => acc + val, 0);
//     return sum / values.length;//return 
//   }