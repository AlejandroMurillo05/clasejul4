text = open("mbox-short.txt")
emails = set()
for x in text:
    if x.startswith("From:"):
        x = x[6:]
        emails.add(x)
enviar = list(emails)
for i in range(len(enviar)-1, 0, -1):
    x = enviar[i]
    print("Enviado OK\t", x.rstrip())
text.close()
    