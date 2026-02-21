Aquí tienes el README ajustado según tus indicaciones:

---

# 📄 XONISPAM

**Advertencia:** Este código tiene únicamente fines educativos. No debe usarse para actividades malintencionadas ni para molestar a otras personas. El autor no se hace responsable del uso indebido.

## 🎯 ¿Qué es XONISPAM?

XONISPAM es un script Python simple que automatiza la escritura y envío de texto usando la biblioteca `pyautogui`. Permite:

- Enviar un mismo mensaje N veces (spam normal).
- Enviar palabra por palabra el contenido de un archivo `.txt`.

El script simula pulsaciones de teclado en la máquina donde se ejecuta, por lo que el foco debe estar en la aplicación destino (chat, editor, etc.).

## ✅ Requisitos

- Python 3.8+ instalado.
- Dependencias Python listadas en `requirements.txt`.
- Entorno con servidor gráfico (Xorg) o soporte para generar eventos de teclado desde Python. En Wayland o entornos restringidos puede no funcionar.

### Dependencias del sistema por plataforma:

#### 🐧 Arch Linux
```bash
sudo pacman -S python-pip
sudo pacman -S tk
sudo pacman -S scrot xorg-xinput xdotool
pip install pyautogui --break-system-packages
```

#### 🐧 Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip -y
sudo apt install python3-tk python3-dev scrot xdotool python3-xlib -y
pip3 install pyautogui --break-system-packages
```

#### 🪟 Windows
- Instala Python 3 desde [python.org](https://python.org)
```bash
pip install pyautogui
```

**Notas:**
- `scrot` y `xdotool` ayudan en Linux para ciertas funciones de automatización.
- En algunas distribuciones con Wayland puede ser necesario cambiar a Xorg o permitir control de entrada.

## ⚙️ Uso

1. Asegúrate de que la ventana objetivo (chat, editor, etc.) tenga el foco y el cursor en el campo donde quieres escribir.
2. Ejecuta el script:

```bash
python start.py
```

3. Elige una de las opciones del menú:

- **SPAM normal [0]**: te pedirá el mensaje y la cantidad.
- **SPAM de texto [1]**: te pedirá la ruta a un archivo `.txt` y enviará palabra por palabra.
- **SALIR [2]**: salir del programa.

4. Tras elegir, el script espera **3 segundos** antes de empezar para que tengas tiempo de colocar el foco en la ventana destino.

## ✋ Pausar / Detener

- Para detener el script en ejecución en la terminal: `Ctrl + C`
- Si el script está enviando teclas y necesitas recuperar el control, intenta cambiar a otra ventana o presionar la combinación de seguridad del sistema (ej. `Ctrl+Alt+F1` en Linux para cambiar de consola).

## 🔒 Consideraciones de seguridad y ética

- No uses este script para enviar mensajes no solicitados, acosar o causar daños.
- No lo ejecutes en sistemas de terceros sin permiso.
- Evita usarlo en sistemas donde `pyautogui` pueda interactuar con privilegios elevados o alterar la configuración del sistema.

## 🐛 Problemas comunes

- **"Las teclas no se envían"**: revisa que la ventana de destino tenga el foco y que el servidor gráfico permita inyección de eventos.
- **"Funcionó solo parcialmente"**: puede haber diferencias entre entornos (Wayland vs Xorg). Prueba en Xorg si es posible.
- **"Permisos"**: en algunos entornos de escritorio hay que habilitar control por aplicaciones.

## 📦 Archivos incluidos

- `start.py` — script principal de XONISPAM.
- `requirements.txt` — dependencias Python.

## ✉️ Contacto y Créditos

- **Proyecto:** XONIDU
- **Contacto:** xonidu@gmail.com  
- **#Somos XONINDU**
- **Creador: Darian Alberto Camacho Salas
