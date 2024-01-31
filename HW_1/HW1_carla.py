import carla
import random
import math
import time 
client = carla.Client('localhost', 2000)
world = client.get_world()

vehicle_blueprints = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()

vehicle_bp = vehicle_blueprints.find('vehicle.audi.tt')
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

spectator = world.get_spectator()
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=2.5)),vehicle.get_transform().rotation)
spectator.set_transform(transform)

for i in range(30):
   vehicle_bp = random.choice(vehicle_blueprints.filter('vehicle'))
   npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
   
for v in world.get_actors().filter('*vehicle*'):
    v.set_autopilot(True)

camera_bp = vehicle_blueprints.find('sensor.camera.rgb')
camera_init_trans = carla.Transform(carla.Location(z=2))
camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to = vehicle)

camera.listen(lambda image: image.save_to_disk('out/%06.png'% image.frame))

camera.stop()
