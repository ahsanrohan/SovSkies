import pyglet
import math

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # Velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Flags to toggle collision with bullets
        self.reacts_to_bullets = True
        self.is_bullet = False
        self.is_enemy = False

        # Flag to remove this object from the game_object list
        self.dead = False

        # List of new objects to go in the game_objects list
        self.new_objects = []

        # Tell the game handler about any event handlers
        # Only applies to things with keyboard/mouse input
        self.event_handlers = []
        self.wrap = True
        self.bind = False #bind to screen, no wrap around
        self.orientation = False

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Wrap around the screen if necessary
        if self.wrap == True:
            self.check_bounds()

        if not self.wrap and not self.bind: #destroy object once it leaves screen + buffer
            buffer = 200
            min_x = 0
            min_y = 0
            max_x = 1800
            max_y = 1000
            if self.x < min_x - buffer or self.y < min_y - buffer or self.x > max_x + buffer or self.y > max_y + buffer:
                self.dead = True

        if self.bind == True:
            self.bind_bounds()
        # Orient object to face object
        if self.orientation == True:
            if self.velocity_x == 0:
                self.rotation = 90
            else:
                self.rotation = 90 - math.degrees(math.atan2(self.velocity_y,self.velocity_x))

        
    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = 0
        min_y = 0
        max_x = 1800
        max_y = 1000
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y

    def bind_bounds(self):
        #print(self.x)

        min_x = 50
        min_y = 50
        max_x = 1500
        max_y = 950
        if self.x <= min_x:
            self.x = min_x
        if self.y <= min_y:
            self.y = min_y
        if self.x >= max_x:
            self.x = max_x
        if self.y >= max_y:
            self.y = max_y

    def collides_with(self, other_object):
         #Determine if this object collides with another

    #     # Ignore bullet collisions if we're supposed to
         if not self.reacts_to_bullets and other_object.is_bullet:
             return False
         if self.is_bullet and not other_object.reacts_to_bullets:
             return False

         # Calculate distance between object centers that would be a collision,
         # assuming square resources



         collision_distance = self.image.width * 0.4 * self.scale \
                              + other_object.image.width * 0.4 * other_object.scale
        
         collision_distance_x = self.image.width * .03 * self.scale \
                              + other_object.image.width *  other_object.scale

         collision_distance_y = self.image.height * .03 * self.scale \
                              + other_object.image.height *  other_object.scale
        

         # Get distance using position tuples
         actual_distance_x = abs(self.position[0]- other_object.position[0])
         actual_distance_y = abs(self.position[1] - other_object.position[1])
         actual_distance = math.sqrt((self.position[0] - other_object.position[0]) ** 2 +
                                     (self.position[1] - other_object.position[1]) ** 2)
         #util.distance(self.position, other_object.position)

         return (actual_distance <= collision_distance or actual_distance_x <= collision_distance_x and actual_distance_y <= collision_distance_y)

    def handle_collision_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.health = self.health - other_object.damage
            self.color = (255,100,100)
            pyglet.clock.schedule_once(self.revert_color, 0.1)
            

        if other_object.is_bullet == True and other_object.die_on_impact == True:

            pyglet.clock.schedule_once(other_object.die, 0)

    def revert_color(self, dt):
        self.color = (255,255,255)
