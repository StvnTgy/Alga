**Rekurzióval megoldható feladatok**

**SPOJ – Recursive sequence**

**Feladat leírása**

<https://www.spoj.com/problems/SEQ/>

Röviden magyarul:

Meg van adva a sorozat első k tagja illetve a k+1-tól kezdve egy lineáris rekurzív képzési szabály az előző k-tag alapján. Meg van k db. együttható, amivel az előző k tag egyes tagjait be kell szorozni, majd ezek összeadásával kapjuk a következő tagot.

A feladat: a k szám, az első k tag, és a k db. együttható segítségével számoljuk ki az n. tagot, egy inputban több (C), legfeljebb 1000 teszteset is szerepelhet.

**A megoldás magyarázata:**

A C érték beolvasása után egy C-szer ismétlődő for ciklust nyitunk a C db. tesztesetnek.

A b tömbbe beolvasott első k. db. tagot deque-ba tároljuk el, mert a feldolgozás során folyamatosan adunk hozzá és vágunk le ebből, így ez lényegesen gyorsabb deque-val, mint sima listával.

A megoldás során (kiszamol) különválasztjuk azt az esetet, amikort a kért sorszám (n) kisebb vagy egyenlő, mint a megadott k elemszám. Ilyenkor egyszerűen visszaadjuk a megkapott k elem közül az n.-iket.

Ha n nagyobb, mint k, akkor n-k szor meghívjuk a rekurziós eljárást k-től n-ig. A rekurzió a az i. tagtól megadott k elemre visszaadjuk az i+1.-től számított k db. elemből álló listát. Amivel aztán újra meghívásra kerül az eljárást, a már említett n – k – szor. Ekkor jutunk el egy olyan listához, aminek az utolsó eleme a keresett n. tag, tehát a return b[k-1]-vel kell visszatérni.
