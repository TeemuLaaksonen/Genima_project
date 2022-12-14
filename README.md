# Genima_project
Small message encryption program made as a studying project for Python basics. More description about the project below (in Finnish).

# Harjoitustyö, Ohjelmoinnin perusteet
## Teemu Laaksonen, AB3688

### Harjoitustyön aihe

Harjoitustyönä on tehty yksinkertainen ohjelma, jonka avulla voi salata viestejä ja purkaa ohjelmalla salattuja viestejä.
Kyseessä on siis kryptaus-ohjelma, jonka inspiraationa on toiminut Alan Turingista ja Enigmasta kertova kirja "Alan Turing: The Enigma ja
kirjan pohjalta tehty elokuva "Imitation Game". Ohjelma on leikkisästi nimetty Genimaksi, joka on sanan Enigma anagrammi.

### Harjoitustyön haastavuus ja työn eteneminen

Harjoitustyö on haastavuudeltaan melko helppo. Ohjelman rakenne on yksinkertainen ja se sisältää neljä funktiota, muutamia muuttujia ja
yksinkertaisen käyttöliittymän. Ohjelman ohjelmoimiseksi tarvittiin Pythonin perusteiden ja syntaksin tunteminen, Base64-moduuli ja Tkinterin
alkeet.

Kun ohjelman idea oli hahmoteltu, tein paperille luonnoksen ohjelman perusosien toiminnoista ja niiden tarvitsemista muuttujista. OHjelman vaatima
koodi vaikutti paperilla hyvin helpolta, mutta jo suunnitteluvaiheessa tiesin, etten osaisi rakentaa toimivaa kryptaus-järjestelmää varsinaisten
salausjärjestelmien ollessa minulle vielä tuntemattomia. Tiesin myös jo alkuvaiheessa, että minun tulisi opetella itsenäisesti Tkinterin alkeet.

Aloitin ohjelman rakentamisen etsimällä stackoverflowsta suuntaa-antavaa ajatusta sopivan salaustavan toteuttamiseksi. Päädyin etsinnän aikana freecodecamp.org-sivustolle,
jossa oli kuvattu hyvin pintapuolisesti ohjelman rakenteiden tausta-ajatus ja toiminta. Toteutin ensimmäisen version ohjelman koodista tämän kuvauksen
mukaisesti, mutta ohjelma ei toiminut ollenkaan tarkoituksenmukaisella tavalla. Stackoverflowsta löysin mahdollisesti soveltuvan salaustavan ajatuksen,
jonka rakentamiseen käytin useita tunteja. Ongelmana oli, etten ymmärtänyt funktion toiminnan periaatetta, siis sitä miten salaus tapahtuu ja mikä on sen matemaattinen kaava.

Kun funktiot toimivat konsolissa molempiin suuntiin, aloin tutustumaan Tkinterin käyttöön ja siihen, miten käyttöliittymä ensinnäkin saadaan käynnistymään
konsolista. Itse käyttöliittymän rakentaminen oli melko helppoa, sillä verkkosivuilta löydetyn ohjeistuksen avulla ymmärsin toiminnan olevan hyvin lähellä
CSS-koodia, josta minulla on kokemusta jo jonkin verran.

Testausvaiheessa ohjelmasta löytyi useita bugeja, joiden korjaamiseen meni pitkä aika. Ohjelma mm. enkryptasi viestin oikein, mutta toimintoa vaihdettaessa
se enkryptasi jo salatun viestin vielä toiseen kertaan. Lisäksi painikkeet, tietotyypit ja funktioiden toiminta vaihteli aina yhden bugin korjaamisen jälkeen.
Tunnetustihan yhden toiminnan korjaamiseksi pitää ensin rikkoa kaksi..

### Harjoitustyön funktioiden toiminta

Harjoitustyön, Geniman, funktiot toimivat seuraavaksi kuvatulla tavalla:

Funktio "encrypt" on rakennettu for-loopilla toimimaan siten, että integerin arvoksi otetaan muuttujana saatavan "message":n pituus. Funktio
looppaa tekstin jokaisen merkin kohdalla asettamalla muuttujan x_key arvoksi integerin ja muuttujan "key" osamäärästä saatavan index-arvon. X-key
muuttujaan lisätään loopin index-arvo ja lopputuloksesta jäävä osamäärä 256:lla jaon jälkeen muutetaan string arvoon ennen sen syöttämistä base64-moduulille suojausta varten.
Enkryptattu merkki lisätään listaan.

Funtion "decrypt" toiminta purkaa salauksen tekemällä "encrypt"-funktioiden toimet päinvastaisessa järjestyksessä.

Näiden edellä mainittujen funktioiden toteuttamiseksi omat valmiuteni Python-ohjelmoinnissa eivät olisi riittäneet, mutta tietoa etsimällä löysin toimivan ratkaisun, jonka
rakentaminen opetti paljon esimerkiksi Base64-moduulin toiminnasta, kryptauksen perusteista ja integerin, sekä stringin yhteen liittämisestä erilaisin toiminnoin.

Funktion "mode_funtion" toiminta on yksinkertainen. If-rakenteella etsitään muuttujan "mode" arvoa, ja sen ollessa "E" suoritetaan "encrypt" funktio, joka saa
muuttujikseen muuttujat "cipher_key" ja "text". Vastaavasti "mode" muuttujan ollessa "D", funtio kutsuu "decrypt"-funktiota.

"Reset"-funktio asettaa muuttujien arvoksi tyhjän stringin. Funktion tarkoituksena on tyhjentää syöttökentät.

### Harjoitustyön oppimistulokset lyhyesti

Harjoitustyön oppimistuloksia:

- Yksinkertaisen graafisen käyttöliittymän rakentaminen Tkinterin avulla
- Base64-moduulin tarkoitus ja toiminnan perusteet
- StringVar()-luokan käyttö perustasolla
- Kryptauksen alkeita
- Stringien ja integerien yhteen liittämistä
- Syöttökenttien tietojen hakemista ja syötteiden muokkaaminen
- Graafisen käyttöliittymän käynnistäminen
- Debugausta, tiedonhakua, ongelmien kuvaamista sanallisesti hakutermeiksi

