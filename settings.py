class Settings():
    """A class to store all setting"""
    def __init__(self):
        """inirialise the game setting"""
        #screen setting
        self.screen_width=600
        self.screen_height=1200
        self.bg_color=(230,230,230)
        #ship settings
        self.ship_limit=3
        #bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10
        #alien settings
        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.initialise_dynamic_settings()
    
    def initialise_dynamic_settings(self):
        """initialises value"""
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1
        self.alien_point=50

    def increase_speed(self):
        """incraese game speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * 1.5)
