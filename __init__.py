from googlesearch import search


# TO-DO: Exportar as queries de um Excel. 
# TO-DO: Fazer um regex para adicionar o dominio do site 

def get_domain(domain_file="domain.txt"):
    """
    Open the domain.txt and get the domain name from it
    """
    #TO-DO: Utilizar alguma flag no terminal para pegar referenciar esse file (ex: -f)
    try:    
        with open(domain_file, "r") as f: 
            domain_name = [line.strip() for line in f if line.strip()]
            return domain_name
    except Exception as e:
        print(f"Error: {e}")

def search_domain(domains):
    """
    Search for a domain or a list of domain using Google Dorking
    """
    for domain in domains:
        query = f"site: {domain}"
        for result in search(query, num_results=5, lang="en"):
            print(result)

if __name__ == '__main__':
    search_domain(get_domain())
    