class memory:
    def __init__(self):
        self.bit = "0 and 1" #smallest unit in computer
        self.one_nibble = 4 #bits
        self.one_bytes = 8 #bits
        self.one_kilobyte = 1024 #bytes
        self.one_megabyte = 1024 #KB
        self.one_gigabyte = 1024 #MP
        self.one_terabyte = 1024 #GB
        self.one_petabyte = 1024 #TB
        self.one_Exabyte = 1024 #PB
        self.one_zetabyte = 1024 #EB
        self.one_Yottabyte = 1024 #ZB

    def bits(self):
        n = int(input("Check Your Nibbles: "))
        # todo 1bits is equal to: 0.25 Nibbles
        # todo divide the digital storage value by 4
        f=4
        r=n/f
        print(f"Total Nibble in {n} bits : {r} Nibbles")
        print()

    def nibble(self):
        n=int(input("Enter Your Nibble: "))
        x=self.one_nibble
        # todo multiply the digital storage value by 4
        r=n*x
        print(f"1 bits is equal to : 0.25 Nibbles")
        print(f"4 bits is equal to : 1 Nibbles")
        print(f"{n} Nibble is Equal to : {r} Bits")
        print()

    def bytes(self):
        n = int(input("Enter Your Bytes: "))
        # todo multiply the digital storage value by 8
        r=n*self.one_bytes
        print(f"{n} Bytes is Equal to : {r} Bits")
        print()

    def kilobytes(self):
        n = int(input("Enter Your KiloBytes: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_kilobyte
        print(f"{n} KB is Equal to : {r} Bytes")
        print()

    def megabytes(self):
        n = int(input("Enter Your MegaBytes: "))
        # todo multiply the digital storage value by 1024
        r=n*self.one_megabyte
        print(f'{n} MB is Equal to : {r} KiloBytes')
        print()

    def gigabyte(self):
        n = int(input("Enter Your GB: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_gigabyte
        print(f'{n} GB is Equal to : {r} Megabytes')
        print()

    def terabyte(self):
        n = int(input("Enter Your TeraByte: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_terabyte
        print(f'{n} TB is Equal to : {r} Gegabytes')
        print()

    def Petabyte(self):
        n = int(input("Enter Your PetaaByte: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_petabyte
        print(f'{n} PB is Equal to : {r} Terabytes')
        print()

    def Exabyte(self):
        n = int(input("Enter Your ExaByte: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_Exabyte
        print(f'{n} EB is Equal to : {r} Petaabytes')
        print()

    def ZetaByte(self):
        n = int(input("Enter Your ZetaByte: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_zetabyte
        print(f'{n} ZB is Equal to : {r} Exabyte')
        print()

    def YottaByte(self):
        n = int(input("Enter Your YetaByte: "))
        # todo multiply the digital storage value by 1024
        r = n * self.one_Yottabyte
        print(f'{n} YB is Equal to : {r} ZetaByte')
    def excess(self):
       self.bits(),self.nibble(),self.bytes(),self.kilobytes(),self.megabytes(),self.gigabyte(),self.terabyte(),self.Petabyte(),self.Exabyte(),self.ZetaByte(),self.YottaByte()
r=memory()
r.excess()
