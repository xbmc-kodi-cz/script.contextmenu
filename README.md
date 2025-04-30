# Context Menu
Přidává do kontextového menu Kodi další užitečné položky.

Doplněk přidává do kontextového menu Kodi další položky, které nabízejí řadu specifických a dále popsaných funkcí. Koncepce řešení umožňuje autorovi přidávat další funkce dle libosti a možností, které Kodi nabízí. Doplněk využívá možnost definice kontextového menu nezávislého na konkrétním doplňku, přímo v jeho definičním souboru addon.xml. Z tohoto pohledu je množina funkcí otevřená a pokud někdo přijde s nápadem, jakou funkci by bylo vhodné doplnit, stačí v tomto tématu námět zveřejnit návrh a já se o to (pokud to funkce Kodi dovolí) pokusím.

### Popis řešení a funkcí

V doplňku v současné verzi fungují tři úrovně výběru položek v menu (aplikují se v uvedeném pořadí):
1. **podle nastavení doplňku** - to umožňuje uživateli vybrat si, které položky v menu mohou být zobrazeny
2. **podle stavu dalších doplňků** - pokud je položka v menu vázána na nějaký další doplněk, kontroluje se, zda je doplněk instalovaný a povolený a pokud tomu tak není, tak se položka v menu neobjeví
3. **podle okamžitého kontextu** - zobrazení položek v menu může být podmíněno aktuálním obsahem položky v seznamu, na které bylo kontextové menu vyvoláno

**Poznámka:** Výběr podle 3. kritéria je zpravidla nastaven tak, že v případě, kdy by položka doplňku Context Menu nějak kolidovala (například by ji dublovala) s položkou kontextového menu nějkého dalšího doplňku, tak je její zbrazení potlačeno. Příkladem ja např. dále uvedená položka Přehrát upoutávku. Stejná položka se nachází v kontextovém menu doplňku Stream Cinema Community (SCC), takže při zobrazení seznamu z SCC se v kontextovém menu položka Přehrát upoutávku z doplňku Context Menu nezobrazí.

### Dostupné položky a jejich funkce

- **Uživatelsky definované položky** - pozice označená jako **Horní**
- DELETED **Automatický výběr streamu SCC pro přehrávání** - změní stav Automatický výběr streamu pro přehrávání v nastavení doplňku SCC v sekci Streamy. Funguje jako tzv. "toggle". Zároveň se v kontextovém menu zobrazuje stav do kterého se po jeho aktivaci nastavení přepne (AUTO/RUČNĚ).
- DELETED **Automatický výběr streamu SCC pro stahování** - změní stav Automatický výběr streamu pro stahování v nastavení doplňku SCC v sekci Streamy. Funguje jako tzv. "toggle". Zároveň se v kontextovém menu zobrazuje stav do kterého se po jeho aktivaci nastavení přepne (AUTO/RUČNĚ).
- **Uživatelsky definované položky** - pozice označená jako **1/4**
- **Přehrát upoutávku** - spustí přehrávání upoutávky (trailer-u), pokud existuje. V tomto případě se (zatím) v doplňku nekontroluje, zda jsou případně k dispozici doplňky, kterými se upoutávky přehrávají (Youtube, Tubed atp.)
- **Hledat upoutávku** - vyhledá v Youtube upoutávku podle titulu (i Originálního, pokud existuje) aktuání položky, text hledaného titulu, případně i originálního titulu, je v hledaném řetězci doplněn klíčovými slovy trailer a teaser
- **Uživatelsky definované položky** - pozice označená jako **-1/2**
- **Hledat...** - spustí funkce Hledat v případě, že je položka nastavení **- submenu hledat** ve stavu **ZAPNUTO**, viz popis funkce hledání dále
- **Hledat v TMDb** - spustí funkci Hledat z doplňku TMDb Helper. Hledání v TMDb Helper má omezené chování kvůli bug-u v samotném doplňku, který v přípdě, že hledaný titul nenajde, končí s chybou. - viz popis funkce hledání dále
- **Hledat na Webshare** - spustí funkci Hledat na Webshare z doplňku YAWSP - viz popis funkce hledání dále
- **Hledat v SCC** - spustí funkci Hledat z doplňku SCC - viz popis funkce hledání dále
- DELETED **Hledat na Webshare** - spustí funkci Hledat na Webshare z doplňku SCC - viz popis funkce hledání dále
- DELETED **Hledat v SC** - spustí funkci Hledat z doplňku SC - viz popis funkce hledání dále
- **Hledat v Netflix** - spustí funkci Hledat z doplňku Netflix - viz popis funkce hledání dále
- **Hledat na Youtube** - spustí funkci Hledat z doplňku Youtube - viz popis funkce hledání dále
- **Smart hledání TMDb - Webshare** - spustí funkci Smart hledání z TMDb Helper doplňku na Webshare prostřednictvím doplňku YAWSP
- **Uživatelsky definované položky** - pozice označená jako **+1/2**
- **Obnovení obsahu** - provede tzv. **Refresh**, tedy nové načtení aktuálně zobrazeného seznamu
- **Odstranit** - u položky, kde je to v rámci Kodi možné a povolené, se provede její "odstranění". Odstraněním je míněná akce (Action ID Delete) v daném kontextu, dle typu a stavu položky. Pokdu není v daném kontextu tato akce definovaná, neprovede se samozřejmě nic.
- **Uživatelsky definované položky** - pozice označená jako **3/4**
- **Nastavení doplňku** - spustí funkci nastavení doplňku v případě, že aktuálně zobrazený seznam byl nějakým doplňkem vytvořený
- **Nastavení Kodi** - spustí funkci nastavení Kodi
- **Nastavení menu** - spustí funkci nastavení doplňku Context Menu
- **Uživatelsky definované položky** - pozice označená jako **Dolní**

