/*eslint-disable*/
export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    cloneCar() {
        return new this.constructorSymbol.species;
    }
}

Car[Symbol.species] = function () {
    return this;
};
