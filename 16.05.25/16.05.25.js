
class Spaceship {
    constructor() {
        // Здесь можно добавить свойства для Spaceship, если нужно
    }
}
class Nasa extends Spaceship {
    constructor(name, fuel, speed) {
        super(); // Вызов конструктора родительского класса
        this.name = name;
        this.fuel = fuel;
        this.speed = speed;
    }
    getStatus() {
        return `${this.name}, ${this.speed}, ${this.fuel}`;
    }
    launch() {
        console.log(`${this.speed} Скорость увеличена на 50 км/ч, расход топлива снижен`);
    }
    refuel() {
        console.log(`${this.fuel} Долито 60л`);
    }
}
// Функция для взлета ракеты
function RocketTakeoff(spaceship) {
    console.log(`Взлет и полет ракеты: ${spaceship.getStatus()}`);
    spaceship.launch();
    spaceship.refuel();
}
// Пример использования
const myNasa = new Nasa('CatShip', 100, 200);
RocketTakeoff(myNasa);