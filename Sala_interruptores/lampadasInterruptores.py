interruptor_A = False
interruptor_B = False
interruptor_C = False

lampada_a = "apagada"
lampada_b = "apagada"
lampada_c = "apagada"

estado1 = "fria"
estado2 = "quente"

interruptor_B = True
lampada_b = "ligada"

interruptor_B = False
interruptor_A = True

if interruptor_A:
    lampada_a = "ligada"
if not interruptor_B:
    lampada_b = estado2
lampada_c = estado1

resultado={
    "Interruptor A":lampada_a,
    "Interruptor B":lampada_b,
    "Interruptor C":lampada_c
}
for interruptor,lampada in resultado.items():
    print(f'{interruptor}:{lampada}')