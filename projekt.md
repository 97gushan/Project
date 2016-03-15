##Projektbeskrivning
Detta projekt är en prototyp till ett fysikbaserat 2D spel som bygger på koncept från spelet Portal. 
Spelaren ska kunna placera ut två portaler för att sedan kunna färdas från den ena till den andra. 
Momentum bevaras  vilket ger grunden till spelmekaniken. För att klara av nivån uttnytjar man sig utav
den hastighet man har samlat upp för att rikta om den med hjälp utav dessa portaler. 

Projektet ska skrivas i Python med biblioteket PyGame och Windows är den plattform som spelet ska riktas till. 

Fysikberäkningarna kommer fokuseras mest kring kaströrelser med framförallt vinklar som 0,90,180,270 grader men möjligtvis även
45 och 135 graders vinklar. 


####Referenser:
http://www.pygame.org/docs/ref/



##Analys

#####Placera portaler
När spelaren klickar på en musknapp så skickas en liten kub ut kallad portal_positioner. När detta objekt kolliderar med en del av terrängen så placeras en portal ut på den positionen. Detta är ett simpelt och effektivt sätt att placera ut portalerna på men det har sina problem då den rör sig relativt fort. När objektet rör sig i en hög hastighet (som den behöver göra för en bättre spelupplevelse) så kommer kollisionen inte alltid att upptäckas precis vid väggens kant. Den sker ofta lite innanför. Detta kan motarbetas stort sett på två olika sätt: sänka hastigheten hos objektet eller att placera portalen vid väggens x-position (eller y-position om det är tak eller golv). Första alternativet ville jag inte göra då det skulle ta alldeles för lång tid mellan knapptryck tills portalen är ute. Det andra alternativet är dock en bra utvecklingsmöjlighet som kräver lite arbete. 

Då kollision mellan positioner och terräng kollar om positionern är innanför terrängen leder det ibland till lite andra buggar när positionern rör sig i en hög hastighet. Ibland kan koden tolka att portalen vill sättas upp på en vägg istället för ett tak då positionern är innanför båda men koden kollar på kollision för väggar först. Detta bekymmer kan lösas genom att antingen sänka hastigheten hos positionern eller att man försöker hitta en annan lösning på placering utav portaler. 

![alt text] (https://github.com/97gushan/Project/blob/master/positioner_bug.png)


#####Rotera portalgun
Då PyGame enbart kan rotera bilder runt bildens mittpunkt så blev det lite bekymmer. Detta löstes genom att att utnyttja cos och sin för att få ut kateterna som när objektet flyttas efter dom så roteras den längs ut med hypotenusan. 

![alt text] (https://github.com/97gushan/Project/blob/master/portalgunposition.png)

#####Teleportering
Portalerna fungerar så att när spelaren kolliderar med en position lite framför själva portalen (denna position beror på vilket rotation portalen har) så teleporteras spelaren till nästa portal. Som skrivit tidigare angående placeringen utav portalerna så kan dom landa en bit inanför marken. Detta har gjort att jag har varit tvungen att sätta denna teleporteringsposition en bit ovanför marken (eller en bit från sidan från väggen beroende på typ av terräng). Detta gör att spelaren teleporteras när denne är en liten bit från portalen vilket inte på något sett ser bra ut men det fungerar. Om man utvecklar spelet och gör så att portalerna placeras ut bättre så kan man lösa detta problem också då det är en mindre variation på vart portalerna placeras. 

#####Portaler med annan vinkel
Grundtanken var att göra så att man kan placera portaler med en vinkel på 45 eller 135 grader. Denna idé blev svår att genomföra med det sätt som portaler placeras ut. Just nu placeras de som skrivet tidigare när portal_positioner kolliderar med en bit terräng. Denna kollisionsdetektion blir komplicerad att göra om väggen som positionern ska kollidera med är vinklad. En möjlig väg att lösa detta problem på är möjligtvis att man utnyttjar räda linjens ekvation. Man använder sig av den för att kolla om x positionen som positionern har ger ett y-värde som överanstämmer med linjens y-värde.

#####Fysik
Det finns två olika funktioner som gör fysiska beräkningar. För att få en rörelse som känns bra när man spelar och då jag inte räknar något på hur lång tid som har förflutit sedan programmet startade valde jag att använda mig utav en konstant utöver delta_tiden. Detta för att det annars skulle ge en väldigt låg acceleration neråt vilket inte skulle vara intressant att spela med. 

#####Terräng
Terrängen fungerar i grund och botten att det är en linje som placeras ut när objektet skapas. Sedan om det är ett tak eller golv så fylls området över respektive under med en grå låda. Då all terräng är utplacerade för hand kommer kanten på alla tak och golv alltid vara i kontakt med en vägg. Detta försäkrar att ingen vägg kommer vara placerad mitt ute i ingenstans. 

Kollision mellan spelare och terräng har även den samma problem som tidigare positionering. Dock så rör sig spelaren i en betydligt lägre hastighet vilket förenklar saker och ting. Problemet blir inte lika stort då kollisionen kan upptäckas innan spelaren har rört sig allt för långt in.

#####Highscore
Då det inte finns något sätt att direkt förlora på i spelet eller någon direkt poäng att spara undan så valde jag att när användaren trycker på "i" så skickas POST kommandot till URLn med kommandot "highscore" och ett slumpat tal som ska simulera poäng. Servern tar då och läser av kommandot för att sedan kolla om den nya poängen slår någon av de äldre. Slås något av de tio poängen så flyttas de undre ner ett steg. Sedan sparas den nya highscore-listan till databasen igen. 

När en användare går in på highscore-sidan via nätet (97gushan.pythonanywhere.com) så tas highscorelistan från databasen. Sedan läggs vilken position varje värde har, värdet och sist en br-tagg (för att hoppa ned en rad) till i en lista som sedan returneras och då även skrivs ut för användaren.
