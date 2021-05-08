# @senseioffical tarafindan yapılmıştır. 
# 4 farklı hack alanında işinize yarayacak araçları kurmak için kullanabilirsiniz.
# hizmet amaçlı hazırlanmıştır. yapılan hiçbir faaliyetten sorumlu değilim.

import os 
import sys
import time 
os.system ("apt update && apt upgrade")
os.system ("clear")

print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
while True:
  print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•             ~SENSEİ OFFİCAL HACK TOOL~          •
•                                                 •
•        [0] Yardımcı Paketleri Kurmak İçin       •
•        [1] Bilgi Toplama Araçları               •
•        [2] DDOS Saldırı Araçları                •
•        [3] Şifre Kırma Araçları                 •     
•        [4] Güvenlik Açığı Analiz Araçları       •
•                                                 •
•        [x] Çıkış Yapmak İçin                    •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  """)
  
  karar = input ("Ne Yapmak İstersiniz: ")
  if karar=="x":
    print ("Yine Bekleriz...")
    break

  elif karar=="0":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    print ("Yardımcı Paketler Kuruluyor...")
    os.system ("pkg install python -y")
    os.system ("pkg install python2 -y")
    os.system ("pkg install python3 -y")
    os.system ("pkg install curl -y")
    os.system ("pkg install php -y")
    os.system ("pkg install nano -y")
    os.system ("pkg install vim -y")
    os.system ("pkg install cat -y")
    os.system ("pkg install colorama -y")
    os.system ("pkg install figlet -y")
    os.system ("pkg install toilet -y")
    os.system ("pkg install ruby -y")
    os.system ("pkg install perl -y")
    os.system ("pkg install pip")
    os.system ("pkg install pip2")
    os.system ("pkg install pip3")
    os.system ("pkg install tsu")
    print ("Yardımcı paketler Kuruldu.")
    
  elif karar=="1":
    os.system ("clear")
    print ("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    •                                                •
    •              ~BİLGİ TOPLAMA ARAÇLARI~          •
    •                                                •
    •    [1] Telefon Numarasından Bilgi Toplama      •
    •    [2] TC Kimlik Numarasi Son 2 Hane Bulucu    •
    •    [3] IP Adresinden Konum Bulma               •
    •    [4] Web Sitelerinden Bilgi Toplama          •
    •    [5] İnstagram Hesaplarından Bilgi Toplama   •
    •    [6] İsimden Sosyal Medya Hesap Sorgulama    •
    •    [7] Facebook Hesaplarından Bilgi Toplama    •
    •    [8] Mac Adresleri Hakkinda Bilgi Toplama    •
    •    [9] E-posta'dan Bilgi Toplama               •
    •    [10] phishing Aracı                         •
    •                                                •
    •    [x] Çıkış Yapmak İçin                       •
    •                                                •
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    karar1 = input ("Ne Yapmak İstersiniz: ")
    if karar1=="x":
      print ("Yine Bekleriz...")
      break  
      
    elif karar1=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("PhoneInfoga Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ExpertAnonymous/PhoneInfoga.git")
      print ("PhoneInfoga Kuruldu.")
      
    elif karar1=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      tcnumara = input("TC Kimlik No Ilk 9 Hanesini Giriniz: ")
      def tcno(tcno):
        if len(tcno) == 9:
            a = 7*(int(tcno[0])+int(tcno[2])+int(tcno[4])+int(tcno[6])+int(tcno[8]))
            b = int(tcno[1])+int(tcno[3])+int(tcno[5])+int(tcno[7])
            haneOn = (a-b)%10
            onHaneli=str(tcno)+str(haneOn)
            toplamOn = 0
            for i in range(10):
              toplamOn=toplamOn+int(onHaneli[i])
            haneOnBir = toplamOn%10
            return tcno+str(haneOn)+str(haneOnBir)
      print ("TC Kimlik No'nun Tamami :",tcno(tcnumara))
      
    elif karar1=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("IPGeolocation Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/maldevel/IPGeoLocation.git")
      print ("IPGeolocation Kuruldu.")
      
    elif karar1=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("RED_HAWK Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
      print ("RED_HAWK Kuruldu.")
      
    elif karar1=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("osi.ig Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/th3unkn0n/osi.ig.git")
      print ("osi.ig Kuruldu.")
      
      
    elif karar1=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("userrecon Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/issamelferkh/userrecon.git")
      print ("userrecon Kuruldu.")
      
    elif karar1=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      print ("OSIF Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ciku370/OSIF.git")
      print ("OSIF Kuruldu.")
      
    elif karar1=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("mac-lookup Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ivan-loh/mac-lookup.git")
      print ("mac-lookup Kuruldu.")
      
    elif karar1=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Infoga Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/m4ll0k/Infoga.git")
      print ("Infoga Kuruldu.")
    
    elif karar1=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("ShellPhish Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/AbirHasan2005/ShellPhish.git")
      print ("ShellPhish Kuruldu.")
      
  elif karar=="2":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•             ~DDOS SALDIRI ARAÇLARI~             •
•                                                 •
•        [1] Hammer DDOS Aracı                    •
•        [2] Hulk DDOS Aracı                      •
•        [3] XERXES DDOS Aracı                    •
•        [4] SMS Bomb Aracı                       •
•        [5] Anonim SMS Gönderme                  •
•                                                 •
•        [x] Çıkış Yapmak İçin                    •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    karar2 = input ("Ne Yapmak İstersiniz: ")
    if karar2=="x":
      print ("Yine Bekleriz...")
      sys.exit()
      
    elif karar2=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      print ("Hammer Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/cyweb/hammer.git")   
      print ("Hammer Kuruldu.")
      
    elif karar2=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Hulk kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/grafov/hulk.git")
      print ("Hulk Kuruldu.")
     
    elif karar2=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("XERXES Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/CyberXCodder/XerXes.git")
      print ("XERXES Kuruldu.")
      
    elif karar2=="4":
      os.system ("clear")   
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Impulse Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/LimerBoy/Impulse.git")
      print ("Impulse Kuruldu.")
    
    elif karar2=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("yubasms Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/yuba-0/yubasms.git")
      print ("yubasms kuruldu.")
      
  elif karar=="3":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~ŞİFRE KIRMA ARAÇLARI~               •
•                                                 •
•       [1] Hydra Brute Force                     •
•       [2] İnstagram Brute Force                 • 
•       [3] E-mail brute Force                    •
•       [4] Hash Şifre Kırıcı                     •
•       [5] Wordlist Oluşturucu                   •
•       [6] Instagram brute Force 2               •
•       [7] HashCat Hash şifre Kırıcı             •
•       [8] Katak Toolkit                         •
•       [9] Facebook Brute Force                  •
•       [10] Wi-fi Güvenlik Denetim               •
•                                                 •
•       [x] Çıkış Yapmak İçin                     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    karar3=input ("Ne Yapmak İstersiniz: ")
    
    if karar3=="x":
      print ("Yine Bekleriz...")
      sys.exit()
    elif karar3=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Hydra Kuruluyor...")
      os.system ("apt update")
      os.system ("pkg install tsu")
      os.system ("git clone https://github.com/vanhauser-thc/thc-hydra.git")
      print ("Hydra Kuruldu.")
      
    elif karar3=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Instagram Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Bitwise-01/Instagram-.git")
      print ("Instagram Kuruldu.")
      
    elif karar3=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Brute-Force-gmail Yükleniyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/0xfff0800/Brute-force-gmail.git")
      print ("Brute-Force-gmail Kuruldu.")
    
    elif karar3=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("hasher Kuruluyor...")
      os.system ("apt update")
      os.system ("apt install python2 git")
      os.system ("git clone https://github.com/CiKu370/hasher.git")
      print ("Hasher Kuruldu.")
      
    elif karar3=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("cheekyPassListCreator Kuruluyor...")
      os.system ("git clone https://github.com/mXBozkurt/cheekyPassListCreator.git")
      print ("cheekyPassListCreator Kuruldu.")
      
    elif karar3=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("İnstaHack kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/evildevill/instahack.git")
      print ("İnstaHack Kuruldu.")
      
    elif karar3=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("HashCat Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/hashcat/hashcat.git")
      print ("HashCat Kuruldu.")
      
    elif karar3=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Katak Kuruluyor...")
      os.system ("apt update && apt upgrade")
      os.system ("apt install git python2")
      os.system ("pip2 install requests progressbar")
      os.system ("git clone https://github.com/Gameye98/Katak.git")
      print ("Katak Kuruldu.")
    
    elif karar3=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("FBBrute Kuruluyor...")
      os.system ("apt install git python2")
      os.system ("git clone https://github.com/Gameye98/FBBrute.git")
      print ("FBBrute Kuruldu.")
   
    elif karar3=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Aircrack-ng Kuruluyor...")
      os.system ("apt update")
      os.system ("https://github.com/aircrack-ng/aircrack-ng.git")
      print ("Aircrack-ng Kuruldu.")
      
  elif karar=="4":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•        ~GÜVENLİK AÇIĞI ANALİZ ARAÇLARI~         •
•                                                 •
•      [1] Nmap Ağ Tarama                         •
•      [2] SQLMap Web Site Açık Tarama            • 
•      [3] RED_HAWK Web Site Açık Tarama          •
•      [4] Easymap Web Site Açık Tarama           •
•      [5] AstraNmap Güvenlik Tarayıcısı          •
•      [6] SQLscan SQL Açık Tarayıcı              •
•      [7] Wordpresscan wordpres Tarayıcı         •
•      [8] wpscan Wordpres Açık Tarayıcı          •
•      [9] XAttacker Web Site açık Tarayıcı       •
•      [10] Admin Panel Bulucu                    •
•                                                 •
•       [x] Çıkış Yapmak İçin                     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    karar5 = input ("Ne Yapmak İstersiniz: ")
    if karar5=="x":
      print ("Yine Bekleriz...")
      break
    elif karar5=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Nmap Kuruluyor...")
      os.system ("apt update")
      os.system ("pkg install nmap")
      print ("Nmap Kuruldu.")
      
    elif karar5=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("SQLMap Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/sqlmapproject/sqlmap.git")
      print ("SQLMap Kuruldu.")
      
    elif karar5=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("RED_HAWK Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
      print ("RED_HAWK Kuruldu.")
      
    elif karar5=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
      print ("Easymap Kuruluyor...")
      os.system ("clear")
      os.system ("apt update")
      os.system ("git clone https://github.com/Cvar1984/Easymap.git")
      print ("Easymap Kuruldu.")
      
    elif karar5=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("AstraNamp Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Gameye98/AstraNmap.git")
      print ("AstraNmap Kuruldu.")
      
    elif karar5=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("SQLscan Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Cvar1984/sqlscan.git")
      print ("SQLscan Kuruldu.")
      
    elif karar5=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Wordpresscan Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/swisskyrepo/Wordpresscan.git")
      print ("Wordpresscan Kuruldu.")
      
    elif karar5=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("wpscan Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/wpscanteam/wpscan.git")
      print ("wpscan Kuruldu.")
      
    elif karar5=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("XAttacker Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Moham3dRiahi/XAttacker.git")
      print ("XAttacker Kuruldu.")
      
    elif karar5=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Admin-Panel-Finder Kuruluyor...")
      os.system ("apt update")
      os.system ("git clone https://github.com/bdblackhat/admin-panel-finder.git")
      print ("Admin-Panel-Finder Kuruldu.")
       
  else :
    print ("Lütfen Geçerli Bir Sayı Giriniz!")
       
       
       
      
    
