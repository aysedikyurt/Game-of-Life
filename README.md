## Game of Life
 İkinci projemiz Conway'in Hayat Oyunu'ndan esinlenildi. 

Biz popülasyon değişimini değil de günümüzle de ilgili olan bir hastalığın yayılma örüntüsünü inceledik.

Burada '0' yani beyaz kareler sağlıklı insanları ifade ederken; '1' yani siyah kareler hasta insanları ifade etmektedir. Üst, alt, sağ ve sol olmak üzere yalnızca 4 komşuya bakılarak bir hücrenin durumuna karar verilecek. Ayrıca kenarı oluşturan hücreler yalnızca iki komşuları oldukları için değişmeyecekler. Kurallar:
1. Bir hücrenin komşularında 2'den fazla hasta hücre varsa kendisi de bir sonraki döngüde hasta olur.
2. Bir hücrenin komşularında 2'den az hasta varsa kendisi de bir sonraki döngüde iyileşir.
3. Bir hücrenin komşuları eşit sayıda hasta ve sağlıklı hücre içeriyorsa kendi durumunda da bir değişiklik olmaz.

Şimdi kodumuzun nasıl çalıştığını rahatça görebilmek adına az boyutlu, 5x5'lik (length=5) bir random matrisle çalıştıralım:


![Random matrix (5x5)](./h%C3%BCcreler/h%C3%BCcre1.png)

Bir sonraki adımda:

-(3,1)'deki siyah hücrenin beyaz olmasını beklerim, yani iyileşir.

-(2,3)'deki beyaz hücrenin ise siyaha dönmesini beklerim, hasta olur.

Kodumuzu çalıştırp bir sonraki döngüye baktığımızda:

![Matrix](./h%C3%BCcreler/h%C3%BCcre2.png)

İnceleyebilmek adına küçük boyutlu bir matris kullanmıştık. Şimdi bir de büyük boyutlarda (100x100) yaptığımızda neler oluyor ona bakalım.

![matrix(50,50)](./h%C3%BCcreler/h%C3%BCcre3.png)

Bir sonraki zaman diliminde hücrelerimiz aşağıdaki şekilde gözükür.

![matrix](./h%C3%BCcreler/h%C3%BCcre4.png)

Böylece hastalık dağılımının simülasyonunu yapmış oluyoruz. Burada yalnızca 2 zaman döngüsünde incelemiş olduk. Döngü sayısı arttırılarak çıkan örüntü de incelenebilir. Hatta güncel hastalık yayılım verilerine göre düzenlenerek hastalığın gelecekte nasıl bir yayılım izleyeceğine dair öngörülerde de bulunulabilir.

## Ekibimizin adı: molecular
    -Nisa Tan
    -Ayşe Nur Dikyurt


