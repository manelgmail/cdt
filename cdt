:Disp "CAIDA DE TENSION"
:Disp "EN CABLES"
:Disp ""
:Input "CORRIENTE (A)? ", I
:Input "LONGITUD (M)? ", L
:Input "SECCION (MM^2)? ", A
:Disp "1: COBRE"
:Disp "2: ALUMINIO"
:Input "MATERIAL? ", M
:If M=1
:Then
:0.0178→R
:Else
:0.0282→R
:End
:(2*R*L*I)/A→V
:Disp "CAIDA DE TENSION:"
:Disp V
