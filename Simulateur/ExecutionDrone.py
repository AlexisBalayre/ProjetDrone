import asyncio
import os
import time 

from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan


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
    print_mission_progress_task = asyncio.ensure_future(print_mission_progress(drone))
    print_battery_task = asyncio.ensure_future(print_battery(drone))
    print_position_task = asyncio.ensure_future(print_position(drone))
    print_vitesse_task = asyncio.ensure_future(print_vitesse(drone))
    running_tasks = [
        print_mission_progress_task,
        print_battery_task,
        print_position_task,
        print_vitesse_task,
    ]
    termination_task = asyncio.ensure_future(observe_is_in_air(drone, running_tasks))

    # Caractéristiques Mission
    mission_items = []
    for x in balises:
        balise = balises[x]
        if balise["photo"] == 0:
            mode = MissionItem.CameraAction.NONE
        else:
            mode = MissionItem.CameraAction.TAKE_PHOTO
        mission_items.append(
        MissionItem(
            balise['latitude'],
            balise['longitude'],
            balise['altitude'],
            balise['vitesse'],
            True,
            float("nan"),
            float("nan"),
            mode,
            balise['pause']
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


# Avancée Mission
async def print_mission_progress(drone):
    async for mission_progress in drone.mission.mission_progress():
        print(
            f"Mission progress: "
            f"{mission_progress.current}/"
            f"{mission_progress.total}"
        )


# Charge Batterie
async def print_battery(drone):
    async for battery in drone.telemetry.battery():
        print(f"Batterie : {battery.remaining_percent}")


# Coordonnées GPS et Altitude
async def print_position(drone):
    async for position in drone.telemetry.position():
        print("Latitude : ", position.latitude_deg)
        print("Longitude : ", position.longitude_deg)
        print("Altitude : ", position.relative_altitude_m)


# Vitesse
async def print_vitesse(drone):
    async for vitesse in drone.telemetry.fixedwing_metrics():
        print("Vitesse : ", vitesse.airspeed_m_s)


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
    os.system("chmod +x JMAVSim.sh\nopen JMAVSim.sh") # Exécution du shell JMAVSim.sh
    time.sleep(30) # Attente de l'ouverture de l'interface
    # Lancement de la mission
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(balises)) # Lancement du thread

