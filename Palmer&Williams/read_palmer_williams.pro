pro read_Palmer_Williams
  common PW_1975,PW_wvlum,PW_wtpc,PW_refri
  read_file_td,'c:\cat.uwyo.edu\Mie_Calc\Palmer&Williams\Palmer&Williams_0.36-7.2um.csv',2,hd$,nr,nc,mpw
  x=getnos(hd$(0)) & PW_wtpc=fltarr((nem1(x)-1)/2) & j=2
  for i=0,nem1(PW_wtpc) do begin
    PW_wtpc(i)=x(j) & j=j+2
  endfor
  PW_wvlum=mpw(*,0) & PW_wvn=mpw(*,1)
  mpw=mpw(*,2:*)
  PW_refri=fltarr(nr,n_elements(PW_wtpc),2) & j=0
  for w=0,nem1(PW_wtpc) do begin
    PW_refri(*,w,0)=mpw(*,j) & j++
    PW_refri(*,w,1)=mpw(*,j) & j++
  endfor
  ;stop
end
