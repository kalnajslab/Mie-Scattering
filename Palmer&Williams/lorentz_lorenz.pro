function Lorentz_Lorenz,Tk,hPa,WVppmv,wvlum
  wtn=0
  wtpc_h2so4_300=sulfate_wtpc_h2so4(hPa,300,WVppmv) & wtfrac_h2so4=wtpc_h2so4_300/100
  r300=solution_density(wtfrac_h2so4,wtn,300)
  m300=P_W_1975(wvlum,wtpc_h2so4_300)
  wtpc_h2so4=sulfate_wtpc_h2so4(hPa,Tk,WVppmv) & wtfrac_h2so4=wtpc_h2so4/100
  rh2so4=solution_density(wtfrac_h2so4,wtn,Tk)
  A=(m300^2-1)/((m300^2+2)*r300)
  m_T=sqrt((2*A*rh2so4+1)/(1-A*rh2so4))
  ;m_T=nint(m_T*100)/100.
  if A(1) lt 0 then m_T(1)=m300(1)
  return,m_T
end