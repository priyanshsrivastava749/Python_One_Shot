try:
  with (
    open('1.txt','r') as f1,
    open('2.txt','r') as f2,
    open('3.txt','r') as f3
  ):
    content1 = f1.read()
    content2 = f2.read()
    content3 = f3.read()
    print(content1)
    print(content2)
    print(content3)

except Exception as e:
  print(e)