#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONISPAM 2026 - Lanzador Universal de Spam Automatizado
Este script ejecuta xonispam.py y verifica dependencias
Desarrollado por: Darian Alberto Camacho Salas
#Somos XONINDU
"""

import subprocess
import sys
import os
import platform
import shutil
import importlib.util

# Colores para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        """Verifica si la terminal soporta colores"""
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

# Desactivar colores si no hay soporte
if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

def get_system():
    """Detecta el sistema operativo"""
    return platform.system().lower()

def get_linux_distro():
    """Detecta la distribucion de Linux"""
    if get_system() != 'linux':
        return None
    
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content:
                    return 'ubuntu'
                elif 'debian' in content:
                    return 'debian'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content:
                    return 'centos'
                elif 'arch' in content:
                    return 'arch'
                elif 'manjaro' in content:
                    return 'manjaro'
                elif 'mint' in content:
                    return 'mint'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    """Obtiene el comando Python correcto"""
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def print_banner():
    """Muestra el banner de XONISPAM"""
    sistema = get_system()
    distro = get_linux_distro()
    
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.BLUE}{Colors.BOLD}═══════════════════════════════════════════════════════════
                    XONISPAM 2026 v1.0                    
              Herramienta de Automatización de Teclado            
              Envia mensajes repetidos o                
              contenido de archivos .txt                        
                                                          
              Sistema detectado: {sistema_texto}            
                                                          
              Desarrollado por: Darian Alberto            
              Camacho Salas                               
              #Somos XONINDU
═══════════════════════════════════════════════════════════{Colors.END}
    """
    print(banner)

def check_python():
    """Verifica Python instalado"""
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_command(comando):
    """Verifica si un comando existe"""
    return shutil.which(comando) is not None

def check_python_module(module_name):
    """Verifica si un modulo de Python esta instalado"""
    return importlib.util.find_spec(module_name) is not None

def check_dependencies():
    """Verifica las dependencias de Python necesarias"""
    print(f"\n{Colors.BOLD}Verificando dependencias de Python...{Colors.END}")
    
    dependencias = [
        ('pyautogui', 'pyautogui', 'Automatización', 'pyautogui'),
    ]
    
    faltantes = []
    
    for modulo, paquete, desc, import_name in dependencias:
        if check_python_module(import_name):
            print(f"{Colors.GREEN}  - {modulo}: OK{Colors.END}")
        else:
            print(f"{Colors.YELLOW}  - {modulo}: FALTANTE{Colors.END}")
            faltantes.append(paquete)
    
    # Verificar dependencias del sistema para pyautogui en Linux
    if get_system() == 'linux':
        system_deps = ['scrot', 'xdotool']
        for dep in system_deps:
            if check_command(dep):
                print(f"{Colors.GREEN}  - {dep} (sistema): OK{Colors.END}")
            else:
                print(f"{Colors.YELLOW}  - {dep} (sistema): FALTANTE (recomendado){Colors.END}")
                if f'sistema-{dep}' not in faltantes:
                    faltantes.append(f'sistema-{dep}')
    
    return faltantes

