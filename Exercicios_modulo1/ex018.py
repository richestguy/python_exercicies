from math import sin, cos, tan, radians
ang = int(input('Digite um angulo'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O angulo de {} tem o COSENO de {:.2f}'.format(ang, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
