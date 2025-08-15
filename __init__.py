from ddgs import DDGS
import argparse


# TO-DO: Exportar as queries de um Excel. 
# TO-DO: Fazer um regex para adicionar o dominio do site 

def get_parse():
    """
    Get the flags from the terminal
    """
    parser = argparse.ArgumentParser(description="Script for GoogleDorking by Domains CLI inputs")
    parser.add_argument("-f", required=False, type=str, help="Path for the domain file .txt")
    parser.add_argument("--max-results", required=False, type=int,default=1, help="Specify how many results to return")
    
    return parser.parse_args()

def get_domain(domain_file):
    """
    Open the domain.txt and get the domain name from it
    """
    try:    
        with open(domain_file, "r") as f:
            domain_name = [line.strip() for line in f if line.strip()]
            if not domain_name:
                print("There is no domain name in the .txt file.")
                return None
            return domain_name
    except Exception as e:
        print(f"Error: {e}")

def search_domain(domains, num_results = 5):
    """
    Search for a domain or a list of domain using Google Dorking
    """
    if not domains:
        return
    
    with DDGS() as ddgs:
        for domain in domains:
            query = f"site:{domain}"
            count = 0
            for r in ddgs.text(query, max_results=num_results):
                print(r['title'])
                count+=1
                if count >=num_results:
                    break
                

if __name__ == '__main__':
    args = get_parse()
    
    if args.f:
        search_domain(get_domain(args.f), args.max_results)
    else:
        print("Domain file were NOT found, please add '-f path_to_file/domain_file.txt'")