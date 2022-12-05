#python 3.11
import requests
import webbrowser

def search(search_keywords):
    search_result = requests.get("https://ru.hitmotop.com/search?q=" + search_keywords.replace(" ", "+")).text
    search_result = search_result[search_result.find('<div class="p-info p-inner">'):]
    search_result = search_result[search_result.find('<ul class="tracks__list">'):]
    search_result = search_result.split("href=")
    choosen_results = []
    for searches in search_result:
        if searches.startswith('"http'):
            choose = searches[1:]
            choose = choose[:choose.find('"')]
            if choose.find("/get/") > -1:
                choosen_results.append(choose)
    return choosen_results


def getmusicbyurl(url):
    print(track)
    search_result = requests.get(url).text
    search_result = search_result[search_result.find('<div class="tracks__item track mustoggler"') + 42:]
    search_result = search_result[search_result.find('<a data-nopjax') + 14:]
    search_result = search_result[search_result.find('href="') + 6:]
    return search_result[:search_result.find('"')].replace("\\", "")


print('Download music from ru.hitmotop.com\nRequires to use move_mp3 from time to time\n')
tracks = search(input("Search keywords: "))
for cnt, track in enumerate(tracks):
    print(f"{cnt+1}: {track.split('/')[-1].replace('_', ' ')}")
choisen_index = input(f"Choose {1}-{len(tracks)}: ")


if len(choisen_index) > 1:
    list_of_indexes = [int(x) for x in choisen_index.split()]
elif len(choisen_index) == 1:
    list_of_indexes = [choisen_index]

for index in list_of_indexes:
    if 1 <= int(index) <= 48:
        webbrowser.open(tracks[int(index) - 1])
        continue
    print(f'{index} - Index out of range')


