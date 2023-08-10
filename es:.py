'''
class automobile():
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi(self):
        print(f"questa è una {self.marca} {self.modello} del {self.anno}")

automobile1= automobile("Toyota", "corolla", 2017)
automobile2= automobile("AlfaRomeo", "mito", 2009)
automobile3= automobile("Mercedes", "classe A", 2019)

automobile1.descrivi()
automobile2.descrivi()
automobile3.descrivi()
'''
'''
class impiegato():
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio  = stipendio

    def aumenta_stipendio(self):
        self.stipendio *= 1.1 

    def stampa_dettaglio(self):
        print(f"impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio: {self.stipendio: .2f} euro ")

impiegato = impiegato("nabil", "chabab", "1234", 2000)
impiegato.stampa_dettaglio()
impiegato.aumenta_stipendio()
impiegato.stampa_dettaglio()
'''

# ereditarietà es


class veicolo ():
    def __init__ (self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def accelera(self):
        print("sto accelerando")
    
    def ferma (self):
        print("sto frenando")
    
    def __str__(self):
        return f"Marca: {self.marca}, modello: {self.modello}, anno: {self.anno}"


class automobile(veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore
    def cambia_colore(self, nuovo_colore):
        self.colore = nuovo_colore
    def __str__(self):
        return super().__str__() + f", colore: {self.colore}"


automobile = automobile ("Ferarri, Enzo, 2004 ")

automobile.cambia_colore()
