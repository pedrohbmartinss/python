import math
angulo = int(input('Digite um angulo: '))
print('O seno de {} graus é: {:.1f} \nO cosseno de {} graus é: {:.1f} \nA tangente de {} graus é: {:.1f}'.format(angulo, math.sin(math.radians(angulo)), angulo, math.cos(math.radians(angulo)), angulo, math.tan(math.radians(angulo))))