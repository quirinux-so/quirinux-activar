#!/usr/bin/env python3

# ======================================================================
# Archivo:       activar.py
# Ruta:          /opt/activar/
# Autor:         Charlie Martínez® <cmartinez@quirinux.org>
# Licencia:      https://www.gnu.org/licenses/gpl-2.0.txt
# Propósito:     Sistema de registro para Quirinux SSD
# Distribución:  Quirinux 2.x
# ======================================================================

#
# Copyright (c) 2019-2025 Charlie Martínez, derechos reservados.
# Licencia: https://www.gnu.org/licenses/gpl-2.0.txt
# Usos autorizados y no autorizados de la marca Quirinux:
# Ver https://www.quirinux.org/aviso-legal
#

# ----------------------------------------------------------------------
# Sistema de registro para soporte técnico de instalaciones OEM
# y discos externos SSD USB con Quirinux preinstalado.
# ----------------------------------------------------------------------

import os
import locale
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# ----------------------------------------------------------------------
# Idiomas
# ----------------------------------------------------------------------

TRADUCCIONES = {
    "es": {
        "titulo":           "Activación de Licencia",
        "bienvenida":       (
            "Te damos la bienvenida a tu sistema Quirinux Preinstalado.\n"
            "Vamos a activar tu licencia, luego ya no volverás a ver este mensaje.\n"
            "Encuentra el número de serie en la etiqueta de tu equipo o de tu disco SSD."
        ),
        "ingresar_sn":      "Ingresa tu S/N:",
        "boton_activar":    "Activar",
        "titulo_exito":     "Activación exitosa",
        "msg_exito":        "Copia activada a nombre de:\n{nombre}",
        "titulo_error":     "Error de activación",
        "msg_error":        "Código de licencia incorrecto. Intenta otra vez.",
    },
    "gl": {
        "titulo":           "Activación de Licenza",
        "bienvenida":       (
            "Dámosche a benvida ao teu sistema Quirinux Preinstalado.\n"
            "Imos activar a túa licenza, logo xa non volverás ver esta mensaxe.\n"
            "Atopa o número de serie na etiqueta do teu equipo ou do teu disco SSD."
        ),
        "ingresar_sn":      "Introduce o teu N/S:",
        "boton_activar":    "Activar",
        "titulo_exito":     "Activación exitosa",
        "msg_exito":        "Copia activada a nome de:\n{nombre}",
        "titulo_error":     "Erro de activación",
        "msg_error":        "Código de licenza incorrecto. Téntao outra vez.",
    },
    "de": {
        "titulo":           "Lizenzaktivierung",
        "bienvenida":       (
            "Willkommen bei Ihrem vorinstallierten Quirinux-System.\n"
            "Wir aktivieren jetzt Ihre Lizenz – danach wird diese Meldung nicht mehr angezeigt.\n"
            "Die Seriennummer finden Sie auf dem Aufkleber Ihres Geräts oder Ihrer SSD."
        ),
        "ingresar_sn":      "Seriennummer eingeben:",
        "boton_activar":    "Aktivieren",
        "titulo_exito":     "Aktivierung erfolgreich",
        "msg_exito":        "Kopie aktiviert auf den Namen:\n{nombre}",
        "titulo_error":     "Aktivierungsfehler",
        "msg_error":        "Falscher Lizenzcode. Bitte versuchen Sie es erneut.",
    },
    "pt": {
        "titulo":           "Ativação de Licença",
        "bienvenida":       (
            "Bem-vindo ao seu sistema Quirinux Pré-instalado.\n"
            "Vamos ativar a sua licença; depois disso, esta mensagem não aparecerá novamente.\n"
            "Encontre o número de série na etiqueta do seu equipamento ou do seu disco SSD."
        ),
        "ingresar_sn":      "Insira o seu N/S:",
        "boton_activar":    "Ativar",
        "titulo_exito":     "Ativação bem-sucedida",
        "msg_exito":        "Cópia ativada em nome de:\n{nombre}",
        "titulo_error":     "Erro de ativação",
        "msg_error":        "Código de licença incorreto. Tente novamente.",
    },
    "it": {
        "titulo":           "Attivazione Licenza",
        "bienvenida":       (
            "Benvenuto nel tuo sistema Quirinux Preinstallato.\n"
            "Attiveremo la tua licenza; dopo di ciò non vedrai più questo messaggio.\n"
            "Trova il numero di serie sull'etichetta del tuo dispositivo o del tuo disco SSD."
        ),
        "ingresar_sn":      "Inserisci il tuo N/S:",
        "boton_activar":    "Attiva",
        "titulo_exito":     "Attivazione riuscita",
        "msg_exito":        "Copia attivata a nome di:\n{nombre}",
        "titulo_error":     "Errore di attivazione",
        "msg_error":        "Codice di licenza errato. Riprova.",
    },
    "ru": {
        "titulo":           "Активация лицензии",
        "bienvenida":       (
            "Добро пожаловать в вашу предустановленную систему Quirinux.\n"
            "Сейчас мы активируем вашу лицензию — после этого сообщение больше не появится.\n"
            "Серийный номер находится на наклейке вашего устройства или SSD-диска."
        ),
        "ingresar_sn":      "Введите серийный номер:",
        "boton_activar":    "Активировать",
        "titulo_exito":     "Активация выполнена",
        "msg_exito":        "Копия активирована на имя:\n{nombre}",
        "titulo_error":     "Ошибка активации",
        "msg_error":        "Неверный код лицензии. Попробуйте ещё раз.",
    },
    "hu": {
        "titulo":           "Licenc aktiválása",
        "bienvenida":       (
            "Üdvözöljük az előre telepített Quirinux rendszerben.\n"
            "Most aktiváljuk a licencét – ezt követően ez az üzenet többé nem jelenik meg.\n"
            "A sorozatszámot az eszköz vagy az SSD-lemez címkéjén találja."
        ),
        "ingresar_sn":      "Adja meg a sorozatszámot:",
        "boton_activar":    "Aktiválás",
        "titulo_exito":     "Sikeres aktiválás",
        "msg_exito":        "A példány aktiválva a következő névre:\n{nombre}",
        "titulo_error":     "Aktiválási hiba",
        "msg_error":        "Helytelen licenckód. Kérjük, próbálja újra.",
    },
    "fr": {
        "titulo":           "Activation de la licence",
        "bienvenida":       (
            "Bienvenue dans votre système Quirinux préinstallé.\n"
            "Nous allons activer votre licence ; ce message ne s'affichera plus ensuite.\n"
            "Vous trouverez le numéro de série sur l'étiquette de votre appareil ou de votre disque SSD."
        ),
        "ingresar_sn":      "Entrez votre N/S :",
        "boton_activar":    "Activer",
        "titulo_exito":     "Activation réussie",
        "msg_exito":        "Copie activée au nom de :\n{nombre}",
        "titulo_error":     "Erreur d'activation",
        "msg_error":        "Code de licence incorrect. Veuillez réessayer.",
    },
    "en": {
        "titulo":           "License Activation",
        "bienvenida":       (
            "Welcome to your pre-installed Quirinux system.\n"
            "We will now activate your license — after this, you will not see this message again.\n"
            "Find the serial number on the label of your device or SSD drive."
        ),
        "ingresar_sn":      "Enter your S/N:",
        "boton_activar":    "Activate",
        "titulo_exito":     "Activation successful",
        "msg_exito":        "Copy activated in the name of:\n{nombre}",
        "titulo_error":     "Activation error",
        "msg_error":        "Incorrect license code. Please try again.",
    },
}

