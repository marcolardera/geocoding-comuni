# Geocoding comuni italiani

**Aggiornato con le denominazioni ISTAT del 2023-06-30**

In questo repository fornisco un geocoding (latitudine e longitudine) aggiornato dei comuni italiani, sulla base delle denominazioni ufficiali ISTAT, realizzato tramite l'API [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) di OpenStreetMap.
Ritengo che questi dati dovrebbero essere forniti ufficialmente dall'ISTAT ma, in mancanza di essi, può essere utile avere delle fonti non ufficiali.

Il file contenente il geocoding è `comuni.json`. **DISCLAIMER:** Si tratta di dati di cui non posso garantire la correttezza al 100%, non potendo manualmente verificarli uno ad uno. Nominatim è in genere preciso sulle query per singolo comune, per cui mi aspetto un'accuratezza molto elevata, ma non è impossibile che vi sia qualche imprecisione.

È presente anche lo script Python usato per creare questo dataset. Il delay tra una chiamata API e l'altra è settato a 1 secondo, in accordo con le [policy](https://operations.osmfoundation.org/policies/nominatim/) di Nominatim.

