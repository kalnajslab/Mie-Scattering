pro start_here,wvlum
  common MieCoefficients, mrfr,qr,qxt_wvl_m,qext_wvl_tK,qbk_wvl_m,qbks_wvl_tK,m_z
  WVppmv=4.5 
  if wvlum(0) lt 3.0 then begin
    read_Palmer_Williams & GetQext_wvl_m,wvlum     ;read_Palmer_Williams is necessary to set up the common block used by P_W_1975, but this only needs to be done once.
  endif else begin
    GetQext_haloe,wvlum,refrindex
  endelse
end