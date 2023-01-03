class Book:
    titre: str
    prix: float
    rating: int
    disponibility: bool
    img: str

    def __init__(self, titre, prix, rating, disponibility, img):
        self.titre = titre
        self.prix = prix
        self.rating = rating
        self.disponibility = disponibility
        self.img = img

    def __str__(self):
        return f'''
        title : {self.titre}\n
        prix : {self.prix}\n
        note : {self.rating}\n
        disponibility : {self.disponibility}\n
        image : {self.img}\n                
        '''
