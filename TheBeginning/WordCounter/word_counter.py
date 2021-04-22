import requests
from bs4 import BeautifulSoup
import operator


def start(url):

    word_list = []
    source_code = requests.get(url).text  # get the source code and convert it to text

    soup = BeautifulSoup(source_code)  # convert the source code to bs object

    for lecture_title in soup.findAll('font', {'size': '2'}):
        content = lecture_title.string

        if content is not None:
            sentence = content.lower().split()
            for word in sentence:
                word_list.append(word)
                print(word)


start('https://audio.iskcondesiretree.com/index.php?q=f&f=%2F01_-_Srila_Prabhupada%2F02_-_Bhajans%2FVol-01%2F01_-_Krsna_Meditations')