def install_dependencies(faltantes):
    """Instala las dependencias faltantes"""
    if not faltantes:
        return True
    
    print(f"\n{Colors.BOLD}Instalando dependencias faltantes...{Colors.END}")
    
    sistema = get_system()
    distro = get_linux_distro()
    
    # Separar paquetes Python de dependencias del sistema
    python_paquetes = [p for p in faltantes if not p.startswith('sistema-')]
    sistema_paquetes = [p.replace('sistema-', '') for p in faltantes if p.startswith('sistema-')]
    
    # Instalar paquetes Python
    if python_paquetes:
        print(f"Paquetes Python a instalar: {', '.join(python_paquetes)}")
        
        # Construir comando de instalacion
        cmd = [sys.executable, '-m', 'pip', 'install']
        
        # Agregar opciones segun sistema
        if sistema == 'linux':
            if distro in ['arch', 'manjaro', 'fedora']:
                cmd.append('--break-system-packages')
                print(f"{Colors.YELLOW}Usando --break-system-packages para {distro}{Colors.END}")
            else:
                cmd.append('--user')
        elif sistema == 'darwin':
            cmd.append('--user')
        
        cmd.extend(python_paquetes)
        
        # Intentar instalacion
        try:
            print(f"Ejecutando: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
            print(f"{Colors.GREEN}Dependencias de Python instaladas correctamente{Colors.END}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}Error instalando dependencias: {e}{Colors.END}")
            print(f"\n{Colors.YELLOW}Intentando metodo alternativo...{Colors.END}")
            
            # Segundo intento: solo --user
            try:
                cmd2 = [sys.executable, '-m', 'pip', 'install', '--user'] + python_paquetes
                subprocess.run(cmd2, check=True)
                print(f"{Colors.GREEN}Instaladas con --user{Colors.END}")
            except:
                print(f"{Colors.RED}Fallo la instalacion{Colors.END}")
                print(f"\nInstala manualmente:")
                print(f"  pip install {' '.join(python_paquetes)}")
    
    # Instalar dependencias del sistema si faltan
    if sistema_paquetes and sistema == 'linux':
        print(f"\n{Colors.YELLOW}Instalando dependencias del sistema...{Colors.END}")
        install_system_dependencies(sistema_paquetes, distro)
    
    return True

def install_system_dependencies(paquetes, distro):
    """Instala dependencias del sistema en Linux"""
    if distro in ['ubuntu', 'debian', 'mint']:
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y'] + paquetes, check=True)
            print(f"{Colors.GREEN}Dependencias del sistema instaladas{Colors.END}")
            return True
        except:
            print(f"{Colors.RED}Error instalando dependencias del sistema{Colors.END}")
            print(f"\nInstala manualmente:")
            print(f"  sudo apt install {' '.join(paquetes)}")
            return False
    
    elif distro in ['fedora']:
        try:
            subprocess.run(['sudo', 'dnf', 'install', '-y'] + paquetes, check=True)
            print(f"{Colors.GREEN}Dependencias del sistema instaladas{Colors.END}")
            return True
        except:
            print(f"{Colors.RED}Error instalando dependencias del sistema{Colors.END}")
            print(f"\nInstala manualmente:")
            print(f"  sudo dnf install {' '.join(paquetes)}")
            return False
    
    elif distro in ['arch', 'manjaro']:
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm'] + paquetes, check=True)
            print(f"{Colors.GREEN}Dependencias del sistema instaladas{Colors.END}")
            return True
        except:
            print(f"{Colors.RED}Error instalando dependencias del sistema{Colors.END}")
            print(f"\nInstala manualmente:")
            print(f"  sudo pacman -S {' '.join(paquetes)}")
            return False
    
    return False

def mostrar_ayuda():
    """Muestra ayuda de uso"""
    ayuda = f"""
{Colors.BOLD}USO DE XONISPAM:{Colors.END}

  python start.py

{Colors.BOLD}DESCRIPCION:{Colors.END}

  XONISPAM es una herramienta que automatiza el envio de mensajes
  simulando pulsaciones de teclado. Tiene dos modos de uso:

  1. SPAM NORMAL: Envia un mismo mensaje N veces
  2. SPAM DE TEXTO: Lee un archivo .txt y envia palabra por palabra

{Colors.BOLD}ADVERTENCIA:{Colors.END}

  Este programa es SOLO para fines educativos. No lo uses para:
  - Acosar o molestar a otras personas
  - Enviar mensajes no solicitados
  - Actividades malintencionadas

{Colors.BOLD}CONTROLES:{Colors.END}

  - Para detener la ejecucion: Ctrl+C
  - El programa da 3 segundos para colocar el foco en la ventana destino
    """
    print(ayuda)

def verificar_importaciones():
    """Verifica que todas las importaciones necesarias funcionen"""
    print(f"\n{Colors.BOLD}Verificando importaciones...{Colors.END}")
    
    modulos = [
        ('pyautogui', 'pyautogui'),
    ]
    
    todos_ok = True
    for modulo, nombre in modulos:
        try:
            __import__(modulo)
            print(f"{Colors.GREEN}  - {nombre}: OK{Colors.END}")
        except ImportError:
            print(f"{Colors.RED}  - {nombre}: FALLO{Colors.END}")
            todos_ok = False
    
    return todos_ok

def crear_accesos_directos():
    """Crea accesos directos para cada sistema"""
    sistema = get_system()
    
    if sistema == 'windows':
        # Crear .bat para Windows
        with open('INICIAR_XONISPAM.bat', 'w') as f:
            f.write("""@echo off
title XONISPAM 2026 - Automatizacion de Teclado
color 1F
echo ========================================
echo      XONISPAM 2026 - Automatizacion
echo      Desarrollado por Darian Alberto
echo ========================================
echo.
python start.py
pause
""")
        print(f"{Colors.GREEN}Creado INICIAR_XONISPAM.bat - Haz doble clic para ejecutar{Colors.END}")
    
    elif sistema == 'linux':
        # Crear .sh para Linux
        with open('INICIAR_XONISPAM.sh', 'w') as f:
            f.write("""#!/bin/bash
echo "========================================"
echo "      XONISPAM 2026 - Automatizacion"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
read -p "Presiona Enter para salir"
""")
        os.chmod('INICIAR_XONISPAM.sh', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONISPAM.sh - Ejecuta con: ./INICIAR_XONISPAM.sh{Colors.END}")
    
    elif sistema == 'darwin':
        # Crear .command para Mac
        with open('INICIAR_XONISPAM.command', 'w') as f:
            f.write("""#!/bin/bash
cd "$(dirname "$0")"
echo "========================================"
echo "      XONISPAM 2026 - Automatizacion"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
""")
        os.chmod('INICIAR_XONISPAM.command', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONISPAM.command - Haz doble clic para ejecutar{Colors.END}")

def main():
    """Funcion principal"""
    # Limpiar pantalla
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Mostrar banner
    print_banner()
    
    # Verificar si hay argumentos de ayuda
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}Error: Python no esta instalado{Colors.END}")
        print("Instala Python desde: https://www.python.org/downloads/")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    python_version = subprocess.run(get_python_command() + ['--version'], 
                                   capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {python_version}")
    print(f"{Colors.BOLD}Directorio:{Colors.END} {os.path.dirname(os.path.abspath(__file__))}")
    
    # Verificar dependencias
    faltantes = check_dependencies()
    
    if faltantes:
        print(f"\n{Colors.YELLOW}Faltan dependencias{Colors.END}")
        respuesta = input("Instalar automaticamente? (s/n): ")
        
        if respuesta.lower() == 's':
            install_dependencies(faltantes)
        else:
            print(f"\nPuedes instalarlas manualmente con:")
            print("  pip install pyautogui")
            if any(p.startswith('sistema-') for p in faltantes):
                print("\nY dependencias del sistema:")
                if get_system() == 'linux':
                    print("  sudo apt install scrot xdotool  # Ubuntu/Debian")
                    print("  sudo pacman -S scrot xdotool    # Arch")
                    print("  sudo dnf install scrot xdotool  # Fedora")
    
    # Verificar que existe xonispam.py
    if not os.path.exists('xonispam.py'):
        print(f"\n{Colors.RED}Error: No se encuentra xonispam.py{Colors.END}")
        print("Asegurate de que xonispam.py esta en el mismo directorio")
        print("\nPuedes descargarlo desde:")
        print("  https://github.com/XONIDU/xonispam")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    # Verificar que las importaciones funcionan
    print(f"\n{Colors.BOLD}Verificando que todo funcione...{Colors.END}")
    if not verificar_importaciones():
        print(f"\n{Colors.RED}Error: No se puede importar pyautogui{Colors.END}")
        print("El programa no puede continuar sin esta dependencia")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}Iniciando XONISPAM...{Colors.END}")
    print(f"{Colors.BOLD}Para salir en cualquier momento:{Colors.END} Ctrl+C")
    print("-" * 60)
    
    # EJECUTAR xonispam.py - ESTA ES LA PARTE IMPORTANTE
    try:
        python_cmd = get_python_command()
        cmd = python_cmd + ['xonispam.py']
        print(f"Ejecutando: {' '.join(cmd)}")
        print("-" * 60)
        
        # Ejecutar xonispam.py
        resultado = subprocess.run(cmd)
        
        if resultado.returncode != 0:
            print(f"\n{Colors.RED}Error: xonispam.py termino con codigo {resultado.returncode}{Colors.END}")
            
    except FileNotFoundError:
        print(f"\n{Colors.RED}Error: No se encuentra xonispam.py{Colors.END}")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Programa detenido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error ejecutando xonispam.py: {e}{Colors.END}")
    
    print(f"\n{Colors.BLUE}Gracias por usar XONISPAM 2026{Colors.END}")
    print(f"{Colors.BLUE}Desarrollado por Darian Alberto Camacho Salas{Colors.END}")
    print(f"{Colors.BLUE}#Somos XONINDU{Colors.END}")
    
    # Pausa al final (excepto en Windows que ya tiene pausa por el .bat)
    if get_system() != 'windows':
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        # Crear accesos directos
        crear_accesos_directos()
        
        # Ejecutar programa principal
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
