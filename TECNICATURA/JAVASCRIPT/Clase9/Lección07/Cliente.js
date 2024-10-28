class Cliente extends Persona {
    static contadorCliente = 0;

constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this._idCliente = ++Cliente.contadorCliente;
    this._fechaRegistro = fechaRegistro;
}
    
    // Getter para idCliente
    get idCliente() {
        return this._idCliente;
    }
    
    // Getter para fechaRegistro
    get fechaRegistro() {
        return this._fechaRegistro;
    }
    
    // Setter para fechaRegistro
    set fechaRegistro(nuevaFecha) {
        this._fechaRegistro = nuevaFecha;
    }
    
    // Método toString
    toString() {
        return `${super.toString()}, Cliente ID: ${this._idCliente}, Fecha de Registro: ${this._fechaRegistro}`;
    }
}