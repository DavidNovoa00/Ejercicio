print ("bienbenidos a la Pelukeria")
print ("")

u=int(input("Digite opcion"))

if (u==1):
    print ("")
    print ("Historia")
    print ("Pelukeria.Nació en 2000 en Bogota como una pequeña tienda con productos importados de uso general y de perfumería")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Vision")
    print ("Ser reconocidos como líderes en belleza")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Mision")
    print ("Somos Belleza, Higiene, Salud y Bienestar")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Valores")
    print ("Innovación, pasión, trabajo en equipo y excelencia")

if (u==2):
    print ("catalogo digite (1)")
    print ("servicios digite (2)")
   

    x=int(input("digite opcion"))
    if (x==1):
        print ("Maquillaje")
        

        print ("Stick corrector purificante")
        print ("30.000")
        print ("codigo 101")
        print ("---------------------------------")

        print ("Eternal Cream")
        print ("35.000")
        print ("codigo 102")
        print ("---------------------------------")

        print ("Eternal Repair body serum")
        print ("45.000")
        print ("codigo 105")
        print ("---------------------------------")

        print ("Eternal Sleeping oil")
        print ("35.000")
        print ("codigo 106")
        print ("---------------------------------")

        o=int(input (" si desea Compras (1), si no desea comprar (2) "))

        if o==1:
            print ("esta registrado")
            r=int(input (" si  (1), no  (2) "))
            if r == 1:
                id=int(input("ingresa tu identificacion "))
                if id==1111:
                    print ("gracias por su compra")
                else:
                    print ("usuario invalido")
            else:
                print ("registrarse ")        
                nombre=str(input("digite nombre "))
                g=str(input("digite su correo "))
                n=int(input("digite su numero de celular "))

                print ("bienbenido ",nombre," su identificacion es 1111 ")
        else:
            print ("gracia por ver nuestra pagina")
    if  x== 2:
        print (" sevicio") 

        print ("Manicura (parafina, IBX, gel, acrílico y semipermanente)")
        print ("30.000")
        print ("---------------------------------")
        
        print ("Pedicura")
        print ("30.000")
        print ("---------------------------------")

        print ("Maquillaje (novia, novio, invitados y todo tipo de eventos")
        print ("35.000")
        print ("---------------------------------")

        print ("Extensión, lifting y tinte de pestañas y microblending de cejas")
        print ("35.000")
        print ("---------------------------------")

        print ("Todo tipo de de depilaciones, incluido láser, IPL y Neodimio-YAG")
        print ("20.000")
        print ("---------------------------------")