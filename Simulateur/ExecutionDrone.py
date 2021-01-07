import asyncio
import os
import time

from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
from Classes.AvanceeMission import *



avancee = AvanceeMission(0, 0, 0, 0, 0)  # Création de l'instance avancee

async def run(balises):
    # Connexion au drone
    drone = System()
    await drone.connect(system_address="udp://:14540")
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # Suivie de vol
    return_mission_progress_task = asyncio.create_task(return_mission_progress(drone))
    return_vitesse_task = asyncio.create_task(return_vitesse(drone))
    return_battery_task = asyncio.create_task(return_battery(drone))
    return_position_task = asyncio.create_task(return_position(drone))
    running_tasks = [
        return_mission_progress_task,
        return_vitesse_task,
        return_battery_task,
        return_position_task,
    ]
    termination_task = asyncio.ensure_future(observe_is_in_air(drone, running_tasks))

    # Caractéristiques Mission
    mission_items = []
    for x in balises:
        balise = balises[x]
        if float(balise.__dict__["photo"]) == 0:
            mode = MissionItem.CameraAction.NONE
        else:
            mode = MissionItem.CameraAction.TAKE_PHOTO
        mission_items.append(
            MissionItem(
                float(balise.__dict__["latitude"]),
                float(balise.__dict__["longitude"]),
                float(balise.__dict__["altitude"]),
                float(balise.__dict__["vitesse"]),
                True,
                float("nan"),
                float("nan"),
                mode,
                float("nan"),
                float("nan"),
            )
        )
    mission_plan = MissionPlan(mission_items)

    # Réglage fin de mission
    await drone.mission.set_return_to_launch_after_mission(True)

    # Chargement de la mission dans le plan de vol
    print("-- Uploading mission")
    await drone.mission.upload_mission(mission_plan)

    # Armement des moteurs
    print("-- Arming")
    await drone.action.arm()

    # Lancement de la mission - Décollage
    print("-- Starting mission")
    await drone.mission.start_mission()

    # Fin de mission - Atterissage
    await termination_task


# Etapes Mission
async def return_mission_progress(drone):
    async for mission_progress in drone.mission.mission_progress():
        return (
            f"Mission progress: "
            f"{mission_progress.current}/"
            f"{mission_progress.total}"
        )


# Charge Batterie
async def return_battery(drone):
    async for battery in drone.telemetry.battery():
        avancee.setBatterie(battery.remaining_percent)  # Batterie


# Coordonnées GPS et Altitude
async def return_position(drone):
    async for position in drone.telemetry.position():
        avancee.setLatitude(position.latitude_deg)  # Latitude
        avancee.setLongitude(position.longitude_deg)  # Longitude
        avancee.setAltitude(position.relative_altitude_m)  # Altitude


# Vitesse
async def return_vitesse(drone):
    async for vitesse in drone.telemetry.fixedwing_metrics():
        avancee.setVitesse(vitesse.airspeed_m_s)  # Vitesse
        print(avancee.__dict__)


# Fonction arrêt de la mission
async def observe_is_in_air(drone, running_tasks):
    """ Monitors whether the drone is flying or not and
    returns after landing """

    was_in_air = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            was_in_air = is_in_air

        if was_in_air and not is_in_air:
            for task in running_tasks:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            await asyncio.get_event_loop().shutdown_asyncgens()

            return


def ExecutionDrone(balises):
    # Lancement de l'interface graphique JVAMSim
    os.system(
        "chmod +x Simulateur/JMAVSim.sh\nopen Simulateur/JMAVSim.sh"
    )  
    # Exécution du shell JMAVSim.sh
    time.sleep(60)  # Attente de l'ouverture de l'interface
    # Lancement de la mission
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(balises))  # Lancement du thread