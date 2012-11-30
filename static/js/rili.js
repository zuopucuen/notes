var cale = new Calendar("idCalendar", { 
onToday: function(o){ o.className = "onToday"; }, 
onFinish: function(){ 
$("idCalendarYear").innerHTML = this.Year; $("idCalendarMonth").innerHTML = this.Month; 
for(i in this.Days){ 
this.Days[i].innerHTML = "<a href=\"/?date="+this.Year+"-"+this.Month+"-"+ i +"\">" + i + "</a>"; 
} 
} 
}); 
$("idCalendarPre").onclick = function(){ cale.PreMonth(); } 
$("idCalendarNext").onclick = function(){ cale.NextMonth(); } 