### Uživatelsky definované položky

Doplněk umožňuje uživatelsky definovat další položky kontextového menu. V současné chvíli je možné definovat až 4 položky a každou z nich umístit do jedné ze čtyř pozic (viz **Dostupné položky a jejich funkce** výše). Pro každou položku je možné v nastavení doplňku definovat:

- **Povolení položky** - povoluje její zobrazení ve zvolené pozici - defaultně Nepovoleno, tzn. položka nebude zobrazena
- **Pozice** - definuje pozici zobrazení položky v jedné ze čtyř pozic označených jako Horní, 1/4, 3/4 a Dolní) - defaultně Nedefinovaná, tzn. položka nebude zobrazena
- **Název** - označení položky v kontextovém menu - defaultně prázdný řetězec
- **Styl** - stylu fontu názvu Normální, Tučné, Kurzíva a Tučná kurzíva - defaultně Normální
- **Barva** - barva fontu názvu Bílá, Šedá, Modrá, Zelená, Žlutá a Červená - defaultně Bílá
- **Příkaz** - Kodi built-in příkaz, který se vykoná při aktivaci položky kontexového menu - defaultně prázdný řetězec.

K uvedeným parametrům dvě poznámky:

1. Aby se daná položka v kontextovém menu zobrazila je třeba současně jak Povolení položky, tak vybrat jednu ze čtyř pozic jejího umístění (tedy jinou než defaultně Nedefinovaná)
2. Seznam Kodi built-in příkazů najdete ve Wiki Kodi v [List of built-in functions](https://kodi.wiki/view/List_of_built-in_functions), v kombinaci s příkazem Action() je pak možné použít i [Action IDs](https://kodi.wiki/view/Action_IDs).

### Funkce hledání

1. Funkce hledání má dva módy, které se volí v nastavení doplňku. Pokud je položka nastavení **- submenu hledat** ve stavu **VYPNUTO**, objeví se v kontetxovém menu se objeví všechny aktuálně zapnuté funkce hledání. Pokud je je položka nastavení **- submenu hledat** ve stavu **ZAPNUTO**, je v kontext menu vždy zobrazena pouze položka **Hledat...** Po její volbě se spustí funkce hledání a volba místa hledání uživatel provede v další posloupnosti funkcí.
2. Funkci **Hledat** lze generálně vypnout pomocí stejnojmenné položky v nastavení. Nastavení ostatních parametrů zůstane uloženo, jen se v kontextovém menu žádné položka funkce hledání neobjeví.
3. Po spuštění funkce z kontextového menu se nejdříve zobrazí možnost výběru textů z aktuální položky. Uživatel má možnost vybrat z nabízeného seznamu více položek. Ty se budou skládat jedna za druhou a budou odděleny mezerou. U některých položek (kde to není možné jednoduše odvodit) je zobrazen jejich význam (kurzívou). Platí, že všechny psané kurzívou texty se do výsledného textu nepřenáší.
4. Pokud se některý text objeví ve více položkách (například režisér je zároveň i scénárista) a uživatel si vybere obě položky, tak ve výsledném textu bude tento text pouze jednou. Od verze 0.1.15 je přidána možnost neprovádět výběr textů z aktuální položky. V takovém případě se do hledaného textu uloží první text z aktuální položky, což zpravidla bývá titul. V nastavení je položka pro aktivaci této možnosti označena jako - nevybírat položku hledaného textu (použije se titul) a je defaultně vypnuta. Doplněk se tedy po instalaci této verze bude chovat stále stejně jako dosud a budete-li chtít tuto možnost aktivovat, je třeba ji v nastavení zapnout.
5. Uživatel má v této fázi možnot vybraný text buď potvrdit - tlačítko **OK** - nebo zrušit - tlačítko **Zrušit**. Pokud zvolí druhou možnost, do dalšího kroku se přenese prázdný řetezec.
6. Následuje tradiční virtuálni klávesnice, kde si uživatel může text editovat a pak si vybrat, co bude následovat. Pokud tady zvolí tlačítko **OK**, přejde se k dalšímu kroku, pokud **Zrušit**, funkce hledání se ukončí.Od verze 0.1.15 je přidána možnost editaci textu přeskočit. V nastavení je položka pro aktivaci této možnosti označena jako - neupravovat hledaný text a je defaultně vypnuta. Doplněk se tedy po instalaci této verze bude chovat stále stejně jako dosud a budete-li chtít tuto možnost aktivovat, je třeba ji v nastavení zapnout.
7. Posledním krokem je spuštění vlastního vyhledávání. Pokud je nastaveno **- submenu hledat** na **VYPNUTO**, tak se hledání v daném místě spustí hned po zadání **OK** v předchozím bodu. Pokud je **- submenu hledat** nastaveno na **ZAPNUTO**, objeví se seznam obsahující všechna místa, kde je možné hledat a uživatel si z nich jedno vybere. Po výběru se hledání spustí.

### To Do

- hledání v HBO - ani jsem nezačal
- hledání v knihovně - také nejisté, ale věřím, že to nakonec dohromady dám...

## Instalace

Doplněk je určen pouze pro Kodi verze 20 (Nexus) a případně vyšší. Důvodem je, že používá funkce, které jsou v Kodi dostupné právě od této verze. Úpravu doplňku pro nižší verze Kodi nepředpokládám.

Doplněk se instaluje z repozitáže **XBMC-Kodi CZ/SK repozitář**, verze minimálně **1.3.0**. Doplněk najdete v sekci repozitáře **Služby**. Po instalaci je doplněk pro správu dostupný v sekci **Místní nabídky** a **Služby**. Po první instalaci je třeba restartovat Kodi. Tento postup je třeba provést s ohledem na funkce Kodi, které jsou v tomto doplňku použity.

Pokud jste před první instalací doplňku z repozitáře používali doplněk instalovaný ze zip, můžete ho bez problémů tím z repozitáře přeinstalovat. Po instalaci ale doporučuji provést restart Kodi. Po instalaci doplňku z repozitáře budou daší aktualizace probíhat, samozřejmě pokud to máte v Kodi i dopplňku nastavené, automaticky.