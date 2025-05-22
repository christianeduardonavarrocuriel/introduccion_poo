class Mayor:

    def __init__(self) -> None:
        pass

    def mayor(self,n1: int, n2:int, n3:int) -> None:

        if n1 > n2:
            print(n1)

        elif n2 > n3:
            print(n2)

        elif n3 >= n1:
            print(n3)

mi_objeto = Mayor()
mi_objeto.mayor(1,2,3)
mi_objeto.mayor(1,3,2)
mi_objeto.mayor(3,2,1)
mi_objeto.mayor(3,1,2)
mi_objeto.mayor(3,3,1)
mi_objeto.mayor(3,1,3)
mi_objeto.mayor(1,3,3)
mi_objeto.mayor(3,3,3)