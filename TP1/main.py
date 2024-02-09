
file_path = 'emd.csv'
emd = []
with open(file_path, mode='r') as file:
    lines = file.readlines()
    
    headers = lines[0].strip().split(',')
    
    for line in lines[1:]:
        values = line.strip().split(',')
        row_dict = dict(zip(headers, values))
        emd.append(row_dict)

def modalidade_ord_aplhabetical(emd):
    return [row['modalidade'] for row in sorted(emd, key=lambda x: x['modalidade'])]

def percent_atletas_aptos_inaptos(emd):
    n_aptos = sum([1 for row in emd if row['resultado'] == "true" ])
    return (n_aptos/len(emd), 1 - n_aptos/len(emd))

def atletas_por_escalao(emd):
    dist_p_idade = {}
    for row in emd:
        idade = int(row['idade'])
        escalao = f"{(idade // 5) * 5}" + f"{(idade // 5) * 5 + 4}"
        dist_p_idade[escalao] = dist_p_idade.get(escalao, 0) + 1
    return dist_p_idade
    