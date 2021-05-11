import requests
from bs4 import BeautifulSoup




def main():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    # Specify details of the rows I want
    rows = soup.find_all('tr', class_="TableBase-bodyTr")

    # player, team, position, touchdowns
    for n, i in enumerate(rows):
        if n > 19:
            break
        col = i.find_all("td")
        p1 = col[0].find('span', class_="CellPlayerName--long")
        name = p1.find('a').text.strip()
        position = p1.find('span', class_="CellPlayerName-position").text.strip()
        team = p1.find('span', class_="CellPlayerName-team").text.strip()

        touchdowns = col[8].text.strip()
        print(f"name: {name} | position: {position} | team: {team} | td: {touchdowns}")


main()