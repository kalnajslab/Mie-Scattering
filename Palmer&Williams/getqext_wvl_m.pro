pro GetQext_wvl_m,wvlum;,ExtBks$
  ;common  MieCoefficients, mrfr,qr,qxt_wvl_m,qextbks_wvl_tK
  common MieCoefficients;, mrfr,qr,qxt_wvl_m,qext_wvl_tK,qbk_wvl_m,qbks_wvl_tK,m_z
  extdir$='c:\cat.uwyo.edu\Mie_Calc\Extinction\'
  for w=0,nem1(wvlum) do begin
    extfile$=file_search(extdir$+'*'+num2str(wvlum(w)*1e3,'i')+'*.ExtXs')
    read_file_td,extfile$,2,hd$,nr,nc,qxt
    if w eq 0 then begin
      mrfr=getnos(hd$(1))
      qr=qxt(*,0)
      qxt_wvl_m=fltarr(nr,n_elements(wvlum),nc)
    endif
    qxt_wvl_m(*,w,*)=qxt
    ;stop
  endfor
  ;stop,wvlum
end
