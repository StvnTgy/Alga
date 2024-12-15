**Gráf algoritmusok**

**Kurzusok ütemezése / Course Schedule**

**Feladat leírása:**

<https://cses.fi/problemset/task/1679>

Van néhány (k) kurzusunk és néhány (n) függőségünk.

A függőség azt jelenti, hogy bizonyos kurzusoknak van egy vagy több
előfeltételük vagyis csak akkor lehet elvégezni bizonyos kurzusokat, ha
előtte egy vagy több másik megadott kurzust már elvégeztünk.

Inputként megkapjuk az k-t és az n-t. A kurzusok kódja 1-től k-ig a
pozitív egészek. Ezen kívül kapunk n db. számpárt, amiben az első szám
annak a kurzusnak a kódja, ami előfeltétele a második számmal megadott
kurzusnak.

A kimenet: meg kell adni egy lehetséges (tetszőleges) sorrendet, amiben
a megadott kurzusok -- az előfeltételekben megadott szabályok
betartásával -- elvégezhetők.

**Megoldás magyarázata:**

Némi előkészület után egy viszonylag egyszerű (mohó típusú)
algoritmussal megoldható a probléma.

Az előkészület azt jelenti, hogy a beolvasás során az előfeltételeket
egy olyan listákat tartalmazó listában (*dep_list*) tároljuk el, aminek
a i-1-ik eleme azt tartalmazza, hogy az adott kurzus **melyik másik
kurzusnak vagy kurzusoknak az előfeltétele** (ez lehet üres lista is). A
másik irányból nézve elegendő egy kurzushoz azt nyilvántartani, hogy
annak **hány darab előfeltétele van** (még): *no_of_deps\[\]*

A fő függvény (*find_course_order*) feldolgozás része azzal kezdődik,
hogy összegyűjtjük a *queue*-ban azokat a kurzusokat, amiknek nincs
előfeltétele vagyis a *no_of_deps* értékük 0.

Ha nincs ilyen, akkor el se tud kezdődni a bejárás, ilyenkor az eredmény
természetesen IMPOSSIBLE lesz.

Az algoritmus mindössze annyiból áll, hogy kiveszünk egy elemet az
előfeltétel nélküli kurzusokat tartalmazó *queue*-ból, hiszen ezt
biztosan választhatjuk következő elvégzendőnek és hozzáadjuk a megadandó
elvégzési sorrendhez. Ezen kívül végigmegyünk azokon a kurzusokon,
amiknek ez az aktuális kurzus az előfeltétele (ezt tartjuk nyilván a
dep_list listában) és ezeknek a *no_of_deps* értékét csökkentjük 1-gyel,
hiszen az aktuális kurzus elvégzésével 1-gyel csökken az előfeltételek
száma. És ha ezáltal egy kurzus előfeltételeinek a száma 0-ra csökken
(*if no_of_deps\[neighbor\] == 0:* ), akkor ez is szabadon
elvégezhetővég válik, ezért hozzáadjuk az ilyen kurzusokat tartalmazó
queue-hoz.

Mindez addig folytatódik, amíg a queue-nak van eleme vagyis van még
olyan kurzus aminek eleve nem volt előfeltétele vagy már minden
előfeltételét elvégeztük.

Ha ezek után az összes kurzust elvégeztük (if len(course_order) == n),
akkor meg lehet valósítani a feladatot.

Ha nem, akkor (körkörös hivatkozás miatt) a megadott feltételrendszerben
a kurzusok nem végezhetők el.
