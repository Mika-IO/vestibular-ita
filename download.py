import time
import requests


def download_url(urls, base_path="C:\\Users\\Mikaio\\Desktop\\ITA\\provas\\"):
    for url in urls:
        fn = base_path + url.split("/")[-1]
        r = requests.get(url)
        with open(fn, "wb") as f:
            f.write(r.content)


urls = [
    "https://www.vestibular.ita.br/provas/2023_fase1.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2023.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2023_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2023_2f.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2023_2f.pdf",
    "https://www.vestibular.ita.br/provas/redacao_2023_2f.pdf",
    "https://www.vestibular.ita.br/provas/2022_fase1.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2022.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2022_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2022_2f.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2022_2f.pdf",
    "https://www.vestibular.ita.br/provas/redacao_2022_2f.pdf",
    "https://www.vestibular.ita.br/provas/2021_fase1.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2021.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2021_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2021_2f.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2021_2f.pdf",
    "https://www.vestibular.ita.br/provas/redacao_2021_2f.pdf",
    "https://www.vestibular.ita.br/provas/2020_fase1.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2020.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2020_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2020_2f.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2020_2f.pdf",
    "https://www.vestibular.ita.br/provas/redacao_2020_2f.pdf",
    "https://www.vestibular.ita.br/provas/2019_fase1.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2019.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2019_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2019_2f.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2019_2f.pdf",
    "https://www.vestibular.ita.br/provas/redacao_2019_2f.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2018.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2018.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2018.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2018.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2018.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2018.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2017.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2017.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2017.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2017.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2017.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2017.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2016.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2016.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2016.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2016.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2016.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2016.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2015.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2015.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2015.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2015.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2015.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2015.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2014.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2014.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2014.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2014.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2014.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2014.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2013.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2013.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2013.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2013.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2013.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2013.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2012.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2012.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2012.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2012.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2012.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2012.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2011.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2011.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2011.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2011.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2011.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2011.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2010.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2010.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2010.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2010.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2010.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2010.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2009.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2009.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2009.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2009.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2009.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2009.pdf",
    "https://www.vestibular.ita.br/provas/fisica_2008.pdf",
    "https://www.vestibular.ita.br/provas/portugues_2008.pdf",
    "https://www.vestibular.ita.br/provas/ingles_2008.pdf",
    "https://www.vestibular.ita.br/provas/matematica_2008.pdf",
    "https://www.vestibular.ita.br/provas/quimica_2008.pdf",
    "https://www.vestibular.ita.br/provas/gabarito_2008.pdf",
]

download_url(urls)
