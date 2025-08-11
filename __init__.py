from googlesearch import search


# TO-DO: Exportar as queries de um Excel. 
# TO-DO: Fazer um regex para adicionar o dominio do site 

def get_domain(domain_file="domain.txt"):
    #Open the domain.txt and get the domain name from it
    #TO-DO: REGEX, caso necessite
    #TO-DO: Utilizar alguma flag no terminal para pegar referenciar esse file (ex: -f)
    try:    
        with open(domain_file, "r") as f:
            domain_name = f.readline().strip()
            print(domain_name)
        return domain_name
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    query = get_domain()
    for result in search(query, num_results=10, lang='en'):
        print(result)