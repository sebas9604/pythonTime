import pygame
from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent, GiftEvent, ShareEvent, JoinEvent, ConnectEvent             
import pydirectinput
import pyttsx3

import threading
import queue
import time
# =========================
# CONFIGURACIÓN
# =========================
TIKTOK_USER = "sebas.linarest"   # Sin @
SONIDO_PATH = "C:/Users/USUARIO/OneDrive/Videos/boom.mp3"    # Archivo de sonido (MP3 o WAV)
SONIDO_PATH_1 = "C:/Users/USUARIO/OneDrive/Videos/cowbell.mp3"    # Archivo de sonido (MP3 o WAV)
SONIDO_PATH_2 = "C:/Users/USUARIO/OneDrive/Videos/phone.mp3"    # Archivo de sonido (MP3 o WAV)
SONIDO_PATH_3 = "C:/Users/USUARIO/OneDrive/Videos/gun.mp3"    # Archivo de sonido (MP3 o WAV)
# =========================

# Inicializar pygame mixer para reproducir audio
pygame.mixer.init()
engine = pyttsx3.init()


# Cargar el sonido
sonido = pygame.mixer.Sound(SONIDO_PATH)
sonido_1 = pygame.mixer.Sound(SONIDO_PATH_1)
sonido_2 = pygame.mixer.Sound(SONIDO_PATH_2)
sonido_3 = pygame.mixer.Sound(SONIDO_PATH_3)


# Cliente TikTok
client = TikTokLiveClient(unique_id=TIKTOK_USER)

# Evento cuando alguien da like
@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    print("Like")
    pydirectinput.press('TAB')  # cambiar arma
    sonido_3.play()
    pygame.time.delay(int(sonido_3.get_length() * 1000))

@client.on(ShareEvent)
async def on_share(event: ShareEvent):
    print("-----------------------------SHARE")
    pydirectinput.press('v')  # Super
    sonido_1.play()
    pygame.time.delay(int(sonido_1.get_length() * 1000))
# =========================
# EVENTO: Regalo
# =========================
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    gift_name = event.gift.name
    print(f"Regalo recibido: {gift_name} por {event.user.nickname}")

    # Ejemplos de acciones según el regalo
    if gift_name.lower() == "rose":
        print("ROSEROSEROSEROSEROSE")
        pydirectinput.press('z')  # Salto
        pydirectinput.press('shift')  # Dash
    elif gift_name.lower() == "balloons":
        print("Balloooooooooooooooooooooooooooooooooooooooooooons")
        sonido.play()
        pygame.time.delay(int(sonido.get_length() * 1000))
    else:
        print("Regalo no reconocido, acción por defecto")
        pydirectinput.press('enter')  # Acción por defecto
"""""
# Cuando se conecta al live
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print("Conectado al live de", USERNAME)
    voz_cola.put("Conectado al live de " + USERNAME)

# Cuando alguien entra al live
@client.on(JoinEvent)
async def on_join(event: JoinEvent):
    mensaje = f"{event.user.uniqueId} ha entrado al live."
    print(mensaje)
    voz_cola.put(mensaje)
"""
# Ejecutar
if __name__ == "__main__":
    sonido.play()
    print(f"[INFO] Escuchando likes en @{TIKTOK_USER}...")
    client.run()
