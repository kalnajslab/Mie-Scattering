function P_W_1975,wvlin,wtpc_h2so4
  common PW_1975;,PW_wvlum,PW_wtpc,PW_refri
  iwvl=get_index(PW_wvlum,wvlin,1)
  ipc=get_index(PW_wtpc,wtpc_h2so4,1)
  p=fltarr(2,2) & mfin=fltarr(2)
  for mi=0,nem1(mfin) do begin
    p(0,*)=[PW_refri(iwvl,ipc-1,mi),PW_refri(iwvl+1,ipc-1,mi)]
    p(1,*)=[PW_refri(iwvl,ipc,mi),PW_refri(iwvl+1,ipc,mi)]
    mwv0=interpolate_td(p(0,0),p(0,1),PW_wvlum(iwvl),PW_wvlum(iwvl+1),wvlin)
    mwv1=interpolate_td(p(1,0),p(1,1),PW_wvlum(iwvl),PW_wvlum(iwvl+1),wvlin)
    mfin(mi)=interpolate_td(mwv0,mwv1,PW_wtpc(ipc-1),PW_wtpc(ipc),wtpc_h2so4)    
  endfor
  return,mfin
end
