import requests
from bs4 import BeautifulSoup

# Mes fonctions de traitement de traitement
def tous(tab):
    '''
    Tous est une fonction qui prend un parametre qui dois etre un tableau
    et retourne un tableau

    elle manipule le tableau pour ajouter tout sont contenue dans un second tableau et calcule tout les kilometre
    de chaque distance et le temps que cela met

    ======
    param type list : tab 

    '''
    res = []
    km = 0
    etape = (len(tab)-1) * 45
    temps = [0,0]
    temps[1] += etape
    for i in range(len(tab)):
        res.append(tab[i])
    for j in range(len(tab)):
        km = km + int(str(tab[j][2]).replace(u'\xa0', ''))
    for k in range(len(tab)):
        h, m = tab[k][3].split(':')
        temps[0] += int(h)
        temps[1] += int(m)
        if temps[1] >= 60:
            temps[0] += 1
            temps[1] -= 60
    res.append(km)
    res.append(f'{temps[0]}:{temps[1]}')
    return res
        
def pause(h, m):
    '''
    Pause est une fonction qui prend en parametre des heures et des minutes et calcule si
    les minutes depasse 60, si oui, on rajoute une heure au heures

    retourne une chaine de caractere contenant l'heure apres traitement et les minutes apres traitement.

    ======
    param type string: h
    param type string: m

    '''
    for i in range(int(h)//2):
        m = int(m) + 15
        if int(m) >= 60 :
            h = int(h) + 1
            m = int(m) - 60
    return str(h)+':'+str(m)

class Parcours:

    def __init__(self):
        villes = []
        enter = input('Entrez une adresse: ')
        villes.append(enter)
        while enter != 'stop':
            enter = input('Entrez une adresse: ')
            villes.append(enter)
        self.toutesLesVilles = []
        for i in range(len(villes)):
            self.toutesLesVilles.append(villes[i])
        del self.toutesLesVilles[-1]
        self.vitesseMaxAutoroute = '90'
        self.vitesseMaxRoute = '50'
        self.conso = '12'
        self.prixEssence = '1.8'

    def __repr__(self):
        return f'Parcours de : {self.toutesLesVilles}'

    def main(self, villes):
        toutesLesVilles = []
        for i in range(len(villes)):
            toutesLesVilles.append(villes[i])
        if len(toutesLesVilles) > 2:
            res = []
            for i in range(len(toutesLesVilles)):
                try:
                    res.append(self.main([toutesLesVilles[i], toutesLesVilles[i+1]]))
                except:
                    pass
            return tous(res)
        depart = toutesLesVilles[0]
        arrive = toutesLesVilles[-1]
        res = self.data([depart, arrive])
        return [depart, arrive, res[0], pause(res[1], res[2])]

    def data(self, villes):
        if len(villes) > 1:
            # Toute mes variables
            depart = villes[0]
            arrive = villes[-1]
            url = f'https://www.bonnesroutes.com/widget/v1/route?defaultFrom=&defaultTo=&defaultVia=&defaultFuelConsumption=&defaultFuelPrice=&defaultSpeedLimitMotorway=&defaultSpeedLimitOther=&showVia=0&showSpeedProfile=1&showFuelCalc=1&showResultLength=1&showResultDrivingTime=1&showResultFuelAmount=1&showResultFuelCost=1&showResultCustomizedCost=0&showResultMap=1&showResultScheme=1&onlyCountries=&preferCountries=&css=https%3A%2F%2Fwww.bonnesroutes.com%2Fwidget%2Fv1%2Fwidget.css%3Fpc%3D269adb%26bc%3Dffffff%26tc%3D000000%26ff%3D%2522Open%2520Sans%2522%252C%2520Helvetica%252C%2520Roboto%252C%2520Arial%252C%2520sans-serif%26fs%3D16px&currency=EUR&measure=metric&customizedCostFormula=&customizedCostLabel=&from={depart}&to={arrive}&v=&sm={self.vitesseMaxAutoroute}&so={self.vitesseMaxRoute}&fc={self.conso}&fp={self.prixEssence}'
            r = requests.post(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            km = soup.find(attrs={'id': 'total_distance' }).get_text().replace('km','').replace(u'\xa0', '')
            distance_h = soup.find(attrs={'id': 'total_time_hours' }).get_text().replace('h', '')
            distance_m = soup.find(attrs={'id': 'total_time_minutes' }).get_text().replace('min', '')
            # conso_litre = soup.find(attrs={'id': 'fuel_amount' }).get_text()
            # cout_essence = soup.find(attrs={'id': 'fuel_cost' }).get_text()
            return [km, distance_h, distance_m]

test = Parcours()
print(test.main(test.toutesLesVilles))