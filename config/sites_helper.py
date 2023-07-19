import pickle

if __name__ == '__main__':
    with open("sites.dat", "rb") as f:
        sites = pickle.load(f)

    # print(pickle_load['indexer'][1])
    for site in sites['indexer']:
        if site['id'] == 'chdbits':
            site['domain'] = 'https://ptchdbits.co/'
            print(site)

    sites_conf = sites['conf']
    sites_conf['ptchdbits.co'] = sites_conf['chdbits.co']
    for site, value in sites['conf'].items():
        print(site, value)

    with open("sites2.dat", "wb") as f:
        pickle.dump(sites, f)

