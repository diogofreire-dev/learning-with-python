import datetime

agora = datetime.datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

print("Data e hora atuais:", data_formatada)

# %d → Dia (ex: 26)
# %m → Mês (ex: 02)
# %Y → Ano com 4 dígitos (ex: 2025)
# %H → Hora (00-23)
# %M → Minutos (00-59)
# %S → Segundos (00-59)