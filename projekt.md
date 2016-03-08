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
