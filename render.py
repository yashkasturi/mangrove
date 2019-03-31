from bs4 import BeautifulSoup

with open("mangrove_Index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")

BeautifulSoup("Sacr&eacute; bleu!")
