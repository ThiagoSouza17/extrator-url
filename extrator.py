import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_nome_parametro(self):
        lista_de_nome_de_parametros = []
        indice_e_comercial = self.get_url_parametros().find('&')
        if indice_e_comercial == -1:
            indice_parametro = self.get_url_parametros().find('=')
            nome = self.get_url_parametros()[:indice_parametro]
            lista_de_nome_de_parametros.append(nome)
        else:
            indice_parametro = self.get_url_parametros().find('=')
            nome = self.get_url_parametros()[:indice_parametro]
            lista_de_nome_de_parametros.append(nome)
            indice_nome_anterior = 0
            for num in range(self.get_url_parametros().count('=') - 1):
                indice_e_comercial = self.get_url_parametros().find('&', indice_nome_anterior)
                nome = self.get_url_parametros()[indice_e_comercial + 1:self.get_url_parametros().find('=', indice_e_comercial)]
                indice_nome_anterior = indice_e_comercial + 1 + len(nome)
                lista_de_nome_de_parametros.append(nome)
        return lista_de_nome_de_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "URL Base: " + self.get_url_base() + "\n" + "Parâmetros: " + "\n" \
               + [(self.get_nome_parametro()[x] + " = " + self.get_valor_parametro(self.get_nome_parametro()[x])) for x in range(len(self.get_nome_parametro()))].__str__()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=10000&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
# extrator_url2 = ExtratorURL(url)

print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)

# print(extrator_url == extrator_url2)
# print(id(extrator_url))
# print(id(extrator_url2))

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
if moeda_origem == "real":
    conversao_real_para_dolar = int(quantidade) / VALOR_DOLAR
    print("Conversão: {:0.2f}".format(conversao_real_para_dolar), " doláres")