# Idiomas oficiales soportados (código ISO 639-1)
IDIOMAS_OFICIALES = {"es", "gl", "de", "pt", "it", "ru", "hu", "fr", "en"}


def detectar_idioma():
    """
    Detecta el idioma del sistema leyendo las variables de entorno estándar
    de locales en Linux/Debian: LANG, LANGUAGE, LC_ALL, LC_MESSAGES.
    Devuelve el código de dos letras ISO 639-1 si está entre los idiomas
    oficiales; de lo contrario devuelve 'en' (inglés) como fallback.
    """
    for variable in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        valor = os.environ.get(variable, "")
        if valor:
            # LANGUAGE puede contener lista separada por ":" → tomar el primero
            codigo = valor.split(":")[0]
            # Normalizar: extraer solo los dos primeros caracteres (ej: "es_ES.UTF-8" → "es")
            codigo = codigo.split("_")[0].split(".")[0].lower()
            if codigo in IDIOMAS_OFICIALES:
                return codigo

    # Fallback a locale del sistema vía biblioteca estándar
    try:
        lang, _ = locale.getlocale()
        if lang:
            codigo = lang.split("_")[0].lower()
            if codigo in IDIOMAS_OFICIALES:
                return codigo
    except Exception:
        pass

    return "en"


# Seleccionar traducciones activas
IDIOMA = detectar_idioma()
T = TRADUCCIONES[IDIOMA]

# ----------------------------------------------------------------------
# Datos de la licencia
# ----------------------------------------------------------------------
# Estos datos son intransferibles y se registran al momento de grabar
# el disco SSD que se le entrega al comprador.
# Sirven para identificar la copia exacta recibida
# y brindar el soporte técnico contratado. 
# ----------------------------------------------------------------------

