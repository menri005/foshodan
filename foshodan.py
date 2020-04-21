import shodan
import argparse

parser = argparse.ArgumentParser(description='Use FOSHOdan to look up crap in Shodan.')
parser.add_argument('api_key', help='Your Shodan API key')

cli_args = parser.parse_args()

api_key = cli_args.api_key
shodan_api = shodan.Shodan(api_key)

# These will be built like tuples, with include the following
# (search term, keyword in data, screenshot is true)
# this is equivalent to a search query like 
# product:"webcam" data:"+logitech+"
# but beqcause im cheap and I have a free account, I cant use filtering
# so Im just going to scrape data from the responses
terms = [
    ('webcam', 'webcam'),
    ('idrac', ''),
    ('gps', 'ship'),
    ('hvac', 'hvac'),
    ('webcam', 'traffic'),
    ('server', 'telnet'),
    ('wordpress', 'admin'),
    ('windmill', 'windmill'),
    ('router', 'shellshock')
]

for term in terms:
    product = term[0]
    data = term[1]

    print('LOOKING FOR {} CONTAINING {} IN DESCRIPTION'.format(product.upper(), data.upper()))

    results = shodan_api.search(product)

    for result in results['matches']:

        if data in result['data']:
            ip = result['ip_str']
            port = result['port']
            url = 'https://shodan.io/host/{}'.format(ip)
            info = ";".join(result['hostnames'])

            description = '''
            IP and port - {ip}:{port}
            URL - {url}
            Info - {info}\n\n
            '''.format(ip=ip, port=port, url=url, info=info)

            print(description.strip())