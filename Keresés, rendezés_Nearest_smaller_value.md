**Rendezés, keresés**

**Legközelebbi kisebb szám (balra)**

**Feladat leírása:**

<https://cses.fi/problemset/task/1645>

Egy pozitív egészeket tartalmazó listában minden elemére meg kell adni a tőle balra lévő első nála kisebb szám sorszámát. Ha nincs ilyen, akkor 0-t kell visszaadni.

**Megoldás magyarázata:**

A megoldás lényege, hogy egyszer megyünk végig („balról jobbra”) a sorozat elemein és a stack listát úgy kezeljük, hogy abban csak a sorozatnak azon tagjainak a **sorszámát** hagyjuk meg illetve tartjuk nyilván, amik az adott elemtől „visszafelé nézve” csökkenő (rész)sorozatot alkotnak. Ez azért fontos, mert így, amikor keressük a balra lévő első legkisebb elemet (pontosabban annak sorszámát), akkor nem kell az összeg korábbi sorozat elemmel összehasonlítani, elég csak a stack-ben nyilvántartott „visszafele nézve” csökkenő sorozatot vizsgálni.

Ezt a célt éri el a while ciklusban az *arr[stack[-1]] >= arr[i]* feltétel: a stack-ből kivesszünk minden az aktuális elemnél kisebb korábban beletett elemet: *stack.pop()*

Ha még marad elem ezek után a stack-ben, akkor megtaláltuk az i. elemtől balra lévő első legkisebb elem sorszámát, ez a stack utolsó eleme. Persze, hogy tényleges, nem 0-tól kezdődő sorszámot kapjunk, hozzá kell, hogy adjunk 1-et, mivel Pythonban a lista indexelés 0-tól n-1-ig történik.

Ha kiürül a stack, akkor az azt jelenti, hogy az aktuális elem az eddigi legkisebb szám és mivel kezdetben csupa 0-val inicializáltuk a result tömbböt, ezért nem kell tenni semmit.

Akár kiürült a stack, akár nem, az aktuális elemet mindenképp betesszük a stack végére, hiszen a következő elemet mindenképpen ezzel kell először összehasonlítani. 