CODIGO_LICENCIA = ["QSSD", "2024", "08", "001"]  # Modificar según registro
NOMBRE_CLIENTE = "Nombre Apellido"                # Modificar según registro
RUTA_ARCHIVO_CODIGO = "/opt/activar/codigo.txt"
RUTA_LOGOTIPO = "/opt/activar/quirinux_logo.png"

# ID del temporizador after()
after_id = None


# ----------------------------------------------------------------------
# Lógica de activación
# ----------------------------------------------------------------------

def verificar_licencia():
    global after_id

    licencia_ingresada = [
        campo_qssd.get().upper(),
        campo_2024.get(),
        campo_08.get(),
        campo_001.get()
    ]

    if licencia_ingresada == CODIGO_LICENCIA:

        # Detener el loop infinito de "always on top"
        if after_id is not None:
            try:
                ventana.after_cancel(after_id)
            except Exception:
                pass

        # Guardar licencia
        os.makedirs(os.path.dirname(RUTA_ARCHIVO_CODIGO), exist_ok=True)
        with open(RUTA_ARCHIVO_CODIGO, "w") as archivo:
            archivo.write("-".join(licencia_ingresada))

        # Mensaje de éxito
        messagebox.showinfo(
            T["titulo_exito"],
            T["msg_exito"].format(nombre=NOMBRE_CLIENTE)
        )

        ventana.destroy()

    else:
        messagebox.showerror(
            T["titulo_error"],
            T["msg_error"]
        )


def comprobar_activar():
    return os.path.exists(RUTA_ARCHIVO_CODIGO)


def limitar_caracteres(event, max_length):
    if len(event.widget.get()) > max_length:
        event.widget.delete(max_length, tk.END)


def mover_siguiente(event, siguiente_campo, max_length):
    limitar_caracteres(event, max_length)
    if len(event.widget.get()) >= max_length:
        siguiente_campo.focus_set()


def forzar_ventana_al_frente():
    global after_id
    ventana.lift()
    ventana.attributes("-topmost", True)
    after_id = ventana.after(500, forzar_ventana_al_frente)


# ----------------------------------------------------------------------
# Interfáz gráfica
# ----------------------------------------------------------------------

if not comprobar_activar():

    ventana = tk.Tk()
    ventana.title(T["titulo"])

    ventana.attributes("-fullscreen", True)
    ventana.attributes("-topmost", True)
    ventana.resizable(False, False)

    ventana.geometry(f"{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}+0+0")

    # Logo
    logotipo = PhotoImage(file=RUTA_LOGOTIPO)
    etiqueta_logo = tk.Label(ventana, image=logotipo)
    etiqueta_logo.pack(pady=20)

    # Mensaje de bienvenida
    etiqueta_bienvenida = tk.Label(
        ventana,
        text=T["bienvenida"],
        font=("Ubuntu", 16),
        justify="center",
        wraplength=800
    )
    etiqueta_bienvenida.pack(pady=20)

    etiqueta = tk.Label(ventana, text=T["ingresar_sn"], font=("Ubuntu", 18))
    etiqueta.pack(pady=10)

    marco_entrada = tk.Frame(ventana)
    marco_entrada.pack(pady=20)

    campo_qssd = tk.Entry(marco_entrada, font=("Ubuntu", 18), width=6, justify='center')
    campo_qssd.grid(row=0, column=0, padx=10)
    campo_qssd.bind('<KeyRelease>', lambda event: mover_siguiente(event, campo_2024, 4))

    campo_2024 = tk.Entry(marco_entrada, font=("Ubuntu", 18), width=6, justify='center')
    campo_2024.grid(row=0, column=1, padx=10)
    campo_2024.bind('<KeyRelease>', lambda event: mover_siguiente(event, campo_08, 4))

    campo_08 = tk.Entry(marco_entrada, font=("Ubuntu", 18), width=3, justify='center')
    campo_08.grid(row=0, column=2, padx=10)
    campo_08.bind('<KeyRelease>', lambda event: mover_siguiente(event, campo_001, 2))

    campo_001 = tk.Entry(marco_entrada, font=("Ubuntu", 18), width=4, justify='center')
    campo_001.grid(row=0, column=3, padx=10)
    campo_001.bind('<KeyRelease>', lambda event: limitar_caracteres(event, 3))

    boton_activar = tk.Button(
        ventana,
        text=T["boton_activar"],
        font=("Ubuntu", 16),
        command=verificar_licencia
    )
    boton_activar.pack(pady=20)

    # Iniciar loop "always on top"
    after_id = ventana.after(500, forzar_ventana_al_frente)

    # Bloquear botón cerrar
    ventana.protocol("WM_DELETE_WINDOW", lambda: None)

    ventana.mainloop()
