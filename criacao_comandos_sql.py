dic_ufs = {}

arq = open("municipio.txt", encoding='utf-8')

saida = open("comandos.sql", encoding="utf8", mode="w")

for registro in arq:
    #print(registro)
    campos = registro.split(";")
    cod_uf = int(campos[1])
    uf = campos[0]
    cod_mun = int(campos[2])
    mun = campos[3]
    
    if not "'" in mun:
        mun = mun.replace("'", "\'")
        #print(f"insert into estado(id, uf) values({cod_uf}, '{uf}');")
        #print(f"insert into municipio values({cod_mun}, '{mun}', {cod_uf});")
        if not cod_uf in dic_ufs:     
            saida.write(f"insert into estado(id, uf) values({cod_uf}, '{uf}');")
            saida.write("\n")
            dic_ufs[cod_uf] = cod_uf
        saida.write(f"insert into municipio values({cod_mun}, '{mun}', {cod_uf});")
        saida.write("\n")
 
saida.close()