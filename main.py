from emails.guardar_arquivo import guardar_pasta
from enviar_email import send_email

# Lista de e-mails de destino
EMAILS_DESTINO = [
    'contavfs002@gmail.com', 
    'contavfs004@gmail.com',
    'contavfs003@gmail.com'
]

def main():
    print("Iniciando o processo de automação...")
    
    # 1. Consulta o BD e salva o arquivo Excel no diretório
    caminho_ficheiro = guardar_pasta()
    print(f"Ficheiro gerado em: {caminho_ficheiro}")

    # 2. Realiza o envio dos e-mails com o anexo gerado
    send_email(para=EMAILS_DESTINO, ficheiro=caminho_ficheiro)
    
    print("Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()