function getHistory(){
	var len = $("#bets-list tr").length;
	var prev="";
	for(var i=2; i<= len; i++){
		var value=0;
		var profit =0;
		
		value=$("#bets-list tr:nth-child("+i+") td.value")[0].innerText;
		if($("#bets-list tr:nth-child("+i+") td.lose").length>0){
			profit=$("#bets-list tr:nth-child("+i+") td.lose")[0].innerText;
		}else{
			profit=$("#bets-list tr:nth-child("+i+") td.win")[0].innerText;
		}
		prev += value + '|' + profit+'|';
	}
	prev = prev.slice(0, -1);
	console.log(prev);
	return prev;
}
service['coinflip'].history=function(bet) {
    console.log(bet.amount);
    console.log(bet.profit);
    console.log(bet.option);
    bet.prev=getHistory();
    $.ajax({
        type: "GET",
        data: bet,
        url: "http://127.0.0.1:5003/employees",
        dataType: "json",
        async: false,
        success: function(data){
            bet_color_str = data.predict;
            console.log('predict color: '+data.predict);
        }        
    });
    console.log(bet);
    $('#bets-list tr').slice(14, 15).remove();
    $(tmpl('history-tpl', bet)).css({
        opacity: 0
    }).prependTo('#bets-list').animate({
        opacity: 1
    }, 200);
};