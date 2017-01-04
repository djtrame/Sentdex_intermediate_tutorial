#installed beautifulsoup4, downloaded and installed the wheel file for lxml, then installed requests
from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_starting_url():
    #get 3 random lowercase characters
    starting3Chars = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting3Chars, '.com'])
    return url

# url = random_starting_url()
# print(url)

#create a spider
#spider = go to website, find all the links, then go to all those links and spider out
def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

#return a list of links from any url
def get_links(url):
    try:
        response = requests.get(url)
        soup = bs.BeautifulSoup(response.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        print(str(e))
        return []

def main():
    how_many_links_to_crawl = 50
    p = Pool(processes=how_many_links_to_crawl)

    #a list of links to parse
    parse_us = [random_starting_url() for _ in range(how_many_links_to_crawl)]

    #data is a list of lists
    data = p.map(get_links, [link for link in parse_us])

    #for every URL in each of the many URL lists
    #take a list of list, take each list from those lists and put it in a single list
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('urls.txt', 'w') as f:
        f.write(str(data))


if __name__ == '__main__':
    main()


