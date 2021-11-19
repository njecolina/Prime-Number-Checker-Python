def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number %i == 0:
      is_prime = False
  if is_prime == True:
    print("It IS a prime number.")
  else:
    print("It's NOT a prime number.")

print('''
 ▄▄▄·▄▄▄  ▪  • ▌ ▄ ·. ▄▄▄ .     ▐ ▄ ▄• ▄▌• ▌ ▄ ·. ▄▄▄▄· ▄▄▄ .▄▄▄  
▐█ ▄█▀▄ █·██ ·██ ▐███▪▀▄.▀·    •█▌▐██▪██▌·██ ▐███▪▐█ ▀█▪▀▄.▀·▀▄ █·
 ██▀·▐▀▀▄ ▐█·▐█ ▌▐▌▐█·▐▀▀▪▄    ▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▪·•▐█•█▌▐█▌██ ██▌▐█▌▐█▄▄▌    ██▐█▌▐█▄█▌██ ██▌▐█▌██▄▪▐█▐█▄▄▌▐█•█▌
.▀   .▀  ▀▀▀▀▀▀  █▪▀▀▀ ▀▀▀     ▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀▀▀ .▀  ▀
 ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄                                 
▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·                               
██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄                                
▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌                               
·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀  version 0.0.1''')
print("by Sonja Hranjec 2021. - github.com/njecolina")

n = int(input("\nCheck this number: "))
prime_checker(number = n)
