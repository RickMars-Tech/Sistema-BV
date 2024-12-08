import sys 

class Libro: 
    def __init__(self, titulo, autor, isbn): 
        self.titulo = titulo 
        self.autor = autor 
        self.isbn = isbn 
        self.estado = "" 
        
    def recuperar_informacion(self): 
        return self.titulo + "," + self.autor + "," + self.isbn + "," + self.estado + "," 
    
class Usuario: 
    def __init__(self, user_id, nombre, rol): 
        self.user_id = user_id 
        self.nombre = nombre 
        self.rol = rol 
        
    def consultar_informacion(self): 
        return self.user_id + "," + self.nombre + "," + self.rol + "," 
    
class Lector(Usuario): 
    def __init__(self, user_id, nombre, rol): 
        super().__init__(user_id, nombre, rol) 
        
class Bibliotecario(Usuario): 
    def __init__(self, user_id, nombre, rol): 
        super().__init__(user_id, nombre, rol) 
        
class UsDefault(Usuario): 
    def __init__(self, user_id, nombre, rol): 
        super().__init__(user_id, nombre, rol) 
        
class Prestamo: 
    def __init__(self, libro, usuario): 
        self.libro = libro 
        self.usuario = usuario 
        self.fecha_prestamo = "" 
        self.fecha_devolucion = "" 
    
    def recuperar_historial(self): return self.libro + "," + self.usuario + "," + self.fecha_prestamo + "," + self.fecha_devolucion + "," 

class SistemaBiblioteca: 
    def __init__(self): 
        self.libros = [] 
        self.usuarios = [] 
        self.prestamos = [] 
    
    def recuperar_info_general(self): return ",".join([str(libro) for libro in self.libros]) + "," + ",".join([str(usuario) for usuario in self.usuarios]) + "," + ",".join([str(prestamo) for prestamo in self.prestamos]) + ","

