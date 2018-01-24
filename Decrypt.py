def  create_array(str,length):

    for i in  range(0,length):

       if str[i]=='A':
            arr[i]=0
            break
       elif str[i] == 'B':
          arr[i] = 1
          break
       elif str[i] == 'C':
          arr[i] = 2
          break
       elif str[i] == 'D':
          arr[i] = 3
          break
       elif str[i] == 'E':
          arr[i] = 4
          break
       elif str[i] == 'F':
          arr[i] = 5
          break
       elif str[i] == 'G':
          arr[i] = 6
          break
       elif str[i] == 'H':
          arr[i] = 7
          break
       elif str[i] == 'I':
          arr[i] = 8
          break
       elif str[i] == 'J':
          arr[i] = 9
          break
       elif str[i] == 'K':
          arr[i] = 10
          break
       elif str[i] == 'L':
          arr[i] = 11
          break
       elif str[i] == 'M':
          arr[i] = 12
          break
       elif str[i] == 'N':
          arr[i] = 13
          break
       elif str[i] == 'O':
          arr[i] = 14
          break
       elif str[i] == 'P':
          arr[i] = 15
          break
       elif str[i] == 'Q':
          arr[i] = 16
          break
       elif str[i] == 'R':
          arr[i] = 17
          break
       elif str[i] == 'S':
          arr[i] = 18
          break
       elif str[i] == 'T':
          arr[i] = 19
          break
       elif str[i] == 'U':
          arr[i] = 20
          break
       elif str[i] == 'V':
          arr[i] = 21
          break
       elif str[i] == 'W':
          arr[i] = 22
          break
       elif str[i] == 'X':
          arr[i] = 23
          break
       elif str[i] == 'Y':
          arr[i] = 24
          break
       elif str[i] == 'Z':
        arr[i] = 25
        break
    return arr

def decrypt_array(arr,key):
    for i in range (1,25):
      for j in range(0, length-1):
         arr[i] = arr[i] - key
        if arr[i] > 26:
              arr[i] = arr[i] % 26
          elif arr[i] < 0:
              arr[i] = arr[i] + 26

    return arr

def print_array(arr,length):

    for i in  range(0,length-1):

       if str[i]== 0:
            a[i]='A'
            break
       elif str[i] == 1:
          a[i] = 'B'
          break
       elif str[i] == 2:
          a[i] = 'C'
          break
       elif str[i] == 3:
          a[i] = 'D'
          break
       elif str[i] == 4:
          a[i] = 'E'
          break
       elif str[i] == 5:
          a[i] = 'F'
          break
       elif str[i] == 6:
          a[i] = 'G'
          break
       elif str[i] == 7:
          a[i] = 7
          break
       elif str[i] == 8:
          a[i] = 'I'
          break
       elif str[i] == 9:
          a[i] = 'J'
          break
       elif str[i] == 10:
          a[i] = 'K'
          break
       elif str[i] == 11:
          a[i] = 'L'
          break
       elif str[i] == 12:
          a[i] = 'M'
          break
       elif str[i] == 13:
          a[i] = 'N'
          break
       elif str[i] == 14:
          a[i] = "O"
          break
       elif str[i] == 15:
          a[i] = 'P'
          break
       elif str[i] == 16:
          a[i] = 'Q'
          break
       elif str[i] == 17:
          a[i] = 'R'
          break
       elif str[i] == 18:
          a[i] = 'S'
          break
       elif str[i] == 19:
          a[i] = 'T'
          break
       elif str[i] == 20:
          a[i] = 'U'
          break
       elif str[i] == 21:
          a[i] = 'V'
          break
       elif str[i] == 22:
          a[i] = 'W'
          break
       elif str[i] == 23:
          a[i] = 'X'
          break
       elif str[i] == 24:
          a[i] = 'Y'
          break
       elif str[i] == 25:
        a[i] = 'Z'
        break
