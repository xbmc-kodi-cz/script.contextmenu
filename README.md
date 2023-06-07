# Context Menu
Přidává do kontextového menu Kodi další užitečné položky.

Doplněk přidává do kontextového menu Kodi další položky, které nabízejí řadu specifických a dále popsaných funkcí. Koncepce řešení umožňuje autorovi přidávat další funkce dle libosti a možností, které Kodi nabízí. Doplněk využívá možnost definice kontextového menu nezávislého na konkrétním doplňku, přímo v jeho definičním souboru addon.xml. Z tohoto pohledu je množina funkcí otevřená a pokud někdo přijde s nápadem, jakou funkci by bylo vhodné doplnit, stačí v tomto tématu námět zveřejnit návrh a já se o to (pokud to funkce Kodi dovolí) pokusím.

### Popis řešení a funkcí

V doplňku v současné verzi fungují tři úrovně výběru položek v menu (aplikují se v uvedeném pořadí):
1. **podle nastavení doplňku** - to umožňuje uživateli vybrat si, které položky v menu mohou být zobrazeny
2. **podle stavu dalších doplňků** - pokud je položka v menu vázána na nějaký další doplněk, kontroluje se, zda je doplněk instalovaný a povolený a pokud tomu tak není, tak se položka v menu neobjeví
3. **podle okamžitého kontextu** - zobrazení položek v menu může být podmíněno aktuálním obsahem položky v seznamu, na které bylo kontextové menu vyvoláno

Pozn. Výběr podle 3. kritéria je zpravidla nastaven tak, že v případě, kdy by položka doplňku Context Menu nějak kolidovala (například by ji dublovala) s položkou kontextového menu nějkého dalšího doplňku, tak je její zbrazení potlačeno. Příkladem ja např. dále uvedená položka Přehrát upoutávku. Stejná položka se nachází v kontextovém menu doplňku Stream Cinema Community (SCC), takže při zobrazení seznamu z SCC se v kontextovém menu položka Přehrát upoutávku z doplňku Context Menu nezobrazí.


### Uživatelsky definované položky

Doplněk umožňuje uživatelsky definovat další položky kontextového menu. V současné chvíli je možné definovat až 4 položky a každou z nich umístit do jedné ze čtyř pozic (viz Dostupné položky a jejich funkce níže). Pro každou položku je možné v nastavení doplňku definovat:

- **Povolení položky** - povoluje její zobrazení ve zvolené pozici - defaultně Nepovoleno, tzn. položka nebude zobrazena
- **Pozice** - definuje pozici zobrazení položky v jedné ze čtyř pozic označených jako Horní, 1/4, 3/4 a Dolní) - defaultně Nedefinovaná, tzn. položka nebude zobrazena
- **Název** - označení položky v kontextovém menu - defaultně prázdný řetězec
- **Styl** - stylu fontu názvu Normální, Tučné, Kurzíva a Tučná kurzíva - defaultně Normální
- **Barva** - barva fontu názvu Bílá, Šedá, Modrá, Zelená, Žlutá a Červená - defaultně Bílá
- **Příkaz** - Kodi built-in příkaz, který se vykoná při aktivaci položky kontexového menu - defaultně prázdný řetězec.

K uvedeným parametrům tři poznámky:
Aby se daná položka v kontextovém menu zobrazila je třeba současně jak Povolení položky, tak vybrat jednu ze čtyř pozic jejího umístění (tedy jinou než defaultně Nedefinovaná)
Položky se, kromě možnosti každou povolit či zakázat, zobrazují nepodmíněně a není možné (v dané chvíli) žádnou podmínku (odvozenou od aktuálního kontextu) pro jejich (ne)zobrazení definovat. Původně jsem si myslel, že to půjde, ale ukázalo se, že je to jen velmi obtížně realizovatelné. Zatím to tedy spadá do oblasti To-Do.

