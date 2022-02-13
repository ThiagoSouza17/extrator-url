url_original = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

url_base = url[0:19]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

url_parametros = url[20:36]
print(url_parametros)
