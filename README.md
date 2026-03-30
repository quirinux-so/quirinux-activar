# Activador de Licencia Quirinux SSD

Sistema de activación de licencias de soporte para instalaciones OEM de Quirinux en discos SSD USB o equipos preinstalados.

Utilidad implementa una interfaz gráfica en Python que solicita al usuario un número de serie (S/N) para validar la licencia y desbloquear el sistema.

## Características

* Interfaz gráfica en pantalla completa usando tkinter
* Soporte multilenguaje automático basado en configuración del sistema
* Validación de licencia mediante código dividido en segmentos
* Persistencia de activación en archivo local
* Bloqueo de uso hasta activación correcta
* Ventana forzada en primer plano (modo kiosk)
* Compatible con sistemas Linux (especialmente Debian/derivados)

## Idiomas soportados

El sistema detecta automáticamente el idioma del entorno y selecciona la traducción correspondiente.

Idiomas disponibles:

* Español (es)
* Gallego (gl)
* Alemán (de)
* Portugués (pt)
* Italiano (it)
* Ruso (ru)
* Húngaro (hu)
* Francés (fr)
* Inglés (en)

Si el idioma no está soportado, se utiliza inglés por defecto.

## Funcionamiento

1. Al iniciar el sistema, el script verifica si existe el archivo de activación:

   /opt/activar/codigo.txt

2. Si no existe:

   * Se lanza una interfaz gráfica en pantalla completa
   * El usuario debe ingresar el número de serie dividido en 4 campos

3. Si el código es correcto:

   * Se guarda la licencia en el sistema
   * Se muestra mensaje de éxito
   * La aplicación se cierra

4. Si el código es incorrecto:

   * Se muestra un mensaje de error
   * El usuario debe reintentar

5. En ejecuciones posteriores:

   * Si el archivo existe, el sistema no vuelve a mostrar la ventana

## Estructura del código

### Componentes principales

* detectar_idioma()

  * Detecta el idioma del sistema usando variables de entorno (LANG, LC_ALL, etc.)

* verificar_licencia()

  * Compara el código ingresado con el código predefinido
  * Guarda el resultado si es válido

* comprobar_activar()

  * Verifica si el sistema ya fue activado

* forzar_ventana_al_frente()

  * Mantiene la ventana siempre visible (topmost)

* Interfaz gráfica

  * Construida con tkinter
  * Incluye validación de longitud y navegación automática entre campos

## Configuración

Antes de entregar el disco ssd externo o el equipo con Quirinux preinstalado es necesario modificar los siguientes valores:
```
CODIGO_LICENCIA = ["QSSD", "2024", "08", "001"]
NOMBRE_CLIENTE = "Nombre Apellido"
RUTA_ARCHIVO_CODIGO = "/opt/activar/codigo.txt"
RUTA_LOGOTIPO = "/opt/activar/quirinux_logo.png"
```
## Requisitos

* Python 3.x
* Entorno gráfico compatible con Tkinter
* Sistema Linux (probado en Debian/Quirinux)

## Instalación

1. Copiar el script en:

   /opt/activar/activar.py

2. Asegurar permisos de ejecución:

   chmod +x activar.py

3. Ejecutar al inicio del sistema (por ejemplo, usando systemd, rc.local o autostart del entorno gráfico)

## Seguridad

* El código de licencia está embebido en el script
* No existe cifrado ni verificación remota
* Sistema diseñado para control OEM, no como mecanismo antifraude robusto

## Limitaciones

* No hay validación contra servidor externo
* Fácilmente modificable si se accede al código fuente
* Depende de entorno gráfico
* No maneja múltiples usuarios o sesiones

## Licencia

Este proyecto está licenciado bajo GPL v2:

https://www.gnu.org/licenses/gpl-2.0.txt
