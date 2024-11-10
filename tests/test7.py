import bpy
import random
from modules.create import create
from modules.act import act
from modules.delete import delete_all
from modules.rigidbody import setup_rigidbody_world, add_rigidbody
from modules.material import makeMaterialWithStripes  # Import the function

def test7():
    # Delete all existing objects
    delete_all()
    
    # Set up the RigidBody world
    setup_rigidbody_world()
    
    # Create 50 spheres with random scale, rigidbody, and striped material
    for i in range(50):
        sphere_name = f"Sphere_{i}"
        
        # Create sphere
        create.sphere(sphere_name)
        
        # Activate the sphere object
        obj = bpy.data.objects[sphere_name]
        
        # Add RigidBody
        add_rigidbody(obj, body_type='ACTIVE')
        
        # Set random scale
        random_scale = random.uniform(0.5, 1.5)
        act.scale((random_scale, random_scale, random_scale))
        
        # Set random position
        random_location = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(1, 10))
        act.location(random_location)
        
        # Add material with random colored stripes
        makeMaterialWithStripes(obj, stripe_count=12)