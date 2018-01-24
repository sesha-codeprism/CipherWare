def  create_array(plain_text,length):

    for i in  range(0,length):

       if str[i]=='A':
            a[i]=0
            break
       elif str[i] == 'B':
          a[i] = 1
          break
       elif str[i] == 'C':
          a[i] = 2
          break
       elif str[i] == 'D':
          a[i] = 3
          break
       elif str[i] == 'E':
          a[i] = 4
          break
       elif str[i] == 'F':
          a[i] = 5
          break
       elif str[i] == 'G':
          a[i] = 6
          break
       elif str[i] == 'H':
          a[i] = 7
          break
       elif str[i] == 'I':
          a[i] = 8
          break
       elif str[i] == 'J':
          a[i] = 9
          break
       elif str[i] == 'K':
          a[i] = 10
          break
       elif str[i] == 'L':
          a[i] = 11
          break
       elif str[i] == 'M':
          a[i] = 12
          break
       elif str[i] == 'N':
          a[i] = 13
          break
       elif str[i] == 'O':
          a[i] = 14
          break
       elif str[i] == 'P':
          a[i] = 15
          break
       elif str[i] == 'Q':
          a[i] = 16
          break
       elif str[i] == 'R':
          a[i] = 17
          break
       elif str[i] == 'S':
          a[i] = 18
          break
       elif str[i] == 'T':
          a[i] = 19
          break
       elif str[i] == 'U':
          a[i] = 20
          break
       elif str[i] == 'V':
          a[i] = 21
          break
       elif str[i] == 'W':
          a[i] = 22
          break
       elif str[i] == 'X':
          a[i] = 23
          break
       elif str[i] == 'Y':
          a[i] = 24
          break
       elif str[i] == 'Z':
        a[i] = 25
        break
    return a



  def encrypt_array(a,length):
      for i in range (1,length):
       a[i] =  a[i] + 5
      return a

 def print_array(a,length):

    for i in  range(0,length):

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
  print(a)