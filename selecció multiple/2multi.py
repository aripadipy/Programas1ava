if selec == 1:
  km = int(input("Quin valor?\n"))
  print("""
      1)mm
      2)mt""")

  conversion = int(input("en que vols convertirlo?\n"))
  if conversion == 1:
    print((km * 1000)/1852)
  elif conversion == 2:
    print((km * 1000)/1609)

  conversion = int(input("en que vols convertirlo?\n"))
  if conversion == 1:
    print((km * 1000)/1852)
  elif conversion == 2:
    print((km * 1000)/1609)
if selec == 2:
  mm = int(input("Quin valor?\n"))
  print("""
      1)km
      2)mt""")

  conversion = int(input("en que vols convertirlo?\n"))
  if conversion == 1:
    print(mm * 1852)
  elif conversion == 2:
    print((mm * 1,151))
if selec == 3:
  mt = int(input("Quin valor?\n"))
  print("""
      1)km
      2)mm""")
  conversion = int(input("en que vols convertirlo?\n"))
  if conversion == 1:
    print(mt * 1609)
  elif conversion == 2:
    print(mt / 1,151)