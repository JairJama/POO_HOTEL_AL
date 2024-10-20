from .Reservas import Reservas
from datetime import datetime
class Facturacion:
    def __init__(self, nombre_cliente, apellido_cliente, numero_habitacion, fecha_entrada, fecha_salida, tarifa_diaria):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tarifa_diaria = tarifa_diaria
        self.activa = True
        self.reserva = Reservas(numero_habitacion, nombre_cliente, apellido_cliente, fecha_entrada, fecha_salida)

    #Getters

    def get_nombre_cliente(self):
        return self._nombre_cliente

    def get_apellido_cliente(self):
        return self._apellido_cliente

    def get_numero_habitacion(self):
        return self._numero_habitacion

    def get_fecha_entrada(self):
        return self._fecha_entrada

    def get_fecha_salida(self):
        return self._fecha_salida

    def get_tarifa_diaria(self):
        return self._tarifa_diaria

    def is_activa(self):
        return self._activa

    # Setters
    def set_nombre_cliente(self, nombre_cliente):
        self._nombre_cliente = nombre_cliente

    def set_apellido_cliente(self, apellido_cliente):
        self._apellido_cliente = apellido_cliente

    def set_numero_habitacion(self, numero_habitacion):
        self._numero_habitacion = numero_habitacion

    def set_fecha_entrada(self, fecha_entrada):
        self._fecha_entrada = fecha_entrada

    def set_fecha_salida(self, fecha_salida):
        self._fecha_salida = fecha_salida

    def set_tarifa_diaria(self, tarifa_diaria):
        self._tarifa_diaria = tarifa_diaria

    def set_activa(self, estado):
        self._activa = estado
    
    
    
    
    def calcular_total(self, fecha_entrada, fecha_salida, tarifa_diaria):
        dias = (fecha_salida - fecha_entrada).days
        return dias * tarifa_diaria

    def mostrar_detalle_reserva(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                                fecha_entrada, fecha_salida, tarifa_diaria, activa):
        total = self.calcular_total(fecha_entrada, fecha_salida, tarifa_diaria)
        detalle = f"""
        Detalle de la Reserva:
        ---------------------
        Cliente: {nombre_cliente} {apellido_cliente} 
        Habitación: {numero_habitacion}
        Fecha de Entrada: {fecha_entrada.strftime('%d/%m/%Y')}
        Fecha de Salida: {fecha_salida.strftime('%d/%m/%Y')}
        Tarifa Diaria: ${tarifa_diaria:.2f}
        Total a Pagar: ${total:.2f}
        Estado: {'Activa' if activa else 'Cancelada'}
        """
        return detalle

    def generar_factura(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                        fecha_entrada, fecha_salida, tarifa_diaria):
        total = self.calcular_total(fecha_entrada, fecha_salida, tarifa_diaria)
        iva = total * 0.15
        total_con_iva = total + iva
        factura = f"""
        FACTURA
        -------
        Cliente: {nombre_cliente} {apellido_cliente}
        Detalle:
        - Alojamiento en habitación {numero_habitacion}
        - Desde: {fecha_entrada.strftime('%d/%m/%Y')}
        - Hasta: {fecha_salida.strftime('%d/%m/%Y')}
        
        Subtotal: ${total:.2f}
        IVA (15%): ${iva:.2f}
        Total: ${total_con_iva:.2f}
        """
        return factura

    def cancelar_reserva(self, apellido_cliente, nombre_cliente, numero_habitacion):
        self.activa = False
        return f"La reserva para {apellido_cliente}, {nombre_cliente} en la habitación {numero_habitacion} ha sido cancelada."

    def modificar_reserva(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                        fecha_entrada, fecha_salida):
        print("¿Qué desea modificar?")
        print("1. Nombre del cliente")
        print("2. Apellido del cliente")
        print("3. Número de habitación")
        print("4. Fecha de entrada")
        print("5. Fecha de salida")
        print("6. Volver al menú principal")
        
        op_mod = int(input("Escoja una opción: "))
        
        if op_mod == 1:
            nombre_cliente = input("Ingrese el nuevo nombre: ")
        elif op_mod == 2:
            apellido_cliente = input("Ingrese el nuevo apellido: ")
        elif op_mod == 3:
            numero_habitacion = int(input("Ingrese el nuevo número de habitación: "))
        elif op_mod == 4:
            nueva_fecha = input("Ingrese la nueva fecha de entrada (DD/MM/YYYY): ")
            fecha_entrada = datetime.strptime(nueva_fecha, "%d/%m/%Y")
        elif op_mod == 5:
            nueva_fecha = input("Ingrese la nueva fecha de salida (DD/MM/YYYY): ")
            fecha_salida = datetime.strptime(nueva_fecha, "%d/%m/%Y")
        elif op_mod == 6:
            return "Volviendo al menu principal..."
        else:
            return "Opcion invalida."
        
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        
        return "Reserva modificada exitosamente."