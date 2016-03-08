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
När spelaren klickar på vänster musknapp så skickas en liten kub ut kallad portal_positioner. När detta objekt kolliderar med en del av terrängen så placeras en portal ut på den positionen. Detta är ett simpelt och effektivt sätt att placera ut portalerna på men det har sina problem då den rör sig relativt fort. När objektet rör sig i en hög hastighet (som den behöver göra för en bättre spelupplevelse) så kommer kollisionen inte alltid att upptäckas precis vid väggens kant. Den sker ofta lite innanför. Detta kan motarbetas stort sett på två olika sätt: sänka hastigheten hos objektet eller att placera portalen vid väggens x-position (eller y-position om det är tak eller golv). Första alternativet ville jag inte göra då det skulle ta alldeles för lång tid mellan knapptryck tills portalen är ute. Det andra alternativet är dock en bra utvecklingsmöjlighet som kräver lite arbete. 


#####Rotera portalgun
Då PyGame enbart kan rotera bilder runt bildens mittpunkt så blev det lite bekymmer. Detta löstes genom att att utnyttja cos och sin för att få ut kateterna som när objektet flyttas efter dom så roteras den längs ut med hypotenusan. 

![alt text] (https://github.com/97gushan/Project/blob/master/portalgunposition.png)

#####Teleportering
Portalerna fungerar så att när spelaren kolliderar med en position lite framför själva portalen (denna position beror på vilket rotation portalen har) så teleporteras spelaren till nästa portal. Som skrivit tidigare angående placeringen utav portalerna så kan dom landa en bit inanför marken. Detta har gjort att jag har varit tvungen att sätta denna teleporteringsposition en bit ovanför marken (eller en bit från sidan från väggen beroende på typ av terräng). Detta gör att spelaren teleporteras när denne är en liten bit från portalen vilket inte på något sett ser bra ut men det fungerar. Om man utvecklar spelet och gör så att portalerna placeras ut bättre så kan man lösa detta problem också då det är en mindre variation på vart portalerna placeras. 

#####Portaler med annan vinkel
Grundtanken var att göra så att man kan placera portaler med en vinkel på 45 eller 135 grader. Denna idé blev svår att genomföra med det sätt som portaler placeras ut. Just nu placeras de som skrivet tidigare när portal_positioner kolliderar med en bit terräng. Denna kollisionsdetektion blir komplicerad att göra om väggen som positionern ska kollidera med är vinklad. En möjlig väg att lösa detta problem på är möjligtvis att man utnyttjar räda linjens ekvation. Man använder sig av den för att kolla om x positionen som positionern har ger ett y-värde som överanstämmer med linjens y-värde.
