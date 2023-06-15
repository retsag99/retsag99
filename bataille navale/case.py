class Case:
    
    def __init__(self, posX, posY, hasboat = False, boat=None, esttouche = False, image = None) -> None:
        
        self.x = posX
        self.y = posY
        
        self.hasboat = hasboat
        self.boat=boat
        self.boat_name=None
        self.voisin=0
        self.esttouche = esttouche
        self.image = image
    
    def get_hasboat(self):
        return self.hasboat
    def get_boat(self):
        if self.hasboate==True:
            return self.boat
    def get_voisin(self):
        return self.voisin
    def get_esttouche(self):
        return self.esttouche
    def get_image(self):
        return self.image
    
    def set_hasboat(self):
        self.hasboat=True
    def set_boat(self,boat):
        if self.hasboat==True:
            self.boat=boat
            self.boat_name=boat[0]
            self.image=boat[1]
            self.voisin=boat[3]
            
    def set_esttouche(self):
        self.esttouche=True
        self.image=self.boat[2]
    def set_image(self,image):
        self.image=image
        
    def __str__(self) -> str:
        if self.hasboat:
            return "B"
        if self.esttouche:
            return "T"
        return str(self.image)