# 📄 XONISPAM

**Advertencia:** Este código tiene únicamente fines educativos. No debe usarse para actividades malintencionadas ni para molestar a otras personas. El autor no se hace responsable del uso indebido.

## 🎯 ¿Qué es XONISPAM?

XONISPAM es una herramienta Python que automatiza la escritura y envío de texto usando la biblioteca `pyautogui`. Consta de dos componentes:

- **`start.py`** - Lanzador universal que verifica dependencias y ejecuta el programa principal
- **`xonispam.py`** - Programa principal con la funcionalidad de spam

Permite:
- Enviar un mismo mensaje N veces (spam normal)
- Enviar palabra por palabra el contenido de un archivo `.txt`

El script simula pulsaciones de teclado en la máquina donde se ejecuta, por lo que el foco debe estar en la aplicación destino (chat, editor, etc.).

## 📥 Instalación

### 🐧 Arch Linux (AUR - Recomendado)

```bash
# Instalar desde AUR con yay
yay -S xonispam

# Ejecutar
xonispam
```

### 📦 Desde GitHub (desarrollo)

```bash
# Clonar el repositorio
git clone https://github.com/XONIDU/xonispam.git
cd xonispam

# Ejecutar
python start.py
```

## ✅ Requisitos

- Python 3.8+ instalado
- Dependencias Python: `pyautogui`
- Entorno con servidor gráfico (Xorg) o soporte para generar eventos de teclado desde Python

### Dependencias del sistema por plataforma:

#### 🐧 Arch Linux
```bash
# Instalar dependencias del sistema
sudo pacman -S python-pip tk scrot xorg-xinput xdotool

# Instalar dependencias Python (si no usas AUR)
pip install -r requisitos.txt --break-system-packages
```

#### 🐧 Ubuntu / Debian
```bash
# Actualizar repositorios
sudo apt update

# Instalar dependencias del sistema
sudo apt install python3 python3-pip -y
sudo apt install python3-tk python3-dev scrot xdotool python3-xlib -y

# Instalar dependencias Python
pip3 install -r requisitos.txt --break-system-packages
```

