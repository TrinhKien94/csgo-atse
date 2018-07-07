// https://csgoempire.com/#!
var init_balance = parseFloat($('#balance').text());
var betStatus = "false";
var betColor = ['black','black','black'];
var baseBet = [10,10,20];
var countLose = [0,0,0];
var limitLosed = [4,4,4];
var currentBet = [10,10,20];
var betted = [false,false,false];

function detectSituation(){
	var two = $(".list .coin")[8].className.split(" ")[1];
	var three = $(".list .coin")[7].className.split(" ")[1];
	var four = $(".list .coin")[6].className.split(" ")[1];
	var five = $(".list .coin")[5].className.split(" ")[1];
	var six = $(".list .coin")[4].className.split(" ")[1];
	var seven = $(".list .coin")[3].className.split(" ")[1];
	var eight = $(".list .coin")[2].className.split(" ")[1];
	var one = $(".list .coin")[9].className.split(" ")[1];
	// if(one != 'green' && two == 'green'|| one != two && two != three && three == 'green'){
    if(one != 'green' && two == 'green'){
        if(one == 'red')
            betColor[2] = 'black';
        if(one == 'black')
            betColor[2] = 'red';
        console.log("situation 2 bet color: "+betColor[2]);
        // if(three == 'green'){
		// 	betColor[2] = two;
		// }else{
		// 	betColor[2] = one;
		// }
		return 2;
	}
	if(one == 'green' && two == 'green')
		return 1;
    if(one == 'green'){
        betColor[0]='red';
        return 0;
    }
	return -1;
}
function update(){
	var time = service['roulette'].state;
	console.log(time);
	if(time != 'COUNTDOWN'){
		betStatus = "false";
	}
	//Once every round
	if(time == 'COUNTDOWN' && betStatus ===  "false"){
		console.log(betStatus);
		console.log(time);
        var betAll = parseInt($('p.balance span.text-nowrap')[0].innerText);
        for(var i =0 ; i < betted.length; i++){
            if(betted[i]){
                betted[i] = false;
                if(betColor[i] !=  $(".list .coin")[9].className.split(" ")[1]){
                    currentBet[i] = currentBet[i] * 2;	
                }else{
                    currentBet[i] = baseBet[i];
                }
            }
        }
        var situation = detectSituation();
        console.log("Bet situation: "+situation);
		if(situation == 0){
			service['socket'].send({
			    service: 'roulette',
			    cmd: 'deposit',
			    color: 'red',
			    amount: currentBet[situation]
			});
			betted[situation] = true
		}
		// if(situation == 2){
		// 	service['socket'].send({
		// 	    service: 'roulette',
		// 	    cmd: 'deposit',
		// 	    color: 'red',
		// 	    amount: currentBet
		// 	});
		// 	betColor='red';
		// 	betted = true
		// }
		if(situation == 2){
			service['socket'].send({
			    service: 'roulette',
			    cmd: 'deposit',
			    color: betColor[situation],
			    amount: currentBet[situation]
            });
			betted[situation] = true
		}
		betStatus = true;
	}
}
setInterval(update,3889);