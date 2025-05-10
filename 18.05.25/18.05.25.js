// Задание 1
// Наследование
// Это механизм базирования объекта, class на другом объекте 
// (наследование на основе прототипа) или class


// class Human {
//     constructor(Firstname, secondname) {
//         this.Firstname = Firstname;
//         this.secondname = secondname;
//     }
// }
// class Singer extends Human {
//     constructor(Firstname, secondname, thirdname) {
//         super(Firstname, secondname);
//         this.thirdname = thirdname
//     }
// }







// Полиморфизм
// Основная его идея в ООП заключается в способности вызывать один и тот же метод для разных объектов, 
// и при этом каждый объект будет реагировать по-своему

// class Human {
//     constructor(Firstname, secondname) {
//         this.Firstname = Firstname;
//         this.secondname = secondname;
//     }

//     say() {
//         console.log(`Мое имя Арсений ${this.Firstname}`)
//     }
// }   

// class player extends Human {
//     constructor(Firstname, secondname, thirdname) {
//         super(Firstname, secondname);
//         this.thirdname = thirdname
//     }
//     say() {
//         console.log(`Лучший игрок cs S1mple ${this.player}`)
//     }
// }
// const dude = new Human ("Arseniy", "Dude ");
// const bestplayer = new player("S1mple","cs2")

// dude.say();
// bestplayer.say();






// Инкапсуляция
// Инкапсуляция включает в себя идею о том, что данные объекта не должны быть напрямую доступны. /
// Нужно вызывать методы вместо прямого доступа к данным.
// class Human {
//     constructor(Firstname, secondname) {
//         this.Firstname = Firstname;
//         this.secondname = secondname;
//     }

//     say() {
//         console.log(`Мое имя Арсений ${this.Firstname}`)
//     }

//     getsecondname(){
//     return this.secondname
// }
//     setsecondname(newsecondname) {
//         this._secondname = new secondname
//     }
// } 


// № Почему метод startEngine() в базовом классе Vehicle выбрасывает
// ошибку, а не реализует логику по умолчанию?

// Потому что у нас существует несколько типов машин  и мы запускаем функцию getinfo чтобы узнать информацию.



// № Как работает полиморфизм в методах startEngine
// сновная его идея в ООП заключается в способности вызывать один и тот же метод для разных объектов, 
//  и при этом каждый объект будет реагировать по-своему
// В нашем случае: мы создаем обьект и чтобы не обращаться к нему используем функцию super не обращаясь на прямую к обекту

// class Vehicle {
//     constructor(brand, model, year) {
//         this.brand = brand
//         this.model = model
//         this.year = year
//         this.speed = 0
//         this.engine = false
//     }

//     lass GasolineCar extends Vehicle {
//         constructor(brand, model, year, fuelCapacity) {
//             super(brand, model, year);
//             this.fuelCapacity = fuelCapacity; // Объем топливного бака;
//             this.currentFuel = fuelCapacity; // Текущий уровень топлива;
//         }

//         Еще:
      
//         lass ElecrticCar extends Vehicle {
//             constructor(brand, model, year, batteryCapacity) {
//                 super(brand, model, year);
//                 this.batteryCapacity = batteryCapacity // Емкость батареи кВт . ч
//                 this.currentCharge = batteryCapacity // Текущий заряд


//             }









// Задание 2
class Vehicle {
    constructor(brand, model, year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0;
        this.engine = false;
    }

    startEngine() {
        throw new Error("Метод должен быть в подклассе");
    }

    stopEngine() {
        this.engine = false;
        console.log(`${this.getInfo()} двигатель выключен`);
    }

    // Метод ускорения
    acceleration(amount) {
        if (!this.engine) {
            console.log("Сначала запустите двигатель");
            return;
        }
        this.speed += amount;
        console.log(`${this.getInfo()} ускоряется до ${this.speed} км/ч`);
    }

    // Метод торможения
    brake(amount) {
        this.speed = Math.max(0, this.speed - amount);
        console.log(`${this.getInfo()} замедляется до ${this.speed} км/ч`);
    }

    // Получение инфы об авто
    getInfo() {
        return `${this.brand} ${this.model} ${this.year}`;
    }

    // Метод сигнализации
    honk() {
        console.log(`${this.getInfo()} сигналит: Бип-бип!`);
    }

    headlights() {
        console.log(`${this.getInfo()} Фары включены`);
       }
}

class GasolineCar extends Vehicle {
    constructor(brand, model, year, fuelCapacity) {
        super(brand, model, year);
        this.fuelCapacity = fuelCapacity; // Объем топливного бака;
        this.currentFuel = fuelCapacity; // Текущий уровень топлива;
    }

    startEngine() {
        if (this.currentFuel <= 0) {
            console.log("Нет топлива! Едь на росНефть");
            return false;
        }
        this.engine = true;
        console.log(`${this.getInfo()} двигатель запущен (бензин)`);
        return true;
    }

    refuel(liters) {
        this.currentFuel = Math.min(this.fuelCapacity, this.currentFuel + liters);
        console.log(`Заправлено. Топлива ${this.currentFuel} литров. ${this.fuelCapacity}`);
    }

    acceleration(amount) {
        if (!this.startEngine()) return; 
        let fuelConsumption = amount * 0.1; 
        if (this.currentFuel < fuelConsumption) {
            console.log("Недостаточно топлива");
            return;
        
        }
        this.currentFuel -= fuelConsumption;
        super.acceleration(amount);
        console.log(`Остаток топлива ${this.currentFuel.toFixed(1)} литра`);
    }
}