#### 🪟 Windows
1. Instala Python 3 desde [python.org](https://python.org)
2. Abre una terminal (cmd o PowerShell) y ejecuta:
```bash
pip install -r requisitos.txt
```

#### 🪟 Windows - Ejecutar como Administrador

Para ejecutar XONISPAM con permisos de administrador en Windows, usa el archivo `XONISPAM_ADMIN.bat`:

```batch
@echo off
title XONISPAM 2026 - Administrador
color 1F

:: Solicitar permisos de administrador
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando permisos de administrador...
    echo.
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)

:: Ejecutar start.py con permisos de administrador
cls
echo ============================================================
echo              XONISPAM 2026 - Automatizacion de Teclado
echo              (Modo Administrador)
echo ============================================================
echo.
echo [OK] Permisos de administrador obtenidos
echo.
echo Iniciando XONISPAM...
echo.

python start.py
pause
```

**Guardar como:** `XONISPAM_ADMIN.bat` (en la misma carpeta que `start.py`)

**Uso:** Haz doble clic en `XONISPAM_ADMIN.bat` y acepta los permisos de administrador.

**Notas:**
- `scrot` y `xdotool` ayudan en Linux para ciertas funciones de automatización
- En algunas distribuciones con Wayland puede ser necesario cambiar a Xorg o permitir control de entrada
- El lanzador (`start.py`) instala automáticamente las dependencias faltantes

## ⚙️ Uso

### Desde AUR (instalado con yay)
```bash
# Simplemente ejecuta
xonispam
```

### Desde GitHub (modo desarrollo)
```bash
# Ejecutar el lanzador
python start.py
```

### Menú principal

```
MENU PRINCIPAL:

  [0] SPAM normal - Envia un mismo mensaje N veces
  [1] SPAM de texto - Envia palabra por palabra desde archivo .txt
  [2] SALIR
```

**Importante:** Tras elegir una opción, el script espera **3 segundos** para que tengas tiempo de colocar el foco en la ventana destino.

## 🚀 Características del Lanzador

El `start.py` incluye:

- ✅ **Verificación automática de Python y pip**
- ✅ **Instalación automática de dependencias** (pyautogui)
- ✅ **Soporte `--break-system-packages` para Arch/Fedora**
- ✅ **Instalación automática de dependencias del sistema** (scrot, xdotool en Linux)
- ✅ **Búsqueda de `xonispam.py` en múltiples ubicaciones:**
  - Mismo directorio (desarrollo local)
  - `/usr/share/xonispam/` (instalación AUR)
  - `~/.xonispam/` (usuario)
- ✅ **Accesos directos automáticos** (.bat para Windows, .sh para Linux)

## ✋ Pausar / Detener

- Para detener el script en ejecución: `Ctrl + C`
- Si el script está enviando teclas y necesitas recuperar el control, cambia a otra ventana o presiona `Ctrl+Alt+F1` (Linux) para cambiar de consola.
- **En Windows:** Mueve el mouse a la esquina superior izquierda para activar el FailSafe de pyautogui

## 🔒 Consideraciones de seguridad y ética

- No uses este script para enviar mensajes no solicitados, acosar o causar daños
- No lo ejecutes en sistemas de terceros sin permiso
- Evita usarlo en sistemas donde `pyautogui` pueda interactuar con privilegios elevados
- **Este programa es SOLO para fines educativos**

## 🐛 Problemas comunes

| Problema | Solución |
|----------|----------|
| "Las teclas no se envían" | Verifica que la ventana destino tenga el foco y que el servidor gráfico permita inyección de eventos |
| "Funcionó solo parcialmente" | Puede haber diferencias entre Wayland y Xorg. Prueba en Xorg |
| "scrot/xdotool no encontrado" | El lanzador pregunta si instalar estas dependencias automáticamente |
| "Error: No se encuentra xonispam.py" | Asegúrate de que `xonispam.py` está en el mismo directorio que `start.py` o instaló correctamente desde AUR |
| "Hook declined" en AUR | El archivo `.SRCINFO` es requerido - el PKGBUILD actualizado ya lo incluye |
| "Permiso denegado en Windows" | Usa `XONISPAM_ADMIN.bat` para ejecutar como administrador |

## 📦 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `start.py` | Lanzador universal (verifica dependencias y ejecuta el programa) |
| `xonispam.py` | Programa principal con la funcionalidad de spam |
| `requisitos.txt` | Dependencias Python (`pyautogui`) |
| `PKGBUILD` | Para instalar desde AUR |
| `XONISPAM_ADMIN.bat` | Lanzador para Windows con permisos de administrador |
| `README.md` | Este archivo de documentación |

## 📊 Estadísticas del proyecto

- **Estrellas:** 0
- **Observadores:** 1
- **Forks:** 0
- **Lenguaje principal:** Python 96.0%
- **Shell:** 4.0%

## 📝 Versiones

### v1.0.0 (2026)
- Lanzamiento inicial
- Soporte multiplataforma (Windows, Linux, MacOS)
- Dos modos de spam: mensaje repetido y archivo de texto
- Instalación automática de dependencias
- Accesos directos para cada sistema operativo
- Publicado en AUR: `yay -S xonispam`
- Script `.bat` para Windows con permisos de administrador

## 🔗 Enlaces

- **GitHub:** https://github.com/XONIDU/xonispam
- **AUR:** https://aur.archlinux.org/packages/xonispam

## ✉️ Contacto y Créditos

- **Proyecto:** XONISPAM
- **Contacto:** xonidu@gmail.com
- **Creador:** Darian Alberto Camacho Salas
- **Organización:** XONIDU
- **#Somos XONINDU**

---

