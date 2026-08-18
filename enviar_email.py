import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

def send_email(para: list, cc: str = None, assunto: str = "Teste de Envio de E-mail via Python", ficheiro: str = None):
    MEU_EMAIL = "miguelsilvams1998@gmail.com"
    MINHA_SENHA_APP = os.getenv("MINHA_SENHA_GMAIL")  

    CORPO_HTML = """
        <h2>Teste de Automação</h2>
        <p>Este é um e-mail de teste enviado diretamente pelo Python!</p>
    """

    try:
        print("A conectar ao servidor do Microsoft...")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(MEU_EMAIL, MINHA_SENHA_APP)

            # Iterar sobre cada destinatário da lista para envios individuais
            for destinatario in para:
                mensagem = MIMEMultipart()
                mensagem["From"] = MEU_EMAIL
                mensagem["To"] = destinatario
                mensagem["Subject"] = assunto

                if cc:
                    mensagem["Cc"] = cc

                # Anexa o corpo do e-mail
                mensagem.attach(MIMEText(CORPO_HTML, "html"))

                # Trata o anexo caso um caminho de arquivo seja passado
                if ficheiro and os.path.exists(ficheiro):
                    with open(ficheiro, "rb") as f:
                        parte_anexo = MIMEBase("application", "octet-stream")
                        parte_anexo.set_payload(f.read())

                    encoders.encode_base64(parte_anexo)
                    nome_arquivo = os.path.basename(ficheiro)
                    parte_anexo.add_header(
                        "Content-Disposition",
                        f'attachment; filename="{nome_arquivo}"'
                    )
                    mensagem.attach(parte_anexo)

                # Monta a lista final de quem vai receber na rede
                destinatarios_envio = [destinatario]
                if cc:
                    destinatarios_envio.append(cc)

                # Dispara o e-mail
                server.sendmail(MEU_EMAIL, destinatarios_envio, mensagem.as_string())
                print(f"✅ E-mail enviado com sucesso para: {destinatario}")

    except Exception as e:
        print(f"❌ Erro ao enviar: {e}")