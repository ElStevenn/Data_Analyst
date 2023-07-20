import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

URL_BASE = "https://resultados.elpais.com/elecciones/2021/autonomicas/09/"
html = ".html"

"""Declare these arrays to insert each town"""
Barcelona_Dic = []
Lleida_Dic = []
Girona_Dic= []
Tarragona_Dic = []



class extract_party_data:
    """Class where I get a dictionary with province data. The objective is get all party votes, sum of all votes and town's name."""
    Data_Dic = []

    def __init__(self, province = None, print_values = False):
        """Get province ID"""
        if province.lower() == "barcelona":
            self.Province = (URL_BASE + "08", URL_BASE + "08" + html)
        elif province.lower() == "tarragona":
            self.Province = (URL_BASE + "43", URL_BASE + "43"+ html)
        elif province.lower() == "lleida":
            self.Province = (URL_BASE + "25", URL_BASE + "25" + html)
        elif province.lower() == "girona":
            self.Province = (URL_BASE + "17", URL_BASE + "17" + html)
        else:
            raise ValueError("You're not entered a correct province!")
        
        self.print_values = print_values
        self.Province_name = province.title()

        self.extract_data_and_filter()

    @staticmethod
    def remove_dot(number):
        if "." in number:
            number = number.replace(".", "")
        return number

    @staticmethod
    def filt_counter(num):
        if 1 <= num <= 9:
                return f"/0{num}"
        else:
            return f"/{num}"
        
    @staticmethod
    def get_total_party_votes(soup):
        table = soup.find_all("table", {"id":"tablaResumen"})[0]
        votes = BeautifulSoup(str(table), 'html.parser')
        party_votes = votes.find_all("td")[1]

        return party_votes.text
        
    def get_main_party_votes(self, soup):
        PSC, PP, VOX, Cs, ERC, ECP, JxCat, CUP = 0, 0, 0, 0, 0, 0, 0, 0

        party_votes = soup.find_all("table")[1]
        party_votesII = BeautifulSoup(str(party_votes), 'html.parser')

        party_votesIII = party_votesII.find_all("tbody")[0]
        party_votesIV = BeautifulSoup(str(party_votesIII), 'html.parser')

        party_votesV = party_votesIV.find_all("tr")

        for party in party_votesV[1:]:
            party_ = BeautifulSoup(str(party),'html.parser')
                        
            party_name = str(party_.find_all("acronym")[0].text)
            
            party_votes = str(party_.find_all("td")[0].text)
    

            if party_name == 'PSC':
                PSC = self.remove_dot(party_votes)
            elif party_name == 'ERC':
                ERC = self.remove_dot(party_votes)
            elif party_name == 'VOX':
                VOX = self.remove_dot(party_votes)
            elif party_name == "Cs":
                Cs = self.remove_dot(party_votes)
            elif party_name == "ECP-PEC":
                ECP = self.remove_dot(party_votes)
            elif party_name == "PP":
                PP = self.remove_dot(party_votes)
            elif party_name == "JxCat":
                JxCat = self.remove_dot(party_votes)
            elif party_name == "CUP-G":
                CUP = self.remove_dot(party_votes)
            else:
                pass
        
        return PSC, PP, VOX, Cs, ERC, ECP, JxCat, CUP
        

    
    def extract_data_and_filter(self):
        """Extract the data and apply a filter"""
        cont = 1
        total_iterations = 310 - cont  # Total number of iterations


        for cont in tqdm(range(cont, 310), desc=f"Extracting {self.Province_name} data"):
            response = requests.get(self.Province[0] + self.filt_counter(cont) + html)

            if response.status_code == 404:
                continue
            
            soup = BeautifulSoup(response.content, "lxml")
            Name = str(soup.find_all("h1")[1].text).strip()
            Total_party_votes = self.remove_dot(self.get_total_party_votes(soup).strip())
            party_votes = self.get_main_party_votes(soup)

            party_dic = {
                "town_name": Name,
                "party_votes": Total_party_votes,
                "PSC": party_votes[0],
                "PP": party_votes[1],
                "VOX": party_votes[2],
                "Cs": party_votes[3],
                "ERC": party_votes[4],
                "ECP": party_votes[5],
                "JxCat": party_votes[6],
                "CUP": party_votes[7]
            }

            if self.print_values:
                print(party_dic)

            # Aggregate new town in the array
            self.Data_Dic.append(party_dic)
        
    
    def __repr__(self):
        """These are all the party votes"""
        return str(self.Data_Dic)
           

if __name__ == "__main__":
    Barcelona_Provinces = extract_party_data("barcelona")
    print(Barcelona_Provinces)