Seznam Kodi built-in příkazů najdete ve Wiki Kodi v [List of built-in functions](https://kodi.wiki/view/List_of_built-in_functions), v kombinaci s příkazem Action() je pak možné použít i [Action IDs](https://kodi.wiki/view/Action_IDs).

### Dostupné položky a jejich funkce

**Uživatelsky definované položky** - pozice označená jako **Horní**
**Automatický výběr streamu SCC pro přehrávání** - změní stav Automatický výběr streamu pro přehrávání v nastavení doplňku SCC v sekci Streamy. Funguje jako tzv. "toggle". Zároveň se v kontextovém menu zobrazuje stav do kterého se po jeho aktivaci nastavení přepne (AUTO/RUČNĚ).
**Automatický výběr streamu SCC pro stahování** - změní stav Automatický výběr streamu pro stahování v nastavení doplňku SCC v sekci Streamy. Funguje jako tzv. "toggle". Zároveň se v kontextovém menu zobrazuje stav do kterého se po jeho aktivaci nastavení přepne (AUTO/RUČNĚ).
**Uživatelsky definované položky** - pozice označená jako **1/4**
**Přehrát upoutávku** - spustí přehrávání upoutávky (trailer-u), pokud existuje. V tomto případě se (zatím) v doplňku nekontroluje, zda jsou případně k dispozici doplňky, kterými se upoutávky přehrávají (Youtube, Tubed atp.)
**Hledat...** - spustí funkce Hledat v případě, že je položka nastavení **- submenu hledat** ve stavu **ZAPNUTO**, viz popis funkce hledání dále
**Hledat v SCC** - spustí funkci Hledat z doplňku SCC - Pozn. 1, viz popis funkce hledání dále
**Hledat na Webshare** - spustí funkci Hledat na Webshare z doplňku SCC - Pozn. 1, viz popis funkce hledání dále
**Hledat v SC** - spustí funkci Hledat z doplňku SC - Pozn. 3, viz popis funkce hledání dále
**Hledat na Youtube** - spustí funkci Hledat z doplňku Youtube - Pozn. 2, viz popis funkce hledání dále
**Obnovení obsahu** - provede tzv. **Refresh**, tedy nové načtení aktuálně zobrazeného seznamu
**Odstranit** - u položky, kde je to v rámci Kodi možné a povolené, se provede její "odstranění". Odstraněním je míněná akce (Action ID Delete) v daném kontextu, dle typu a stavu položky. Pokdu není v daném kontextu tato akce definovaná, neprovede se samozřejmě nic.
**Uživatelsky definované položky** - pozice označená jako **3/4**
**Nastavení doplňku** - spustí funkci nastavení doplňku v případě, že aktuálně zobrazený seznam byl nějakým doplňkem vytvořený
**Nastavení Kodi** - spustí funkci nastavení Kodi
**Nastavení menu** - spustí funkci nastavení doplňku Context Menu
**Uživatelsky definované položky** - pozice označená jako **Dolní**

Poznámka: Tyto položky jsou v aktuální verzi doplňku zablokovány, protože jsou vázány na existenci dalších, dosud nezveřejněných doplňků. Teprve, až budou tyto doplňky zveřejněny, budou funkce uvolněny také.
Pozn. 1: předpokládá instalovaný doplněk Stream Cinema Community
Pozn. 2: předpokládá instalovaný doplněk Youtube
Pozn. 3: předpokládá instalovaný doplněk Stream Cinema CZ a SK

## ToDo

- hledání v Netflix - zatím nejisté, pravděpodobně to nepůjde
- hledání v HBO - ani jsem nezačal
- hledání v knihovně - také nejisté, ale věřím, že to nakonec dohromady dám...

## Instalace

Doplněk je určen pouze pro Kodi verze 20 (Nexus) a případně vyšší. Důvodem je, že používá funkce, které jsou v Kodi dostupné právě od této verze. Úpravu doplňku pro nižší verze Kodi nepředpokládám.
Doplněk se v Kodi instaluje do sekce Místní nabídky/Context Menus. Po první instalaci je třeba restartovat Kodi. Tento postup je třeba provést s ohledem na funkce Kodi, které jsou v tomto doplňku použity.