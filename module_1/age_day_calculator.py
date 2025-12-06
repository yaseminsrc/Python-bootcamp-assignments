# -*- coding: utf-8 -*-
"""age_day_calculator.ipynb

Yaş Gün Hesaplayıcı: Doğum tarihinden bugüne kaç gün yaşandığını hesaplayan program (Doğum tarihinden bugüne kadar geçen gün)    
Age and Day Calculator: Program that calculates the number of days lived from the date of birth to the present day.
"""

from datetime import datetime

doğum = input("Doğum tarihinizi girin (gün/ay/yıl): ")
doğum_tarihi = datetime.strptime(doğum, "%d/%m/%Y")

bugün = datetime.now()

fark = bugün - doğum_tarihi
print(fark.days, " yaşadığınız gün sayısıdır.")


# fonksiyon ile yaparsak
def yaş_gün_hesaplayıcı():
  doğum = input("Doğum tarihinizi girin (gün/ay/yıl): ")
  doğum_tarihi = datetime.strptime(doğum, "%d/%m/%Y")

  bugün = datetime.now()

  fark = bugün - doğum_tarihi
  print(fark.days, " yaşadığınız gün sayısıdır.")

yaş_gün_hesaplayıcı()
