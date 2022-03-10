import json
import requests

def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found')
    
    if not bing_api_key:
        raise KeyError('Bing key not found')


    return bing_api_key

def run_query(search_terms):
    bing_key = read_bing_key() # prepares authentication
    search_url = "https://api.bing.microsoft.com/v7.0/search" # prepare the URL that we'll be requesting
    headers = {'Ocp-Apim-Subscription-Key':bing_key}
    params = {'q':search_terms, 'textDecorations':True, 'textFormat':'HTML'}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title':result['name'],
            'link':result['url'],
            'summary':result['snippet']
        })
    return results

# for test
def main():
    print("Please input your search")
    results = run_query(input())

    for i in results:
        print('title: %s\n' %i['title'])
        print('link: %s\n' %i['link'])
        print('summary: %s\n' %i['summary'])
        print('=============================================================')

    

if __name__ == '__main__':
    main()