class DieselCar extends Vehicle {
    constructor(brand, model, year, fuelCapacity){
      super(brand, model, year);
      this.fuelCapacity = fuelCapacity;
      this.currentFuel = fuelCapacity;
    }
    
    startEngine() {
      if (this.currentFuel <= 0){
          console.log("Нет топлива! Едь на ГазПромНефть");
          return false;
      }
      this.engine = true;
      console.log(`${this.getInfo()} Двигатель запущен (дизель)`);
      return true;
  }
  
  refuel(liters) {
      this.currentFuel = Math.min(this.fuelCapacity, this.currentFuel + liters); 
      console.log(`Заправлено. Дизель ${this.currentFuel} литров. ${this.fuelCapacity}`);
  }

  acceleration(amount) {
      if (!this.startEngine()) return; 
      let fuelConsumption = amount * 0.1; 
      if (this.currentFuel < fuelConsumption) {
          console.log("Недостаточно топлива");
          return;
      }
      this.currentFuel -= fuelConsumption;
      super.acceleration(amount);
      console.log(`Остаток топлива ${this.currentFuel.toFixed(3)} литра`);
  }
}

class ElectricCar extends Vehicle {
  constructor(brand, model, year, batteryCapacity) {
      super(brand, model, year);
      this.batteryCapacity = batteryCapacity; // Емкость батареи кВт . ч
      this.currentCharge = batteryCapacity; // Текущий заряд
  }
  startEngine() {
      if (this.currentCharge <= 0) {
          console.log("Батарея разряжена");
          return false;
      }
      this.engine = true;
      console.log(`${this.getInfo()} двигатель запущен`);
      return true;
  }

  charge(kwh) {
      this.currentCharge = Math.min(this.batteryCapacity, this.currentCharge + kwh);
      console.log(`Заряжено. Батарея: ${this.currentCharge.toFixed(1)} кВт * ч. из ${this.batteryCapacity} кВч`);
  }

  acceleration(amount) {
      if (!this.startEngine()) return; 
      let energyConsumption = amount * 0.05; 
      if (this.currentCharge < energyConsumption) {
          console.log("Недостаточно заряда, едь на станцию");
          return;
      }
      this.currentCharge -= energyConsumption;
      super.acceleration(amount);
      console.log(`Остаток заряда: ${this.currentCharge.toFixed(1)} кВт Ч.`);
  }
}

class HybridCar extends GasolineCar {
  constructor(brand, model, year, fuelCapacity, batteryCapacity) {
      super(brand, model, year, fuelCapacity);
      this.batteryCapacity = batteryCapacity;
      this.currentCharge = batteryCapacity;
      this.electricMode = false;
  }

  startEngine() {
     if (this.currentCharge > 0) { 
         this.engine = true; 
         this.electricMode = true; 
         console.log(`${this.getInfo()} двигатель запущен (электрический режим)`); 
         return true; 
     } else if (this.currentFuel > 0) { 
         this.engine = true; 
         this.electricMode = false; 
         console.log(`${this.getInfo()} двигатель запущен (бензиновый режим)`); 
         return true; 
     } 
     console.log("Нет заряда и топлива"); 
     return false; 
   }

   acceleration(amount) { 
       if (this.electricMode) { 
           let energyConsumption = amount * 0.04; 
           if (this.currentCharge < energyConsumption) { 
               console.log(`Переключаемся на бензин`); 
               this.electricMode = false;
               if (this.currentFuel <= 0) { 
                   console.log("Бензин закончился"); 
                   return; 
               } 
           } else { 
               this.currentCharge -= energyConsumption; 
               super.acceleration(amount); 
               console.log(`(Электро) остаток заряда: ${this.currentCharge.toFixed(1)} кВт Ч.`); 
               return; 
           } 
       } 

       let fuelConsumption = amount * 0.1;

       if (this.currentFuel <= 0) { 
           console.log("Бензин закончился"); 
           return; 
       } 
       this.currentFuel -= fuelConsumption;
       super.acceleration(amount);
       console.log(`(Бензин) Остаток топлива ${this.currentFuel.toFixed(1)} литров.`); 
   } 
   honk() { // Переопределяем метод honk для гибридного автомобиля
       super.honk();
       console.log(`${this.getInfo()} сигналит с использованием электрического режима!`);
   }
   headlights() {//Метод 
    super.headlights() //Метод headlights для освещения дороги
    console.log(`${this.getInfo()} Фары включены`);
   }
}
// Демонстрация полиморфизма.
function testDrive(vehicle) {
   console.log('Тест драйв для:', vehicle.getInfo());
   
   vehicle.startEngine();
   vehicle.headlights();
   vehicle.honk(); 
   vehicle.acceleration(20);
   vehicle.acceleration(30);
   vehicle.brake(15);
   vehicle.acceleration(25);
   vehicle.startEngine();
}

let gasolineCar = new GasolineCar("Opel", "Zafira", 2007, 60);
let dieselCar = new DieselCar("Toyota", "Prado", 2011, 30);
let electricCar = new ElectricCar("Tesla", "Model X", 2020, 75);
let hybridCar = new HybridCar("Toyota", "Prius", 2021, 45, 5);

testDrive(gasolineCar);
testDrive(electricCar);
testDrive(hybridCar);
testDrive(dieselCar);