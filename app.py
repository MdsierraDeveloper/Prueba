from data import Data


#objeto que contiene las empresas y las sucursales.
datos = Data.get_companies()
sucursal = Data.get_branches()



class mostrarCompañias():
    print("datos cargandose...")
    for i in datos:
        print(i)
    
    def mostrarSucursalesId():
        print("sucursales cargando...")
        array = sucursal.key()
        for i in sucursal:
            print(i)
            array = sucursal.key()
        return array
    
        
    

    print(mostrarSucursalesId())
   

        


    

