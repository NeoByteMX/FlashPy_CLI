import json
import os

class Flashcard:
    """Clase que representa una única tarjeta de estudio."""
    
    def __init__(self, anverso: str, reverso: str):
        self.anverso = anverso
        self.reverso = reverso

    def to_dict(self) -> dict:
        """Convierte la flashcard a un diccionario para facilitar su serialización a JSON."""
        return {
            "anverso": self.anverso,
            "reverso": self.reverso
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Flashcard':
        """Crea una instancia de Flashcard a partir de un diccionario."""
        return cls(data.get("anverso", ""), data.get("reverso", ""))


class GestorFlashcards:
    """Clase que gestiona la colección de flashcards y la persistencia en JSON."""
    
    def __init__(self, archivo_json: str = "mis_flashcards.json"):
        self.archivo_json = archivo_json
        self.flashcards = []
        self.cargar_datos()

    def cargar_datos(self):
        """Carga las flashcards desde el archivo JSON si existe."""
        if os.path.exists(self.archivo_json):
            try:
                with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                    self.flashcards = [Flashcard.from_dict(item) for item in datos]
            except json.JSONDecodeError:
                print("\n[!] Advertencia: El archivo JSON estaba vacío o corrupto. Se iniciará una lista nueva.")
                self.flashcards = []
        else:
            # Si no existe, simplemente inicializamos la lista vacía
            self.flashcards = []

    def guardar_datos(self):
        """Guarda la lista actual de flashcards en el archivo JSON."""
        with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
            datos = [flashcard.to_dict() for flashcard in self.flashcards]
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def agregar_flashcard(self, anverso: str, reverso: str):
        """Agrega una nueva flashcard y actualiza el archivo JSON."""
        nueva_flashcard = Flashcard(anverso, reverso)
        self.flashcards.append(nueva_flashcard)
        self.guardar_datos()

    def obtener_flashcards(self) -> list:
        """Devuelve la lista actual de flashcards."""
        return self.flashcards


class AppConsola:
    """Clase que maneja la interfaz de usuario en la consola."""
    
    def __init__(self):
        self.gestor = GestorFlashcards()

    def mostrar_menu(self):
        print("\n" + "="*35)
        print("📚 APLICACIÓN DE FLASHCARDS 📚")
        print("="*35)
        print("1. Agregar nueva Flashcard")
        print("2. Ver todas las Flashcards")
        print("3. Modo Estudio")
        print("4. Salir")
        print("="*35)

    def ejecutar(self):
        """Bucle principal de la aplicación."""
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-4): ").strip()

            if opcion == '1':
                self.menu_agregar()
            elif opcion == '2':
                self.menu_listar()
            elif opcion == '3':
                self.menu_estudiar()
            elif opcion == '4':
                print("\n¡Gracias por estudiar! Guardando y cerrando programa... 👋")
                break
            else:
                print("\n[!] Opción no válida. Por favor, intenta de nuevo.")

    def menu_agregar(self):
        print("\n--- Agregar Flashcard ---")
        anverso = input("Escribe el concepto (Anverso): ").strip()
        reverso = input("Escribe la definición (Reverso): ").strip()
        
        if anverso and reverso:
            self.gestor.agregar_flashcard(anverso, reverso)
            print("✅ ¡Flashcard agregada y guardada con éxito!")
        else:
            print("❌ Error: El anverso y el reverso no pueden estar vacíos.")

    def menu_listar(self):
        flashcards = self.gestor.obtener_flashcards()
        print("\n--- Tus Flashcards ---")
        if not flashcards:
            print("No tienes flashcards guardadas aún.")
            return
        
        for i, fc in enumerate(flashcards, 1):
            print(f"{i}. Anverso: {fc.anverso} | Reverso: {fc.reverso}")

    def menu_estudiar(self):
        flashcards = self.gestor.obtener_flashcards()
        if not flashcards:
            print("\n[!] Necesitas agregar flashcards antes de poder estudiar.")
            return

        print("\n--- Modo Estudio ---")
        print("Presiona Enter para ver la respuesta, o escribe 'salir' para terminar el repaso.")
        
        for i, fc in enumerate(flashcards, 1):
            print(f"\nTarjeta {i}/{len(flashcards)}")
            print(f"❓ Pregunta (Anverso): {fc.anverso}")
            
            accion = input("👉 Presiona Enter para ver la respuesta... ").strip().lower()
            if accion == 'salir':
                print("Saliendo del modo estudio...")
                break
            
            print(f"💡 Respuesta (Reverso): {fc.reverso}")
            print("-" * 20)
            
        print("\n¡Repaso finalizado!")

if __name__ == "__main__":
    # Inicializar y ejecutar la aplicación
    app = AppConsola()
    app.ejecutar()