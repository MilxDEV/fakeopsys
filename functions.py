def BasMath(task,numb1,numb2):

  if task == "összeadás" or task == "+":
      return numb1 + numb2
  elif task == "kivonás" or task == "-":
      return numb1 - numb2
  elif task == "szorzás" or task == "*":
      return numb1 * numb2
  elif task == "osztás" or task == "/":
      return numb1 / numb2
  


def exit(message):
    print(message)
    running = False



def commands():
    print("##################################")
    print("###        HELP Page     (1/1) ###")
    print("###  - Basic Calculator        ###")
    print("###  - Time                    ###")
    print("###  - Clear                   ###")
    print("##################################")


def clear():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("*** Console Cleared ***")