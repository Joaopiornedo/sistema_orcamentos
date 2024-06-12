from fpdf import FPDF 

#dados cliente
nome = str(input("Digite o Nome do cliente: "))
telefone = str(input("Digite o telefone do cliente: "))
endereco = str(input("Digite o endereço do cliente: "))
servico = str (input("Serviço a ser feito: "))
descricao_servico = str (input(" Descrição do serviço a ser feito: "))
#valores :
valor_hora = 100
estimativa_horas = int(input("Digite as horas trabalhadas: "))
valor_total = valor_hora * estimativa_horas 
data_orcamento= str(input("Data Orçamento: "))
#criando pdf 
pdf = FPDF()
pdf.add_page()
#definindo a fonte 
pdf.set_font('Arial', 'B', 11);
pdf.image("template.png", x=0, y=0, w=pdf.w, h=pdf.h)
#posicionamento do texto:
pdf.text(160, 120,str(data_orcamento))
pdf.text(170, 150,str(valor_total))
pdf.text(140, 93,nome)
pdf.text(140, 100,str(telefone))
pdf.text(140, 107,endereco) 
pdf.text(24, 150,servico)
pdf.text(95, 150,descricao_servico)
#salvando o arquivo pdf :
pdf.output(f'./Orçamento {nome}.pdf') 

