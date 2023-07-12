fd = open("mbox-short.txt", "w")
lst = ["primera linea\n", "segunda linea\n"]

fd.writelines(lst)
fd.close()

