Function Molecular_Bks,lambda_um,prsPa,tempK
  Qmol=fltarr(5)
  Kb = 1.38064852d-23                     ;m2 kg/s2/K = N m/K = J/K Boltzmann's constant
  dair=0.6d-9                             ;diameter of air molecule
  lambda_m=lambda_um*1d-6
  ref_lambda=[0.355,0.532,1.064]
  mair=[1.0002857,1.0002782,1.000274]            ;index of refraction air Hostetler et al.
  depolV=[0.0301,0.02,0.073]                     ; Vega and Antuna
  depolH_total=[0.01554,0.01441,0.014]           ; Total Rayleigh depolarization, Hostetler et al. Table 4.2
  depolH_Cabannes=[0.003945,0.003656,0.003523]   ; 532 nm depolarizaion, Cabannes line, Hostetler et al. Eq 4.4 and Table 4.2 
  k_bw=[1.0153,1.0142,1.0137]                    ; Hostetler et al. Table 4.2 
  d=get_index(ref_lambda,lambda_um,0)
  if d ge 0 then begin
    depolV=depolV(d) & depolH=depolH_Cabannes(d) & k_bw=k_bw(d) & mair=mair(d)
  endif
  lidar_ratio=(8*!pi/3)*k_bw                     ;Hostetler et al.
  Ns=101325/(Kb*288.15)                          ;molecules/m3 at STP
  mair2=(mair^2-1)^2/(mair^2+2)^2
  L_mns=lambda_m^4*Ns^2
  
  Nm=prsPa/(Kb*tempK) ;air molecules/m3
  ;Qmol(0) = 6.2259E-28 / lambda_um^4 * (0.532^4)   ;Qmol = 6.2259E-28 '*1.E8 'um^2 per steradian, for wavelength of 532 nm.
  k=nem1(qmol)-5
  ;Qmol(k)=2*!pi^5*dair^6/(3.*lambda_m^4) * mair2               ;m2
  Qmol(k+1) = 5.1e-31                                          ;m2 scattering cross section for nitrogen m2 at 532 nm
  Qmol(k+2)=5.45e-27*(0.55/lambda_um)^4 * 0.01^2               ;m2 sr-1 ;http://lidar.ssec.wisc.edu/papers/pp_thes/node4.htm
  Qmol(k+3)=8*!pi^3*(mair^2-1)^2/(3*L_mns)*(6+3*depolV)/(6-7*depolV) ;m2 Vega & Antuna
  Qmol(k+3)=Qmol(k+3)/10                                            ;correction identified by Juan Carlos in email June 2019.
  Qmol(k+4)= 9*!pi^2/L_mns * mair2 * (6+3*depolV)/(6-7*depolV) ;m2 Reddy & Kumar
  Qmol(k+5)=24*!pi^3/L_mns * mair2 * (3+6*depolH)/(3-4*depolH) ;m2 Hostetler et al.
  Qmol(k+5)=Qmol(k+5)/lidar_ratio

  Molbks=Qmol(k+5)*Nm                                             ; m-1 sr-1
  ;stop,Ns,Nm,molbks
  Molbks=Molbks*1e3                                          ;m-1 sr-1 *1000m/km = km-1 sr-1
  Return,MolBks
end 
;Hostetler et al. 2006: https://www-calipso.larc.nasa.gov/resources/pdfs/PC-SCI-201v1.0.pdf
;Vega and Antuna, 2017: http://www.sedoptica.es/Menu_Volumenes/Pdfs/OPA_50_1_49013.pdf
;Reddy and Kumar, 2013: https://www.researchgate.net/publication/288048626_Micro_Pulse_Lidar_as_a_Tool_for_Active_Remote_Sensing_of_Atmospheric_Particulate