import os
import smtplib
import sys
from email.mime.text import MIMEText


def enviar_email():
    email_from     = os.environ.get("EMAIL_FROM", "")
    email_password = os.environ.get("EMAIL_PASSWORD", "")
    email_to       = os.environ.get("EMAIL_TO", "")

    #apenas para identifcar no log
    if not all([email_from, email_password, email_to]):
        print("ERRO: EMAIL_FROM, EMAIL_PASSWORD e EMAIL_TO devem ser Secrets no GitHub Actions.", file=sys.stderr)
        sys.exit(1)

    tests_status = os.environ.get("TESTS_STATUS", "unknown")
    build_status = os.environ.get("BUILD_STATUS", "unknown")
    repo         = os.environ.get("GITHUB_REPOSITORY", "desconhecido")
    run_number   = os.environ.get("GITHUB_RUN_NUMBER", "?")
    run_id       = os.environ.get("GITHUB_RUN_ID", "")
    branch       = os.environ.get("GITHUB_REF_NAME", "desconhecida")
    deploy_status = os.environ.get("DEPLOY_STATUS", "unknown")
    status_geral = "SUCESSO" if tests_status == "success" and build_status == "success" else "FALHA"

    assunto = f"[CI/CD] {status_geral} — {repo} #{run_number}"

    corpo = f"""Pipeline CI/CD finalizado.

Repositório : {repo}
Branch      : {branch}
Execução    : #{run_number}

Testes : {tests_status.upper()}
Build  : {build_status.upper()}
Deploy : {deploy_status.upper()}
"""

    msg = MIMEText(corpo, "plain", "utf-8")
    msg["From"]    = email_from
    msg["To"]      = email_to
    msg["Subject"] = assunto

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(email_from, email_password)
        servidor.sendmail(email_from, email_to, msg.as_string())

    print(f"Notificação enviada para {email_to}.")


if __name__ == "__main__":
    enviar_email()
