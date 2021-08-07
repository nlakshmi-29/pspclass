def file_Creation():
     ofile=open("Sample.txt","w+")
     choice=True
     while True:
            line=input("\n Enter a sentence")
            ofile.write(line)
            choice=input("Enter more?-Y/N")
            if choice=='N':break
     ofile.close()
     def Reverse_Content():
      ofile=open("Sample.txt","r")
      k=ofile.readlines()
      t=reversed(k)
      for i in t:
           print(i.rstrip())
