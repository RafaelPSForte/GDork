from googlesearch import search


# TO-DO: Pegar um domínio de um file.txt para usar como parâmetro
# TO-DO: Exportar as queries de um Excel. 
# TO-DO: Fazer um regex para adicionar o dominio do site 


if __name__ == '__main__':
    query = ""
    for result in search(query, num_results=10, lang='en'):
        print(result)