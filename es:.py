#Esercizio 1: Creare una classe Automobile che abbia gli attributi
#"marco", "modello" e "anno". Aggiungi un metodo "descrivi che stampi una descrizione dell'automobile,
#ad esempio "Questa è una Toyota
#Corolla del 2017

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
#Esercizio 2: Creare una classe Impiegato che abbia gli attributi "nome*
#"cognome", "matricola" e "stipendio". Aggiungere un metodo
#"aumenta _stipendio chi, aumenti lo stipendio dell'impiegato del 10% e un metodo "stampa _dettagli che stampi tutti i dettagli dell'impiegato, ad esempio "Impiegato: Marco Rossi, matricola 12345, stipendio: 3000
#Euro'.

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



