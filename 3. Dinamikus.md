**Dinamikus programozás**

**Feladat leírása:**

<https://www.hackerrank.com/challenges/decibinary-numbers/problem>

Röviden magyarul a decibináris számok olyan számok, amikben 0-tól 9-ig
fordulhatnak elő számjegyek de a helyiértékek nem a 10, hanem a 2
hatványai.

A feladat az, hogy megmondjuk, hogy melyik decibináris szám áll a k.
helyen, ha elsődlegesen az értékük, majd a tízes számrendszerbelinek
tekintett alakjuk szerint rendezzük őket növekvő sorrendben.

Egész pontosan n db. ilyen kérdésre kell egy futtatás során válaszolni n
db. számmal.

Az első néhány decibináris szám sorrendbe állítása:

x		DeciBinaryNumber	Decimal
1		0					0
2		1					1
3		2					2
4		10					2
5		3					3
6		11					3
7		4					4
8		12					4
9		20					4
10		100					4
...
20		110					6

Észre lehet venni, hogy több decibináris szám is van, aminek ugyanaz a
(decimális) értéke, ez adja a feladat -- egyik -- nehézségét.

**A megoldás magyarázata:**

Az inputok beolvasása után meghívásra kerül a fő függvény, a
find_dbn(q), amit a n db. inputból álló listával hívjuk meg vagyis
egyszerre válaszolunk az összes kérdésre és nem n-szer kerül meghívásra
a find_dbn. (dbn =DeciBinaryNumber)

A fő algoritmus azt csinálja, hogy 1-től kezdődően megszámolja, hogy
hány olyan decibináris szám van, ami az adott (1,2,3, ... stb.) értéket
veszi fel. Ezeket 0-tól kezdve (0 értékű decibináris számból 1 van,
egyébként 1 értékűből is 1 db., ezt kényelmi okokból külön kezeltem az
algoritmus elején) összegezve vizsgálni kell, hogy mikor haladja meg egy
q kérdéslistában szereplő valamelyik sorszám értéket.

Ehhez a vizsgálathoz a q listát rendeztem, de előbb egy dictionary-ben
eltároltam, hogy az egyes értékek milyen pozícióban szerepeltek
eredetileg, hogy a választ tartalmazó tömbben vissza lehessen állítani
az eredeti sorrendet.

Az adott értékkel rendelkező decibináris számok összeszámolása rekurzív
módon történik. Esetekre bontjuk aszerint, hogy az egyes helyiértéken
milyen számjegy áll. Ez páratlan esetben 1,3,5,7 és 9, míg páros esetben
0,2,4,6 vagy 8 lehet. Ha ezt kivonjuk a számból, akkor egy olyan számot
kapunk, aminek az 1-es helyiértékén 0 áll. Vagyis páros és ha leosztjuk
2-vel, akkor észrevehetjük, hogy az történik a számmal, hogy letöröljük
a 0-t a végéről és számjegyek eggyel jobbra tolódnak (a decibináris
számrendszer miatt). Vagyis egy x számot páratlan esetben
visszavezethetjük a (x-1)/2, (x-3)/2, ... (x-9)/2 lehetséges decibináris
alakjainak számára: ezen esetek összegével egyenlő az x decibináris
alakjainak a száma. Ehhez az esetre bontáshoz van szükség a paritás
vizsgálatra. (parity = i % 2)

A current változóban számoljuk az 1-tól indított külső while ciklus
aktuális elemének (i) az esetszámát, amit a szum változóban összegzünk.
Ha a szum változó értéke eléri vagy meghaladja a q lista aktuális
(cursor-ral index-szelt) elemét, az azt jelenti, hogy a q. sorszámú
decibináris szám értéke i. Csak még azt nem tudjuk, hogy ezek közül
pontosan melyik.

Ennek kiderítésére szolgált a get_all_dbn_equal_to(i,memo) függvény.
Ennek a második paramétere egy gyorsabb futást szolgáló, a korábbi
eredményeket eltároló dictionary (memo). Ez a függvény visszaadja azon
decibináris számol listáját, amelyek értéke i. Ezt szintén rekurzív,
pontosabban mivel eltároljuk az eddigi eredményeket, ezért lényegében
dinamikus módon tesszük a fentebb leírt módon a páros és páratlan
eseteket különbontva az 1-esek számától függően visszavezetjük az adott
esetet egy 1-gyel kevesebb számjegyből álló esetre.

A miután a get_all_dbn_equal_to függvény visszatér ezzel a listával (és
az eltárolt eddigi eredményekkel), ki kell választani belőle a megfelelő
decibináris számot. Ezt pedig éppen az a különbség adja meg, ami az
eddig összegzett darabszámok és az adott kérdésben szereplő q szám
között van: ennyivel „mentünk túl" a keresett számon vagyis a lista
ennyiedik legnagyobb elemére van szükségünk, amire a python beépített
heapy osztályának nlargest függvényét használtam.

Ezután az eredti sorszámokat tartalmazó dictionary-ben visszakeressük,
hogy a válasz tömb hanyadik elemébe írjuk be a megkapott értéket.
