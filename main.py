url_original = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

url_base = url[0:19]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

url_parametros = url[20:36]
print(url_parametros)

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)