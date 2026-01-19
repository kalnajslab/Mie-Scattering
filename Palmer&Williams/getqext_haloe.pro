pro GetQext_Haloe,wvlum,refrindex
  common MieCoefficients;,mrfr,qr,qxt_wvl_m,qextbks_wvl_tK
  ;extdir$='c:\cat.uwyo.edu\Mie_Calc\HALOE_EXT\'
  extdir$='c:\cat.uwyo.edu\Mie_Calc\Extinction\'
  mrfr=0
  for w=0,nem1(wvlum) do begin
    halofid$=file_search(extdir$+'*'+num2str(wvlum(w)*1e3,'i')+'*.ExtXs')
    read_file_td,halofid$,2,hd$,nr,nc,qxthalo
    qr=qxthalo(*,0) & qxthalo=qxthalo(*,2:*)
    mri$=findreplace(hd$(1),')',',') & mri$=findreplace(hd$(1),'(',',') & mi=getnos(mri$)
    mri=fltarr(n_elements(mi)/2,2)
    j=0
    for i=0,nem1(mri(*,0)) do begin
      mri(i,0)=mi(j) & j++ 
      mri(i,1)=mi(j) & j++
    endfor
    r=get_index(mri(*,0),refrindex(w,0),1)
    i=get_index(mri(*,1),refrindex(w,1),1)
    if w eq 0 then qxt_wvl_m=fltarr(nr,n_elements(wvlum))
    qxt_wvl_m(*,w)=qxthalo(*,r+i)
    ;stop,refrindex(w,*),r+i
  endfor
;stop
end